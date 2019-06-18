from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
# from .models import User,Exam,News,Board
from django.template import loader
from django.views import generic
from django.urls import reverse
# from .forms import AddNewsForm,AddExamForm,AddBoard
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')
