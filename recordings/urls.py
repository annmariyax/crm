from django.urls import path

from . import views

urlpatterns=[
   
    path('recordings/',views.RecordingsView.as_view(),name='recordings')
]