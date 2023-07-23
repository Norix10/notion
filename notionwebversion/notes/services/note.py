from notes.models import Note

def note_create(name, body):
    return Note.objects.create(name = name, body = body)
    