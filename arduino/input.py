list = ['a','b','c','d','e','f','g','h','i','j','k','l']
f=open("match.ino","r")
text=f.read()
f.close()
f=open("test.ino","w")
result=""
result+="\nswitch (finger.fingerID) { "
for i in range(len(list)):
    result+="\n case "+str(i)+":\n   lcd.print(\""+list[i]+"\");\n   break;"
result+="\n default:\n   lcd.print(\"error\");\n}\n"
text=text.replace("$replacetext",result)
f.write(text)
f.close()