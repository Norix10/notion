from notes.models import Note

def note_create(name, body):
    return Note.objects.create(name = name, body = body)

def note_delete(note_id): 
    Note.objects.get(id = note_id).delete()