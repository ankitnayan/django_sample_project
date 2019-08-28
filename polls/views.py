from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):
    print("I am inside polls index")
    return HttpResponse("Hello, world. You're at the polls index.")

