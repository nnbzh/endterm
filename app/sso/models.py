from typing import List
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager as BaseUserManger
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class UserManager(BaseUserManger):
    pass


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(
        _("email address"), blank=True, unique=True, null=True
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    phone_number = models.CharField(
        verbose_name=_("Phone number"),
        max_length=13,
        blank=True,
        null=True,
        unique=True,
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    objects = UserManager()

    EMAIL_FIELD: str = "email"
    USERNAME_FIELD: str = "username"
    REQUIRED_FIELDS: List[str] = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        return f"{self.get_username()} - {self.get_full_name()}"


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="profile",
    )

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profile")
