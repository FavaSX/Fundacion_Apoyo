from django.urls import path
from .views import home, registror
urlpatterns = [
    path('', home, name="home"),
    path('registror/', registror, name='registror')
]
