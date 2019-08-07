from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.


class UserManager(BaseUserManager):


	def _create_user(self, username, email, password, 
					is_staff, is_superuser, **extra_field):

		if not email:
			raise ValueError("El campo email es necesario")
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, is_active=True, is_staff=is_staff,
							is_superuser=is_superuser, **extra_field)
		user.set_password(password)
		user.save(using = self._db)

		return user

	def create_user(self, username, email, password=None, **extra_field):
		return self._create_user(username, email, password, False, False,  **extra_field)

	def create_superuser(self, username, email, password, **extra_field):
		return self._create_user(username, email, password, True, True,  **extra_field)




class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=50, unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=True)



	objects = UserManager()
	USERNAME_FIELD = 'username'
	PASWORD_FIELD = 'password'
	REQUIRED_FIELDS = ['email', 'password']

	def get_short_name(self):
		return self.username


















# from django.db import models

# # Create your models here.


# class User(models.Model):
# 	Nickname = models.CharField(max_length=50, unique=True)
# 	Email = models.EmailField(max_length=50, unique=True)
# 	Nombres = models.CharField(max_length=100)
# 	Apellidos = models.CharField(max_length=100)


# 	def __str__(self):
# 		return self.Nombres


