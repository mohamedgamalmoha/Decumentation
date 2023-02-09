from django.urls import path

from .views import TopicsView

app_name = "docs"
urlpatterns = [
    path('<int:pk>/', TopicsView.as_view(), name='topics'),
]
