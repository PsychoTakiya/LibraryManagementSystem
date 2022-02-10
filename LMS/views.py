from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html');

def booksDisplay(request):
    return render(request,'booksdisplay.html')