from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.cache import cache

from api.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password):
        user = self.model(
            email=UserManager.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nickname, password):
        user = self.model(
            email=email,
            nickname=nickname,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name='이메일'
    )
    nickname = models.CharField(
        max_length=10,
        blank=False,
        unique=True,
        verbose_name='닉네임'
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app `app_label`?
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Is the user a member of staff?
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = '유저들'  # verbose_name_plural Permission(models.Model)
        ordering = ['-created_at']

    def __str__(self):
        return self.email
