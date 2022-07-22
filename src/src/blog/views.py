from multiprocessing import context
from django.shortcuts import render
from .models import post
"""
posts = [ # c'est des exemples des enregistrements
    {
        'title': 'first blog',
        'content': 'le contenu test',
        'author': 'bilalbelli'
    },
    {
        'title': 'second blog',
        'content': 'le contenu test',
        'author': 'bilalbelli'
    },
    {
        'title': 'third blog',
        'content': 'le contenu test',
        'author': 'bilalbelli'
    }
]
"""
# Create your views here.
def home(request):
    context = { #c'est l'enregistrement de la page
        'title': 'home page',
        'posts': post.objects.all()#to import from database
        #'posts': posts to import from static
    }
    return render(request ,'blog\index.html', context)

def about(request):
    return render(request ,'blog/about.html')
