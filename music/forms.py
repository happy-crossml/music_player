from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms  
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'palaceholder':'Enter Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'palaceholder':'Re Enter Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def save(self, commit=True):
        user =  super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user    
                
class LoginForm(forms.Form):
    username =  forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
            if not user.is_active:
                raise forms.ValidationError("User is not active")
        return super(LoginForm, self).clean(*args, **kwargs)