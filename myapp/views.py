from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def first(request):
    return render(request, 'first.html')
