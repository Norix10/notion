from django.shortcuts import render

# Create your views here.
def welocome_view(request):
    return render(request, 'welcome/view.html')
