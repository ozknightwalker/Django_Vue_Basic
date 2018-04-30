from __future__ import unicode_literals

from django.urls import path

from .views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
]
