from django.shortcuts import render
# Code from Code Institute Boutique Ado Walksthrough


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)
