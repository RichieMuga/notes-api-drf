from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer
from .mixins import UserFilterMixin

class NoteListCreate(UserFilterMixin,generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteRetriveUpdate(UserFilterMixin,generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.filter()
    serializer_class = NoteSerializer


class NoteRetrieveDestroy(UserFilterMixin,generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
