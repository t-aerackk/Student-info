from django.shortcuts import render
from .models import *
from .forms import *

def student(request):
    if request.method=='POST':
        fm=studentForm(request.POST)
        if fm.is_valid():
            fm.save()

    else:
         fm=studentForm()
    return render(request,'enroll/form.html',{'fm':fm})