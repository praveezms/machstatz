from django import forms
from .models import User

#create your forms here

class StudentsRegistations(forms.ModelForm):
    class Meta:
        model = User
        fields  = ['firstname','lastname','email','password']
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }

    