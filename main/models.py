from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import CustomerManager

class Customer(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField('username', max_length=256)
    firstName = models.CharField('Имя', max_length=256,null=True)
    secondName = models.CharField('Фамилия', max_length=256,null=True)
    is_active = models.BooleanField(default=True)
    account_type = models.CharField("Тип", max_length=30)
    admin = models.BooleanField(default=False) # a superuser
    verif_time = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomerManager()

    def has_perm(self, perm, obj=None):
        if self.admin:
            return True

    def has_module_perms(self, app_label):
        if self.admin:
            return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        if self.account_type == 'mod' or self.account_type == 'admin':
            return True
        return False
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email