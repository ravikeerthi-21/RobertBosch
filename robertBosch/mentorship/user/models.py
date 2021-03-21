import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):
    '''
    creating a manager for a custom user model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
    '''
    def create_user(self, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "login"


class Query(models.Model):
    query = models.CharField(max_length=250, primary_key=True)
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True, editable=False)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="query_submitter", on_delete=models.CASCADE)
    assignedTo = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="query_assignedTo", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.query[:20], self.submitter


class Replies(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    reply = models.CharField(max_length=1000)
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    last_replied_on = models.DateTimeField(auto_now_add=True, editable=False)
    repliedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.query[:20], self.reply[:20], self.repliedBy

