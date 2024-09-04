from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152102',
        'name': 'Janssen Benedict',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
