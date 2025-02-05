from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SignInForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False, 
        initial=False, 
        widget=forms.CheckboxInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply CSS classes to text fields only
        self.fields['username'].widget.attrs.update({'class': 'textbox', 'placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class': 'textbox', 'placeholder':'Password'})

        for field in self.fields.values():
            field.label = ''
