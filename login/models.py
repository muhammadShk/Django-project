from django.db import models
from datetime import datetime
import re 

class UserManager(models.Manager):
    def registration_validator(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['first_name']) < 2:
            errors["first_name"] = " First name should be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors["last_name"] = " Last name should be at least 2 characters"

        if len(post_data['email']) == 0:
            errors["email"]="enter email"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        if len(post_data['password']) < 8:
            errors['password'] = "password cannot be less then 8 charaters long"
        
        if post_data['password'] != post_data['password_conf']:
            errors['password_conf'] ='passwords dont match'     

        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors['email'] = 'email already exists'
        
        # if post_data['birthday'] > datetime.date.today():
        #     error['birthdate']= "We dont accept time travellers"

        return errors

    def login_validator(self, post_data):
        errors = {}
        if len(User.objects.filter(email=post_data['login_email'])) == 0:
            errors['login_email']= 'email does not exist'
        return errors



class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()



