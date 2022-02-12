from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from LMS.models import Books, Readers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm , User
from django.contrib.auth import authenticate, login as dj_login, logout


# Create your views here.
def index(request):
    return render(request, 'index.html');

def booksDisplay(request):
    dispBooks = Books.objects.all()
    display = {
        "display_books" : dispBooks
    }

    return render(request,'booksdisplay.html',display)

def booksUpdation(request):
    if request.method == "POST":
        booksName = request.POST.get('booksName')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        print(booksName,author,publisher)
		
        books = Books(booksName=booksName, author=author, publisher = publisher )
        print(booksName,author,publisher)
        books.save()
        return HttpResponseRedirect('updation') #to prevent adding previous records from getting saved
	
    return render(request,'booksupdation.html')

def booksDeletion(request):
    if request.method == "POST":
        delBookName = request.POST.get('booksName')
        delauthor = request.POST.get('author')
        delpublisher = request.POST.get('publisher')
        print(delBookName,delauthor,delpublisher)
        if Books.objects.filter(booksName = delBookName, author = delauthor).exists():
            print("entry present")
            deleteBook = Books.objects.get(booksName = delBookName , author = delauthor)
            deleteBook.delete()
            return HttpResponseRedirect('updation')

			
        else :
            print("not present")

def custUpdation(request):
    if request.method == "POST":
        readersName = request.POST.get('readersName')
        age = request.POST.get('age')
        

        readers = Readers(readersName = readersName, age=age)
        readers.save()
        HttpResponseRedirect('custUpdation')

    return render(request,'customerupdation.html')

def readersDeletion(request):
    if request.method == "POST":
        delreadersName = request.POST.get('readersName')
        delage = request.POST.get('age')
        if Readers.objects.filter(readersName = delreadersName, age = delage).exists():
            print("entry present")
            deleteReader = Readers.objects.get(readersName = delreadersName , age = delage)
            deleteReader.delete()
            return HttpResponseRedirect('custUpdation')
			
        else :
            print("not present")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            dj_login(request, user)
            print("logged in")
            return redirect("home")
        else:
            print("failed")
            return render(request, "login.html")
    print("oops")
    return render(request,'login.html')

def logoutUser(request):
    if request.method == "POST":
        print("logout")
        logout(request)
        return redirect('login')



