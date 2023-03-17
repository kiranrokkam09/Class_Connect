from django import views
from django.db.models.query_utils import select_related_descend
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from classroom.models import ClassRoom,RoomStream, Comment
from profiles.models import Teacher, Student
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def files(request,id):
    dic ={'id':id}
    return render(request,"class/files.html",dic)