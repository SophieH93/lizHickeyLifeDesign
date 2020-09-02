from django.shortcuts import render

# Create your views here.

def about_liz(request):

    return render(request, 'about/about_liz.html')
