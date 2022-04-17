"""
    Response represent the user flow with it's questionnaire
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from .questionnaire import Questionnaire
from .bussiness_plan import BussinessPlan


class QResponse(models.Model):

    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        verbose_name=_("Questionnaire"), related_name="responses")
    bussiness_plane = models.ForeignKey(
        BussinessPlan,
        on_delete=models.CASCADE,
        blank=True)

    class Meta:
        verbose_name = _("Questionnaire Respone")
        verbose_name_plural = _("Questionnaire Respones")

    def __str__(self):
        return 'Response: {} - {}'.format(self.questionnaire, self.bussiness_plane)
