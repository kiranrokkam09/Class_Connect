from django import views
from django.db.models.query_utils import select_related_descend
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from classroom.models import ClassRoom,RoomStream, Comment,ClassFiles,Attendance
from profiles.models import Teacher, Student,User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def files(request,id):
    room = get_object_or_404(ClassFiles, id=id)
    files = room.class_files
    context ={'room':room,'s':files}
    return render(request,"class/files.html",context)
def attendance(request,id):
    room = get_object_or_404(ClassRoom, id=id)
    students = room.student.all().order_by('name')
    context ={'room':room,
              's' :students}
    return render(request,"class/attendance.html",context)
def save(request,id):
    room = get_object_or_404(ClassRoom, id=id)
    for i, s in enumerate(room.student.all()):
        status=request.POST.get(s.name,False)
        date=request.POST.get('date')
        sat=Attendance(classname=room.name,Student=s.name,date=date,Status=status)
        sat.save()
    return render(request,"class/attendance.html",{'room':room,
                                                   's':room.student.all().order_by('name')})
def getattendance(request,id,username):
    room = get_object_or_404(ClassRoom, id=id)
    students = room.student.all().order_by('name')
    filter=Attendance.objects.filter(classname=room.name,Student=username)
    return render(request,"class/studentatt.html",{'room':room,
                                                    's' :students,
                                                    'names':filter})
    
