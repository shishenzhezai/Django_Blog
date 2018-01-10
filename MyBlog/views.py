from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Sys_User, Forum_Questions, Tags


# Create your views here.
class IndexView(generic.ListView):
    template_name = "MyBlog/index.html"
    context_object_name = ""

    def get_queryset(self):
        return HttpResponseRedirect("Hello")
