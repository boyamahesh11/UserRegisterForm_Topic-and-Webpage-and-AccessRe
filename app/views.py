from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def Registration(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessRecordForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessRecordForm(request.POST)
        if tfd.is_valid() and  wfd.is_valid() and afd.is_valid():
            nsto=tfd.save(commit=False)
            nsto.save()
            nswo=wfd.save(commit=False)
            nswo.topic_name=nsto
            nswo.save()
            nsao=afd.save(commit=False)
            nsao.name=nswo
            nsao.save()


            return HttpResponse('registered sucessfully')
        else:
            return HttpResponse('Not valid')





    return render(request,'Registration.html',d)
