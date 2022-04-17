"""
    Contain the questions and answer
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from .question import Question
from .response import QResponse


class Answer(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name=_("Question"),
        related_name="answers")
    response = models.ForeignKey(
        QResponse,
        on_delete=models.CASCADE,
        verbose_name=_("Response"),
        related_name="answers")
    created_at = models.DateTimeField(
        _("Creation date"),
        auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Update date"),
        auto_now=True)
    answer = models.TextField(
        _("Answer"),
        blank=True,
        null=True)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):
        return "{} : {}".format(self.question, self.answer)
