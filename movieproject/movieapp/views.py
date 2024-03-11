from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Movie
from.forms import Movieform
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
class Movielistview(ListView):
    model=Movie
    template_name='index.html'
    context_object_name='m'

class Movieeditview(UpdateView):
    model=Movie
    template_name='update.html'
    context_object_name='m'
    fields=('name','des','year','img')
    def get_success_url(self):
        return reverse_lazy('index',kwarg={'pk':self.objects.id})



# Create your views here.
def index(request):
    return render(request,'index.html',{'m':Movie.objects.all()})

def movie(request,movie_id):
    obj={'a':Movie.objects.get(id=movie_id)}
    return render(request,'movie.html',obj)

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        des=request.POST.get('des')
        year=request.POST.get('year')
        img=request.FILES['img']
        a=Movie(name=name,year=year,img=img,des=des)
        a.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'movie':movie,'form':form})



def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')