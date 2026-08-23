from django import forms

class userform(forms.Form):
    num1 = forms.CharField(label="username",widget=forms.TextInput(attrs={"placeholder":"UserName",}))
    num2 = forms.CharField(label="sirname")
    gender = forms.ChoiceField(
    choices=[
        ("male", "Male"),
        ("female", "Female"),
    ],
    widget=forms.RadioSelect()
)
    