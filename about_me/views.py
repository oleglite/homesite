from django.shortcuts import render
from models import PersonalInfo

# Create your views here.
def home(request):
    person = PersonalInfo.objects.all()[0]
    return render(request, 'about_me/about_page.html', {
        'person': person,
        'page_title': 'About Me',
    })