from notes.models import Note

def all_notes():
    return Note.objects.all()