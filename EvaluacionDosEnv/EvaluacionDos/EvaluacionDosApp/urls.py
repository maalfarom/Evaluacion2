from django.conf.urls import include, url
from . import views
from EvaluacionDosApp.views import index, \
    AutoList

urlpatterns = [
    url(r'^$', AutoList.as_view() ),
]
