from django.db import models
from django.utils.translation import gettext_lazy as _


class Questionnaire(models.Model):

    ALL_IN_ONE_PAGE = 0
    BY_QUESTION = 1
    BY_CATEGORY = 2

    DISPLAY_METHOD_CHOICES = [
        (BY_QUESTION, _("By question")),
        (BY_CATEGORY, _("By category")),
        (ALL_IN_ONE_PAGE, _("All in one page")),
    ]

    name = models.CharField(
        _("Name"),
        max_length=400)
    description = models.TextField(_("Description"))
    editable_answers = models.BooleanField(
        _("Users can edit their answers"),
        default=True)
    display_method = models.SmallIntegerField(
        _("Display method"),
        choices=DISPLAY_METHOD_CHOICES, default=ALL_IN_ONE_PAGE
    )

    class Meta:
        verbose_name = _("Questionnaire")
        verbose_name_plural = _("Questionnaires")

    def __str__(self):
        return str(self.name)
