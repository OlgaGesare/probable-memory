class NotesApplication(object):
  def __init__ (self, name):
    self.name = name
    self.notes = []

  def create (self, note_content):
    self.notes.append(note_content)
    return self.notes

  def list (self):
    note_id = 0
    note_content = ""
    for x in self.notes:
      note_content += ("Note ID: %d \n%s\n\nBy Author %s\n\n" % (note_id, x, self.name))
      note_id += 1
    return note_content 

  def get (self,note_id):
    return self.notes[note_id]

  def search (self,search_text):
    search_result = ("Showing results for search '%s'\n\n" % (search_text))
    noteid = 0
    for note in self.notes:
      if search_text in note:
        search_result += ("Note ID: %d \n%s\n\nBy Author %s\n\n" % (noteid, note, self.name))
      noteid += 1
    return search_result

  def edit (self, note_id, edit_text):
    self.notes[note_id] = edit_text
    return self.notes[note_id]