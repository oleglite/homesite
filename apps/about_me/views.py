from django.shortcuts import render
from apps.about_me.models import PersonalInfo

# Create your views here.
def about_me(request):
    person = PersonalInfo.objects.all()[0]
    return render(request, 'about_me/about_page.html', {
        'person': person,
        'page_title': 'About Me',
        'request': request,
    })


def contacts(request):
    person = PersonalInfo.objects.all()[0]
    return render(request, 'about_me/contacts_page.html', {
        'person': person,
        'page_title': 'Contacts',
        'request': request,
    })