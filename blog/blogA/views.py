from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View
from blogA.forms import Content_Form
from blogA.models import Content

class Content_Add_View(View):
    def get(self, request,*args,**kwargs):
        form = Content_Form()
        datas=Content.objects.all()
        return render(request,'content_add.html',{'form':form,'datas':datas})
    def post(self,request,*args,**kwargs):
        datas=Content.objects.all()
        form = Content_Form(request.POST)
        if form.is_valid():
            form.save()
            form= Content_Form()
            return render(request,'content_add.html',{'form':form,'datas':datas})
        
class Content_Update_View(View):
    def get(self, request, *args,**kwargs):
        id=kwargs.get('pk')
        data=Content.objects.get(id=id)
        form=Content_Form(instance=data)
        datas=Content.objects.all()
        return render(request,'content_add.html',{'form':form,'datas':datas})
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        data=Content.objects.get(id=id)
        form=Content_Form(request.POST,instance=data)
        datas=Content.objects.all()
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            return render(request,'content_add.html',{'form':form,'datas':datas})
    

class Content_Delete_View(View):
    def get(self, request, *args,**kwargs):
        id=kwargs.get('pk')
        Content.objects.get(id=id).delete()
        return redirect('add')
