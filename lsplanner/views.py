from django.shortcuts import render, HttpResponse
from .models import User
# Create your views here.
def home(request):
    return render(request, "home.html", {"name": "LSP"})

def users(request):
    data = User.objects.all()
    return render(request, "users.html", {"users": data})
