from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from notes.services.note import note_create, note_delete
from notes.selectors.note import all_notes
from django.http import HttpResponse


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

    return work_page_view(request)

@csrf_protect
def delete_note_view(request):
    notes = all_notes()
    for note in notes:
        note_delete(note.id)
    return HttpResponse(status=201)