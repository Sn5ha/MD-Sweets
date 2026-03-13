from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
   context={"variable":"Helicopter ride"}
   return render(request,'index.html',context)
   #return HttpResponse("This is Homepage")


def about(request):
    return render(request,"about.html")


def resources(request):
    return render(request,"services.html")


def page1(request):
    return render(request,"contact.html")


def page2(request):
    return HttpResponse("This is Page2")
