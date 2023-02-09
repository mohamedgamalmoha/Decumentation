from django.views.generic.detail import DetailView

from .models import Topic


class TopicsView(DetailView):
    model = Topic
    queryset = Topic.objects.available_main_topics()
    context_object_name = 'current_topic'
    template_name = 'docs/docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_topics'] = self.get_queryset()
        return context
