from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, ArticleSerializer
from tutorial.quickstart.models import Article
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse

def loginUser(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    print request.POST
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'index.html')
            # return reverse('index')
        else:
            return render(request, 'login.html', {'errmsg': 'disabled account'})
            # Return a 'disabled account' error message
    else:
        return render(request, 'login.html', {'errmsg': 'invalid login'})

def userList(request):
    if request.method == 'GET':
        return render(request, 'user-list.html')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def articleList(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'article-list.html', {'articles': articles})

def articleAdd(request):
    if request.method == 'GET':
        return render(request, 'article-add.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
