from django.shortcuts import render


def home(request):
   """
   A view to display the home page
   """
   return render(request, 'home/home.html')


