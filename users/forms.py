from django import forms
from .models import Profile


# Create your forms here.

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("avatar", "skill", "phone",)

        

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['avatar'].widget.attrs['class'] = 'form-control'
        self.fields['skill'].widget.attrs['class'] = 'form-control mb-2'
        
