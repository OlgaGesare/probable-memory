class NotesApplication(object):
  def __init__ (self, name, notes):
    self.name = name
    self.notes = notes

  def create(self, note_content):
    self.notes.append(note_content)

  def list(self):
    note_id=0
    for x in self.notes:
      print("Notes ID:", note_id)
      print(notes[note_id])
      print("By Author", self.author)
      note_id+=1

  def get(self,note_id):
    return self.note[note_id]

  def search (self,search_text):
    print("Showing results for search '",search_text,"'")
    noteid=0
    for note in self.notes:
      if search_text in note:
        print("Note ID: ", noteid)
        print(note)
        print("By Author ", self.name)
      noteid+=1