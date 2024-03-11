from . import views
from django.contrib import admin
from django.urls import include, path
app_name='movieapp'
urlpatterns = [
     path('',views.index,name='index'),
     path('movie/<int:movie_id>/',views.movie,name='movie'),
     path('add/',views.add,name='add'),
     path('update/<int:id>/',views.update,name='update'),
     path('delete/<int:id>/',views.delete,name='delete'),
     # path('cbvdelete/<int:id>/',views.delete,name='cbvdelete'),
     # path('cbvedit/<int:id>/',views.delete,name='cbvedit'),
     path('cbvhome',views.Movielistview.as_view(),name='cbvhome'),
     path('cbvedit/<int:pk>',views.Movieeditview.as_view(),name='cbvedit'),
]