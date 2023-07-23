from django.shortcuts import render

# Create your views here.

def work_page_view(request):
    return render(request, 'notes/work-page.html')