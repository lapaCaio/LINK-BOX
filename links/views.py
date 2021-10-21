from django.shortcuts import render
from links.models import Link

def home(request):
    links = Link.objects.exclude(link_ativo=False).order_by('ordem_link')
    return render(request, 'home.html', {'links':links})
