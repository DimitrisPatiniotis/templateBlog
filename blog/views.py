from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Mike Arambatzis',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 21, 2020'
    },{
        'author': 'Evelin Kinti',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 2, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')