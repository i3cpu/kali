from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='main'),
    path('about', views.about,name='about'),
    path('installation', views.installation,name='installation'),
    path('download', views.download,name='download'),
    path('cantact', views.cantact,name='cantact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
