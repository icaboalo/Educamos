from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core import validators
from django.db import models
from django.utils import timezone
from school.models import Classroom


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    username = models.CharField(max_length=30, unique=True,
                                help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                validators=[validators.RegexValidator(r'^[\w.@+-]+$', (
                                    'Enter a valid username. This value may contain only '
                                    'letters, numbers ' 'and @/./+/-/_ characters.')), ],
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                },
                                )

    full_name = models.CharField('full name', max_length=50, blank=False)
    email = models.EmailField()
    is_professor = models.BooleanField('professor status', default=False)
    classroom = models.ForeignKey(Classroom, blank=True, null=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        pass

    def get_full_name(self):
        return self.full_name
