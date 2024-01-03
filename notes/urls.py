from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='notes_list'),
    path('notes/create/', views.NoteCreate.as_view(), name='notes_create'),
    path('notes/<slug:slug>/', views.NoteRetrieve.as_view(), name='notes_retrieve'),
    path('notes/<slug:slug>/update/', views.NoteUpdate.as_view(), name='notes_update'),
    
]