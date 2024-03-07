from django.test import TestCase
from notes.models import Note
from django.contrib.auth.models import User


class NoteSerializersTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.note = Note.objects.create(
            title="only a test", content="yes, this is only a test", slug="only-a-test", user=self.user
        )

    def test_slug_serialization(self):
        note = Note.objects.get(id=1)
        expected_object_slug = f"{note.slug}"
        self.assertEqual(expected_object_slug, "only-a-test")
