from django import views
from django.urls import path
from .views.room import ViewClassRoom,SingleClass,CreateClassRoom,JoinRoom, LeaveClass, SendMail
from .views.people import PeopleUnderRoom
from .views.stream import CreateStream, CreateComment
from . import myviews

urlpatterns =[
    path('',ViewClassRoom.as_view(),name='all_class'),
    path('view/<str:id>/',SingleClass.as_view(), name='single'),
    path('create/',CreateClassRoom.as_view(),name='create_class'),
    path('join/class/',JoinRoom.as_view(),name='join'),

    path('<str:id>/people/', PeopleUnderRoom.as_view(),name='people'),
    path('<str:id>/leave/', LeaveClass.as_view(), name='leave'),

    path('<str:id>/create/stream',CreateStream.as_view(),name='stream_create'),
    #path('stream/<str:id>/view/',SingleStream.as_view(),name='single_stream'),

    path('<str:id>/create/comment', CreateComment.as_view(),name='comment_create'),
    path('<str:id>/create/files/',myviews.files,name='files'),
    path('<str:id>/create/attendance/',myviews.attendance,name='attendance'),
    path('view/<str:id>/<str:username>/create/attendance/student',myviews.getattendance,name='getattendance'),
    path('view/<str:id>/create/attendance/added',myviews.added,name='added'),
    path('<str:id>/create/save/',myviews.save,name='save'),
    #send email route
    path('send/code/via/mail',SendMail.as_view(),name='send'),
]