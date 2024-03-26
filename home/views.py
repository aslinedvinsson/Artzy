from django.shortcuts import render

# Code from Code Institute Boutique Ado Walksthrough

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')