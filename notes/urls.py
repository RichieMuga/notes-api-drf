from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteListCreate.as_view(), name='notes_list'),
    path('notes/<int:pk>/', views.NoteRetriveUpdate.as_view(), name='notes_detail'),
    path('notes/<int:pk>/', views.NoteRetrieveDestroy(), name='notes_delete'),
]