from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors ={}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'El nombre debe tener al menos 2 caracteres'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'El apellido debe tener al menos 2 caracteres'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['register_email']):    
            errors['register_email'] = "La dirección de correo electrónico debe ser válida."
        if len(postData['register_password']) < 8:
            errors['register_password'] = 'El password debe tener al menos 8 caracteres'
        if postData['register_password'] != postData['confirm']:
            errors['register_password'] = "La contraseña debe ser la misma"
        return errors
    def login_validator(self, postData):
        errors ={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['login_email']):    
            errors['login_email'] = "La dirección de correo electrónico debe ser válida."
        if len(postData['login_password']) < 8:
            errors['login_password'] = 'El password debe tener al menos 8 caracteres'
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=60)
    date_of_birth= models.DateField(blank=False, null=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)  
    objects = UserManager()
def __str__(self):
    return f"<{self.first_name} {self.last_name} {self.email} {self.books_uploaded} {self.id}>"
