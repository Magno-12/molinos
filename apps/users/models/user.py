import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers.user_manager import UserManager


class User(AbstractBaseUser):
    ADMIN = 'admin'
    EMPLOYEE = 'empleado'
    INVOICE = 'facturas'

    ROLE_CHOICES = [
        (ADMIN, _('Admin')),
        (EMPLOYEE, _('Empleado')),
        (INVOICE, _('Facturas')),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ADMIN,
    )
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return self.email
