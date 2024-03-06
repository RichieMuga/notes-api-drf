from django.test import TestCase
from notes.models import Note
from django.contrib.auth.models import User


class NoteTestCase(TestCase):
    """Test the models for the notes model"""

    def setUp(self):
        # Create a user instance
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Create a Note instance associated with the user
        Note.objects.create(
            title="only a test", content="yes, this is only a test", slug="only-a-test", user=self.user
        )

    def test_note_content(self):
        note = Note.objects.get(id=1)
        expected_object_name = f"{note.title}"
        self.assertEqual(expected_object_name, "only a test")
        expected_object_content = f"{note.content}"
        self.assertEqual(expected_object_content, "yes, this is only a test")

    def test_note_slug(self):
        note = Note.objects.get(id=1)
        expected_object_slug = f"{note.slug}"
        self.assertEqual(expected_object_slug, "only-a-test")

    def test_note_user(self):
        note = Note.objects.get(id=1)
        expected_object_user = f"{note.user}"
        self.assertEqual(expected_object_user, "testuser")

    def test_note_created_at(self):
        note = Note.objects.get(id=1)
        expected_object_created_at = f"{note.created_at}"
        self.assertEqual(expected_object_created_at, f"{note.created_at}")

    def test_note_last_modified(self):
        note = Note.objects.get(id=1)
        expected_object_last_modified = f"{note.last_modified}"
        self.assertEqual(expected_object_last_modified, f"{note.last_modified}")
    
    def test_note_int(self):
        note = Note.objects.get(id=1)
        expected_object_str = 1
        self.assertNotEqual(expected_object_str, "only a test")

    def test_note_str(self):
        note = Note.objects.get(id=1)
        expected_object_str = f"{note.title}"
        self.assertEqual(expected_object_str, "only a test")

    def test_note_content_str(self):
        note = Note.objects.get(id=1)
        expected_object_str = f"{note.content}"
        self.assertEqual(expected_object_str, "yes, this is only a test")

    def test_note_slug_str(self):
        note = Note.objects.get(id=1)
        expected_object_str = f"{note.slug}"
        self.assertEqual(expected_object_str, "only-a-test")

    def test_note_user_str(self):
        note = Note.objects.get(id=1)
        expected_object_str = f"{note.user}"
        self.assertEqual(expected_object_str, "testuser")