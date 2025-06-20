from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, CompatibilityProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'index_number', 'password1', 'password2']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'index_number': forms.TextInput(attrs={'placeholder': 'Enter index number'}),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )


class CompatibilityForm(forms.ModelForm):
    class Meta:
        model = CompatibilityProfile
        exclude = ['user']
        widgets = {
            'music_choice': forms.Select(choices=[
                ('Gospel', 'Gospel'), ('Hip-Hop', 'Hip-Hop'), ('Afrobeat', 'Afrobeat'), ('Other', 'Other')
            ]),
            'cleanliness': forms.Select(choices=[
                ('Tidy', 'Tidy'), ('Average', 'Average'), ('Messy', 'Messy')
            ]),
            'sleep_schedule': forms.Select(choices=[
                ('Early Bird', 'Early Bird'), ('Night Owl', 'Night Owl')
            ]),
            'noise_level': forms.Select(choices=[
                ('Quiet', 'Quiet'), ('Moderate', 'Moderate'), ('Loud', 'Loud')
            ]),
            'study_preference': forms.Select(choices=[
                ('Alone', 'Alone'), ('Group', 'Group')
            ]),
            'religion': forms.Select(choices=[
                ('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Other', 'Other')
            ]),
            'favorite_color': forms.TextInput(attrs={'placeholder': 'e.g. Blue'}),
            'health_issues': forms.Textarea(attrs={'rows': 2}),
            'additional_info': forms.Textarea(attrs={'rows': 2}),
        }