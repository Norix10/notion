from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from notes.services.note import note_create, note_delete
from notes.selectors.note import get_notes, all_notes, get_note
from django.http import HttpResponse
from django.urls import reverse
import json

# Create your views here.

def work_page_view(request):
    notes = all_notes()
    context = {
        "notes": notes
    }
    return render(request, 'notes/work-page.html' , context)

@csrf_protect
def create_note_view(request):
    name = request.POST.get("name")
    body = request.POST.get("body")

    note_create(name, body)

    return redirect(reverse('work-page'))

@csrf_protect
def delete_note_view(request):
    ids = list(map(int, json.loads(request.body)))
    print(ids)
    notes = get_notes(ids)
    for note in notes:
        note_delete(note.id)
    return redirect(reverse('work-page'))

@csrf_protect
def view_note_view(request, id):
    if request.method == "POST":
        note = get_note(id) 
        body = request.POST.get("body")
        note.body = body
        note.save()

    context = {
        "note": get_note(id),
        "notes": all_notes()
    }
    
    return render(request, 'notes/note-view.html' , context)
