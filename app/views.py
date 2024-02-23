from django.shortcuts import render,HttpResponse

# Create your views here.
from app.forms import empform
from app.models import emp
#                                             functions based views


def insert(request):
    if request.method=='GET':
        var=empform()
        return render(request,'sam.html',{'var':var})
    
    elif request.method=='POST':
        v=empform(request.POST)
        if v.is_valid():
            v.save()
            return HttpResponse('data stored in a table')
        

def read(request):
    var=emp.objects.all()  #get,filter
    return render(request,'read.html',{'var':var})

def up(request,pk):
    a=emp.objects.get(id=pk)
    if request.method=='GET':
        var=empform(instance=a)
        return render(request,'sam.html',{'var':var})
    
    elif request.method=='POST':
        v=empform(request.POST,instance=a)
        if v.is_valid():
            v.save()
            return HttpResponse('data updated in a table')
        

def delete(request,pk):
    emp.objects.filter(id=pk).delete()
    return HttpResponse('data deleted from the table')




#                                              class based views

from django.views import View

class ins(View):
    def get(self,request):
        var=empform()
        return render(request,'sam.html',{'var':var})
    def post(self,request):
        v=empform(request.POST)
        if v.is_valid():
            v.save()
            return HttpResponse('data stored in a table')
        
class rd(View):
    def get(self,request):
        var=emp.objects.all()   #get,filter
        return render(request,'read.html',{'var':var})
    
class upp(View):
    def get(self,request,pk):
        a=emp.objects.get(id=pk)
        var=empform(instance=a)
        return render(request,'sam.html',{'var':var})
    
    def post(self,request,pk):
        a=emp.objects.get(id=pk)
        v=empform(request.POST,instance=a)
        if v.is_valid():
            v.save()
            return HttpResponse('data updated in a table')
        
class d(View):
    def get(self,requesr,pk):
        emp.objects.filter(id=pk).delete()
        return HttpResponse('data deleted from the table')




        



