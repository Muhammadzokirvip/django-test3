from django.shortcuts import render
from myapp.models import LoginSigin

login_instance = LoginSigin.objects.create(login_name='John', email='john@example.com', title='Title', body='Body', icon='icon.png')
