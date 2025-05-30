from django.db import models

# Create your models here.

class Register (models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=30)
	last_login = models.DateTimeField(null=True, blank=True)  # Optional: To track last login time
	
	def __str__(self):
		return self.email

class Contact(models.Model):
    cname = models.CharField(max_length=30)
    cnumber = models.CharField(max_length=30)
    cemail = models.CharField(max_length=30)
    cservice = models.CharField(max_length=30)
    ccomment = models.CharField(max_length=100)