from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^statics',views.index,name='index')
]