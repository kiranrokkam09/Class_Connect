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
from classroom.functions import handle_uploaded_file  

def handle_uploaded_file(f):
    with open('media/others/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
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
        stream.save()
        messages.success(request,'The Stream has Been Added'+str(file))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


'''
# SIngle Stream 
class SingleStream(View):
    method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id):
        stream = get_object_or_404(RoomStream, id=id)
        context ={
            'comment':stream.comment_set.all().order_by('-created_at')
        }
        return render(request,'class/single_stream.html', context)
'''

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