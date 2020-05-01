from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=40,
        unique=True,
        help_text=_('Required. 40 characters or fewer. Letter, digits and @/./+/-/_ only'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists"),
        },
    )
    first_name = None
    last_name = None
    full_name = models.CharField(_('full name'), max_length=255, blank=True)
    email = models.EmailField(_('email address'), unique=True)

    avatar = models.URLField(blank=True, max_length=1000)

    address = models.CharField(_('address'), max_length=500, blank=True)
    year_birth = models.PositiveSmallIntegerField(null=True, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.username

