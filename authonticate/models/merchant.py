from django.utils.translation import ugettext_lazy as _
from django.db import models

from .profile import Profile


class Merchant(Profile):
    
    MERCHANT_STATUS=(
        (0, 'in_progress'),
        (1, 'live')
    )
    
    active_merchant = models.BooleanField(
        _("Is Active"),
        null=False,
        blank=False,
        default=True)
    created_at = models.DateTimeField(
        _("Created at"),
        null=False,
        blank=False,
        auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Created at"),
        blank=True,
        null=True,
        auto_now=True)
    merchant_status = models.IntegerField(
        _("Merchant Status"),
        choices=MERCHANT_STATUS, 
        default=0, 
        help_text="This represents the merchant's onboarding status.")
    national_id = models.CharField(
        _("National ID"),
        max_length=16, 
        blank=True, 
        null=True)
    city = models.CharField(
        _("City"),
        max_length=200,
        blank=True,
        null=True)
    address = models.CharField(
        _("Address"),
        max_length=200,
        blank=True,
        null=True)
    
    def __str__(self):
        return self.user.username

    @property
    def is_live(self):
        return True if self.merchant_status == 1 else False
