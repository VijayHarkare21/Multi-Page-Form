from django.contrib import messages
from django.shortcuts import render
from django.http import *
from django.urls import *

from multistep_form.models import MultiStepForm

# Create your views here.
def multistepform(request):
    return render(request, "multistepform.html")

def multistepform_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("multistepform"))
    else:
        email = request.POST.get("email")
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        cpwd = request.POST.get("cpwd")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phno = request.POST.get("phno")
        phno_2 = request.POST.get("phno_2")
        photo = request.POST.get("photo")
        sign = request.POST.get("sign")
        if pwd!=cpwd:
            messages.error(request,"Confirm Password Doesn't Match!")
            return HttpResponseRedirect(reverse('multistepform'))
        try:    
            multistepform = MultiStepForm(email=email, uname=uname, pwd=pwd, fname=fname, lname=lname, phno=phno, phno_2=phno_2, photo=photo, sign=sign)
            multistepform.save()
            messages.success(request,"Data Saved Successfully!")
            return render(request, 'success.html')
        except:
            messages.error(request,"Error in Saving Data!")
            return HttpResponseRedirect(reverse('multistepform'))
