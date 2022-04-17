"""
    Category of question
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(
        _("Name"),
        max_length=400,
        null=False,
        blank=False)
    description = models.CharField(
        _("Description"),
        max_length=2000,
        blank=True,
        null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name
