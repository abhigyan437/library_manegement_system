from rest_framework import viewsets,filters
from .serializers import BookSerializers,MemberSerializer
from .models import Books,Members
from django.shortcuts import render, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
#from .serializers import userSerializers
from django.contrib.auth.models import User


def book_view(request):
    books = Books.objects.all().values()
    print('BBBBBBBBBB - ',books)
    return render(request,'1.html',{'book':books})


def index(request):
    books = Books.objects.all().values()
    return render(request,'1.html',{'book':books})

def delete_account(request):
    return render(request,'delete.html')

def deleting(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        mem = Members.objects.get(name = name)
        mem.delete()
    return redirect('home')


def booking(request,book_name):
    value = Books.objects.get(book_name = book_name)
    value.available_status = False
    value.save()
    return redirect('index')

def returning(request,book_name):
    value = Books.objects.get(book_name = book_name)
    value.available_status = True
    value.save()
    return redirect('index')

def home(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            mem = Members.objects.filter(name = name).values()
            if mem[0]['password'] == password:
                return redirect('index')
            else:
                return render(request, 'error_login.html')
        except:
            return render(request, 'error_login.html')
    else:
        return render(request,'error_login.html')


def register(request):
    return render(request,'register.html')

def registering(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        a = Members(name = name,password = password)
        a.save()
        return redirect('index')

def register_login(request):
    return redirect('login')

class BooksViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all().order_by('book_name')
    serializer_class = BookSerializers

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all().order_by('name')
    serializer_class = MemberSerializer
