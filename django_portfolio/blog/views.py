from django.shortcuts import render
from django.http import HttpResponse

dummyPosts = [
    {
        'author': 'Niall Kelly',
        'title': 'The Subtle Art of Pooping Inconspicuously',
        'content': 'Be as loud as humanly possible',
        'date_posted': 'tommorow'
    },

        {
        'author': 'Niall Smelly',
        'title': 'The Inconspicuous Art of Pooping Subtly',
        'content': 'Get a litteral helping hand',
        'date_posted': 'sure..'
    }

]

# Create your views here
# views: functions called when specific url entered,
# returns html to display or exception
def home(request):
    context = {
        'posts': dummyPosts
    }
    # give name of template file to render
    # render retrieves from this file
    # can pass context (extra data)
    # e.g post data
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})