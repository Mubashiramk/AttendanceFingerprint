from django import forms


class StudentForm(forms.Form):
    classes = (
        ("1", "CSE-GAMMA"),
        ("2", "CSE-BETA"),
        ("3", "CSE-ALPHA"),
        ("4", "IT"),
        ("5", "MECH-ALPHA"),
    )
    classname = forms.ChoiceField(choices=classes)
    date = forms.DateField()
    hour = forms.IntegerField(label="Enter the hour", min_value=1, max_value=7)
    subcode = forms.CharField()
