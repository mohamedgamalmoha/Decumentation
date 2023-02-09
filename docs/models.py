from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class TopicManager(models.Manager):

    def available(self):
        return self.filter(active=True)

    def main_topics(self):
        return self.filter(parent__isnull=True)

    def available_main_topics(self):
        return self.filter(active=True, parent__isnull=True)


class Topic(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='subtopics', on_delete=models.SET_NULL,
                               limit_choices_to=models.Q(parent__isnull=True), verbose_name=_("Related To"))
    title = models.CharField(max_length=250, verbose_name=_("Title"))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    objects = TopicManager()

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")

    def __str__(self):
        return self.title


class SectionManager(models.Manager):

    def available(self):
        return self.filter(active=True)


class Section(models.Model):
    topic = models.ForeignKey(Topic, null=True, blank=False, related_name="sections", on_delete=models.SET_NULL,
                              limit_choices_to=models.Q(parent__isnull=False), verbose_name=_('Topic'))
    title = models.CharField(max_length=250, verbose_name=_("Title"))
    description = RichTextField(null=True, verbose_name=_("Description"))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    objects = TopicManager()

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")

    def __str__(self):
        return self.title
