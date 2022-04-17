from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class Profile(models.Model):
    """
        Base Abstract Profile Model
        Works as abstract class for any user like merchant and ....
    """

    class Meta:
        abstract = True

    user = models.OneToOneField(
        User,
        null=False,
        blank=False,
        related_name="%(app_label)s_%(class)s_related",
        on_delete=models.CASCADE)
    failed_attempts = models.IntegerField(
        _("Failed Attempts"),
        null=False, 
        default=0)
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now=False,
        auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return '{}:{}'.format(self.id, 
                              self.user.username)
