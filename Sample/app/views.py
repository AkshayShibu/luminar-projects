from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View 
from app.forms import Student_Form
from app.models import Students
# from app.forms import Employee_Form

class Student_Add_View(View):
    def get(self,request,*args,**kwargs):
        form=Student_Form()
        return render(request,'student_add.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=Student_Form(request.POST)
        if form.is_valid():
            form.save()
            form=Student_Form()
            # Students.objects.create(**form.cleaned_data)
            return render(request,'student_add.html',{'form':form})
            


# class Employee_Add_View(View):
#     def get(self,request,*args,**kwargs):
#         form=Employee_Form()
#         return render(request,'employee_add.html',{'form':form})
#     def post(self,request,*args,**kwargs):
#         form=Employee_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             form=Employee_Form()
#             return render(request,'employee_add.html',{'form':form})

class Home(View):
    def get(self,request,*args,**kwargs):
        a='hai'
        return render(request,"index.html",{'a':a})
    
class Student_List_View(View):
    def get(self,request,*args,**kwargs):
        data=Students.objects.all()
        return render(request,'student_all.html',{'data':data})
    
class Student_Update_View(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        data=Students.objects.get(id=id)
        form=Student_Form(instance=data)
        return render(request,'student_add.html',{'form':form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        data=Students.objects.get(id=id)
        form=Student_Form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('all')
        else:
            return render(request,'student_add.html',{'form':form})
        
class Student_Delete_View(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Students.objects.get(id=id).delete()
        return redirect('all')
