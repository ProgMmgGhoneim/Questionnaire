"""
    Merchant bussiness plane.
    Each merchant have one or many bussiness plan
    bussiness plan and name are uniwue together
"""
import jwt
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from authonticate.models.merchant import Merchant


class BussinessPlan(models.Model):

    name = models.CharField(
        _("Name"),
        max_length=36,
        null=True,
        blank=True)
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        verbose_name=_("Merchant"))
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Update date"),
        auto_now=True)
    
    class Meta:
        verbose_name = _("Bussiness Plane ")
        verbose_name_plural = _("Bussiness Planes ")
        unique_together = (
            ('name', 'merchant')
        )

    def __str__(self):
        return '{} - {}'.format(self.name, self.merchant)

    def generate_auth_token(self):
        key = settings.API_KEY
        algorthm = settings.API_ALGORTHM
        payload = {
            "name": self.name,
            "merchant_id": self.merchant.id,
            "id": self.id,
            "time": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        }
        token = jwt.encode(payload, key, algorithm=algorthm)
        return token

    @staticmethod
    def from_auth_token(token):
        key = settings.API_KEY
        algorthm = settings.API_ALGORTHM
        data = jwt.decode(token, key, algorithms=algorthm)
        return BussinessPlan.objects.filter(id=data.get('id')).last()