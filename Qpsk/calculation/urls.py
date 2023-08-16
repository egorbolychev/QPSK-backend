from .views import *
from django.urls import re_path

urlpatterns = [
    re_path(r'^protocol/$', ProtocolList.as_view()),
    re_path(r'^protocol_params/$', ProtocolParams.as_view()),
    re_path(r'^index/$', Index.as_view()),
    re_path(r'^index/<int:task_id>$', Index.as_view()),
]
