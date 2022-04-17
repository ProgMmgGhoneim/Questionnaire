"""
    Main model that represent Question and Choice
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .category import Category
from .questionnaire import Questionnaire


def validate_choices(choices):
    """Verifies that there is at least two choices in choices
    :param String choices: The string representing the user choices.
    """
    values = choices.split(',')
    empty = 0
    for value in values:
        if value.replace(" ", "") == "":
            empty += 1
    if len(values) < 2 + empty:
        msg = "The selected field requires an associated list of choices."
        msg += " Choices must contain more than one item."
        raise ValidationError(msg)


class Question(models.Model):

    TEXT = "text"
    SELECT = "select"

    QUESTION_TYPES = (
        (TEXT, _("text")),
        (SELECT, _("select")),
    )

    text = models.TextField(
        _("Text"),
        null=False,
        blank=False,
    )
    required = models.BooleanField(
        _("Required"),
        default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name=_("Category"),
        blank=True,
        null=True,
        related_name="Categorys"
    )
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Questionnaire"),
        related_name="questions")
    type = models.CharField(
        _("Type"),
        max_length=200,
        choices=QUESTION_TYPES,
        default=TEXT)
    choices = models.TextField(
        _("Choices"),
        blank=True,
        null=True,
        help_text="This Field is required only when type is select")
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Update date"),
        auto_now=True)

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if self.type == Question.SELECT:
            validate_choices(self.choices)
        super().save(*args, **kwargs)

    def get_clean_choices(self):
        """Return split and stripped list of choices with no null values."""
        if self.choices is None:
            return []
        choices_list = []
        for choice in self.choices.split(settings.CHOICES_SEPARATOR):
            choice = choice.strip()
            if choice:
                choices_list.append(choice)
        return choices_list
