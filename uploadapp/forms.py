from django import forms


class StudentForm(forms.Form):
    classes = (
        ("1", "outputs"),
        ("2", "CSE-BETA"),
        ("3", "CSE-ALPHA"),
        ("4", "IT"),
        ("5", "MECH-ALPHA"),
    )
    subjects = (
        ("1", "CSE306"),
        ("2", "CSE409"),
        ("3", "CSE105"),
        ("4", "CSE104"),
        ("5", "CSE107"),
    )
    classname = forms.ChoiceField(choices=classes)
    date = forms.DateField()
    hour = forms.IntegerField(label="Enter the hour", min_value=1, max_value=7)
    subcode = forms.ChoiceField(choices=subjects)
