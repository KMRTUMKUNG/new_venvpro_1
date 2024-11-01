from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import person

# Create your views here.
def index(request):
    all_person = person.objects.all()
    return render(request,"index.html",{"all_person" : all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = request.POST["age"]
        Phone = request.POST["phone"]
        mail = request.POST["email"]
        
        
        #บันทึกข้อมูล
        person.objects.create(
            name =name,
            lastname = lastname,
            age =age,
            Phone = Phone,
            mail = mail

        )
      


        return redirect ("/")
    else :
        return render(request,"form.html")