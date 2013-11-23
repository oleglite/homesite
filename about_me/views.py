from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'about_me/home.html', {
        'page_title': 'About Me',
    })