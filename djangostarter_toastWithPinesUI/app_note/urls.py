from django.urls import path
from . import views

app_name = 'app_note'

urlpatterns = [
    path('add/', views.add_note_view, name='add_note'),
]
