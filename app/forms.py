from django import forms
from app.models import Events
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#define here our ProfileModelForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields  = ['username', 'email', 'first_name','last_name','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your unique username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter your confirm password'
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'
            
        })
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'type': 'datetime-local'
            
        })
            



class UserLoginForm(forms.ModelForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
 
 
class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(EventsForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'type': 'datetime-local'
            
        })