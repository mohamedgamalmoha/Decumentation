from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Topic, Section


class TopicInlineAdmin(admin.TabularInline):
    model = Topic
    extra = 0
    min_num = 0
    can_delete = True
    verbose_name = _('Subtopic')
    verbose_name_plural = _('Subtopics')
    readonly_fields = ('created', 'updated')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    inlines = (TopicInlineAdmin, )
    queryset = Topic.objects.main_topics()

    def get_queryset(self, *args, **kwargs):
        return self.queryset


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'active', 'created', 'updated')
    readonly_fields = ('created', 'updated')


admin.site.register(Topic, TopicAdmin)
admin.site.register(Section, SectionAdmin)
