from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from notes.models import Note


class TestNoteAPIView(APITestCase):
    """Test notes api views"""

    def setUp(self):
        self.user = User.objects.create_user(username="testcase", password="testcase")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_note(self):
        url = reverse("notes_list")
        data = {"title": "test title", "content": "test content"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Note.objects.count(), 1)

    def test_get_notes(self):
        url = reverse("notes_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_note_detail(self):
        note = Note.objects.create(user=self.user, title="test title", content="test content")
        url = reverse("notes_detail", args=[note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_note_detail(self):
        note = Note.objects.create(user=self.user, title="test title", content="test content")
        url = reverse("notes_detail", args=[note.id])
        data = {"title": "test title", "content": "test content"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.get(id=note.id).title, "test title")

    def test_delete_note_detail(self):
        note = Note.objects.create(user=self.user, title="test title", content="test content")
        url = reverse("notes_delete", args=[note.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Note.objects.count(), 0)
