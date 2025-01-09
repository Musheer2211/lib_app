from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,JsonResponse
from models import Users,Books
import json

# Create your views here.
def home_page(request : HttpRequest):
    username = request.COOKIES.get('user','')
    if username and Users.objects.filter(username=username).exists():
        password = request.COOKIES.get('password','')
        if password and Users.objects.filter(username = username).password == password:
            return redirect('books')
        else:
            return redirect('login')
    else:
        return redirect('login')

def log_in(request : HttpRequest):
    return HttpResponse('log_in')
    
def user_logged_in(request : HttpRequest,username):
    all_books = Books.objects.filter(username = username)
    print(all_books)
    return HttpResponse('books')

def add_books(request):
    try:
        data = json.loads(request.body)
        user = data.get('username','')
        book = data.get('book','')
        try:
            pages = int(data.get('pages' , ''))
            pages_read = int(data.get('pages_read' , ''))
            new_book = Books(username = user , book_name = book,pages_total = pages,pages_read = pages_read)
            new_book.save()
        except ValueError:
            print('value error')
        
    except json.JSONDecodeError:
        print(';(')

    