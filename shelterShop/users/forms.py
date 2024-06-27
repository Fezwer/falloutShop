from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        label=False,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Логин'}),
        help_text='',
    )
    email = forms.CharField(
        label=False,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Почта'}),
    )
    password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
    )
    password2 = forms.CharField(
        label=False,
        strip=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
    )


    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=False,
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Логин'}),
        help_text='',
    )
    password = forms.CharField(
        label=False,
        strip=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
    )
    

class CustomChangePasswordForm(PasswordChangeForm):
    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')

    old_password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Старый пароль'}),
        help_text=''
    )
    new_password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль'}),
    )
    new_password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль повторно'}),
    )

    # def save(self, commit=True):
    #     user = self.user
    #     new_password = self.cleaned_data["new_password1"]

    #     user.set_password(new_password)
    #     if commit:
    #         user.save()
    #     return user
    

    

