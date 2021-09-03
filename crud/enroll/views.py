from django.core import validators
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentsRegistations
from .models import User

# Create your views here.


# this function will add user and shows user
def add_show(request):
    if request.method == 'POST':
        fm = StudentsRegistations(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['firstname']
            nm = fm.cleaned_data['lastname']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            if User.objects.filter(firstname=fn):
               msg="firstname already exist!!"
               stud=User.objects.all()
               return render(request,"enroll/addandshow.html",{'form':fm,'stu':stud,'msg':msg})
            else:
                if User.objects.filter(lastname=nm):
                   msg="lastname already exist!!"
                   stud = User.objects.all()
                   return render(request,"enroll/addandshow.html",{'form':fm,'stu':stud,'msg':msg})
                else:
                     if User.objects.filter(email=em):
                        msg="email already exist!!"
                        stud = User.objects.all()
                        return render(request,"enroll/addandshow.html",{'form':fm,'stu':stud,'msg':msg})
                     else:
                         reg = User(firstname=fn,lastname=nm,email=em,password=pw)
                         reg.save()
                         fm = StudentsRegistations()
                         msg="successfully add"
                         stud=User.objects.all()
    else:
        fm = StudentsRegistations()
    stud = User.objects.all()
    return render(request,"enroll/addandshow.html",{'form':fm,'stu':stud})








# this function update/edit user
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentsRegistations(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentsRegistations(instance=pi)
    return render(request,"enroll/updatestudents.html",{'form':fm})


# this  function delete user 
def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')