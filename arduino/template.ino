#include <Adafruit_Fingerprint.h>
#include<LiquidCrystal.h>
#include <EEPROM.h>

SoftwareSerial mySerial(2, 3);
LiquidCrystal lcd(8,9,10,11,12,13);

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

int uploadButtonPin = 4;   // choose the input pin (for a pushbutton)
int uploadButtonVal = 0; 

uint8_t id;

int address = 0;  // EEPRM address acounter

void setup()  
{
  pinMode(uploadButtonPin, INPUT); 
  uploadButtonVal = digitalRead(uploadButtonPin);  // read input value

  Serial.begin(9600);
  while (!Serial);  // For Yun/Leo/Micro/Zero/...
  delay(100);
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.clear();
  lcd.print("Sensor Enrollment");

  // set the data rate for the sensor serial port
  finger.begin(57600);
  
  if (finger.verifyPassword()) {
    lcd.clear();
    lcd.print("Found sensor");
  } else {
    lcd.clear();
    lcd.print("Fail : Found");
    while (1) { delay(1); }
  }

  for (int i = 0 ; i < EEPROM.length() ; i++) {
    if(i == EEPROM.length() - 1) {
      address = 0;
      break;
    }
    if(EEPROM.read(i) != 0)
    {
      continue;
    } else {
      address = i;
      break;
    }
  }
}

void loop()                     
{ 
  lcd.clear();
  lcd.print("Getting Ready");
  delay(1000);
  while (!  findFingerPrint() );
}

uint8_t findFingerPrint() {

  int p = -1;

  lcd.setCursor(0,0);
  lcd.clear();
  lcd.print("Waiting...");
  delay(2000);
  while (p != FINGERPRINT_OK) {

    int newUploadButtonVal = digitalRead(uploadButtonPin);  // read input value
    if (newUploadButtonVal != uploadButtonVal) {
      lcd.clear();
      lcd.print("Uploading.");

      printTemp();
      uploadButtonVal = newUploadButtonVal;
      delay(1000);

      lcd.clear();
      lcd.print("Prss agn to CLR");

      delay(3000);

      int newUploadButtonVal = digitalRead(uploadButtonPin);  // read input value
      if (uploadButtonVal != newUploadButtonVal) {
        lcd.clear();
        lcd.print("Clearing.");

        clearEEPROM();
        uploadButtonVal = newUploadButtonVal;
        delay(2000);
      }

    }

    p = finger.getImage();
    switch (p) {
      case FINGERPRINT_OK:
        break;
      case FINGERPRINT_NOFINGER:
        lcd.clear();
        lcd.print("Waiting...");
        break;
      case FINGERPRINT_PACKETRECIEVEERR:
        lcd.clear();
        lcd.print("Commication error");
        delay(2000);
        break;
      case FINGERPRINT_IMAGEFAIL:
        lcd.clear();
        lcd.print("Imaging error");
        delay(2000);
        break;
      default:
        lcd.clear();
        lcd.print("Unknown error");
        delay(2000);
        break;
    }
  }

  // OK success!

  p = finger.image2Tz(1);
  switch (p) {
    case FINGERPRINT_OK:
      lcd.clear();
      lcd.print("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      lcd.clear();
      lcd.print("Image too messy");
      delay(2000);
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      lcd.clear();
      lcd.print("Communication error");
      delay(2000);
      return p;
    case FINGERPRINT_FEATUREFAIL:
      lcd.clear();
      lcd.print("ERR: No fingerprint");
      delay(2000);
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      lcd.clear();
      lcd.print("ERR: No fingerprint");
      delay(2000);
      return p;
    default:
      lcd.clear();
      lcd.print("Unknown error");
      delay(2000);
      return p;
  }

  
  p = finger.fingerFastSearch();
  switch (p) {
    case FINGERPRINT_OK:
      EEPROM.write(address, finger.fingerID );         //write value to current address counter address
      address++;                      //increment address counter
      if(address == EEPROM.length())  //check if address counter has reached the end of EEPROM
      {
        address = 0;              //if yes: reset address counter
      }

      lcd.clear();
    $replacetext
      delay(2000);
      break;
    case FINGERPRINT_NOTFOUND:
      lcd.clear();
      lcd.print("Not match");
      delay(2000);
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      lcd.clear();
      lcd.print("ERR: Packet");
      delay(2000);
      break;
    default:
      lcd.clear();
      lcd.print("Unknown error");
      delay(2000);
      break;
  }
lcd.clear();
  lcd.print("Put finger");
  delay(2000);

  return p;
}


void printTemp()
{
  for (int i = 0 ; i < EEPROM.length() ; i++) {
    byte value = EEPROM.read(i);                //read EEPROM data at address i
    if(value != 0)                              //skip "empty" addresses
    {              
      Serial.println(value);
    }
  }
  Serial.println("EOF");
}


void clearEEPROM()
{
  for (int i = 0 ; i < EEPROM.length() ; i++) {
    if(EEPROM.read(i) != 0)                     //skip already "empty" addresses
    {
      EEPROM.write(i, 0);                       //write 0 to address i
    }
  }
  
  lcd.clear();
  lcd.print("EEPROM erased");
  address = 0;                                  //reset address counter
}
