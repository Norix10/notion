from notes.models import Note

def all_notes():
    return Note.objects.all()

def get_notes(ids):
    return Note.objects.filter(id__in = ids)

def get_note(id):
    return Note.objects.get(id = id)
