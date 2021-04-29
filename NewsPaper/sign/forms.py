from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.mail import send_mail
from datetime import datetime

class UserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email')
    first_name = forms.CharField(label = 'Имя 1')
    last_name = forms.CharField(label = 'Фамилия 1')

    class Meta:
        model = User
        fields = ("username", 'first_name','last_name','email','password1','password2',)

    def save(self, comit=True):
        user = super(BaseRegisterForm, self).save(commit=True)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        send_mail(
            subject = 'Registration on the news portal NewsPaper',
            message = f'Hello {user.username}! You are registered on the news portal NewsPaper.',
            from_email = 'evgen2007@bk.ru',
            recipient_list = [f'{user.email}']
        )
        return user

    # def sen_email():
