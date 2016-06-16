import unittest
import Notesapplication


class Notesapplicationtest(unittest.TestCase):
	"""Testing notesapplication
	"""

	@classmethod
	def setUpClass(cls):
		cls._myNotes = Notesapplication.NotesApplication("Jane")

	def test_notes_class_instantiated(self):
		self.assertIsInstance(self._myNotes, Notesapplication.NotesApplication)

	def test_note1_create_note(self):
		self.assertEqual(self._myNotes.create("note one"), ["note one"])

	def test_note1_list1_note(self):
		self.assertEqual(self._myNotes.list(), "Note ID: %d \n%s\n\nBy Author %s\n\n" % (0, "note one", "Jane"))

	def test_note1_get_note(self):
		self.assertEqual(self._myNotes.get(0), "note one")

	def test_note1_search_note(self):
		self.assertIn("note", self._myNotes.search("note"))

	def test_note1_list2_note(self):
		self.assertEqual(self._myNotes.edit(0, "note one b"), "note one b")

	def test_note2_create_note(self):
		self.assertEqual(self._myNotes.create("note two"), ["note one b", "note two"])

	def test_note2_list1_note(self):
		self.assertEqual(self._myNotes.list(), "Note ID: %d \n%s\n\nBy Author %s\n\nNote ID: %d \n%s\n\nBy Author %s\n\n" % (0, "note one b", "Jane", 1, "note two", "Jane"))

	def test_note2_get_note(self):
		self.assertEqual(self._myNotes.get(1), "note two")

	def test_note2_search_note(self):
		self.assertIn("note two", self._myNotes.search("two"))

	def test_note2_list2_note(self):
		self.assertEqual(self._myNotes.edit(1, "note two b"), "note two b")

	def test_note2_search_note(self):
		self.assertIn("Showing results for search 'o'\n\nNote ID: 0 \nnote one b\n\nBy Author Jane\n\nNote ID: 1 \nnote two b\n\nBy Author Jane\n\n", self._myNotes.search("o"))

	def test_note3_list1_note(self):
		self.assertEqual(self._myNotes.list(), "Note ID: %d \n%s\n\nBy Author %s\n\nNote ID: %d \n%s\n\nBy Author %s\n\n" % (0, "note one b", "Jane", 1, "note two b", "Jane"))


if __name__ == '__main__':
	unittest.main()