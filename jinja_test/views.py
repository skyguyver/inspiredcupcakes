from django.shortcuts import render

def index(request):
    return render(request, 'jinja_test/home.html')