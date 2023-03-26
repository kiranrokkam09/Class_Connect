from django import views
from django.db.models.query_utils import select_related_descend
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from classroom.models import ClassRoom,RoomStream, Comment,ClassFiles
from profiles.models import Teacher, Student,User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create Stream
class CreateStream(View):
    method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
        
    def post(self,request,id):
        user = request.user
        room = get_object_or_404(ClassRoom,id=id)
        post = request.POST.get('post')
        file = request.FILES.get('doc')
        stream = RoomStream(user=user,room=room,post=post,file=file)
        files=ClassFiles(room=room,class_files=file)
        lst=[]
        students = room.student.all()
        for i in students:
            lst.append(i)
        if(user.is_teacher):
            send_mail('Assignment Posted',post,'kiran.rokkam09@gmail.com',lst,)
        stream.save()
        files.save()
        messages.success(request,'The Stream has Been Added')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Stream comment Create

class CreateComment(View):   
    method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def post(self,request,id):
        user = request.user
        room = get_object_or_404(RoomStream, id=id)
        comment = request.POST.get('comment')
        comment = Comment(user = user, stream = room, comment=comment)
        comment.save()
        messages.success(request,'Comment Has Been Added')
        # to the same page render
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))