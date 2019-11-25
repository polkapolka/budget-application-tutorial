from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class BudgetUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must provide an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('Users must provide an email address.')

        user = self.model(email=self.normalize_email(email))
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class BudgetUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BudgetUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin