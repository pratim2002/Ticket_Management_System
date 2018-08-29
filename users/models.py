from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .validators import UsernameValidator

USER_ROLES = Choices(
    'admin',
    'employee',
)

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("User must have a valid email address.")

        if not kwargs.get('username'):
            raise ValueError("User must have a valid username.")

        user = self.model(
            username=kwargs.get('username').strip(),
            email=self.normalize_email(email),
            first_name=kwargs.get('first_name', None),
            last_name=kwargs.get('last_name', None),
            is_active=kwargs.get('is_active', True),
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.role = 'admin'
        user.is_active = True
        user.save()

        return user

class User(AbstractBaseUser):
    """
    User Model
    """
    username    = models.CharField(
        max_length=254,
        unique=True,
        validators=[UsernameValidator()],
        error_messages={
            'unique':'User with this username already exists.',
        },
    )
    email       = models.EmailField(_('email address'), unique=True, error_messages={'unique':'User with this email already exist.'})
    first_name  = models.CharField(_('first name'), max_length=254, blank=True, null= True)
    last_name   = models.CharField(_('last name'), max_length=254, blank=True, null=True)
    is_active   = models.BooleanField(_('active'), default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        full_name = self.first_name

        if self.last_name:
            full_name = full_name + '' + self.last_name

        return full_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users_user"

