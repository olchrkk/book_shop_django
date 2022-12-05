from django.urls import path, include
from django.urls import path, include
from .views import IndexView


urlpatterns = [
    path('registration/', IndexView.as_view(), name='registration')
]
