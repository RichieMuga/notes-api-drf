from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication


class NoteListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # This method is responsible for returning the queryset that the view will use to fetch objects from the database.
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)

class NoteRetriveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.filter()
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)


class NoteRetrieveDestroy(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)
