from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"votevalidation.html")


def read_data(request):
 try:
    age=int(request.POST["txtage"])
    if age >=18:
        result="YOUR ELIGIBLE FOR CAST YOUR VOTE"
    elif age>0 and age <18:
        result="YOUR NOT ELIGIBLE FOR CAST YOUR VOTE"
    else:
        result="PLEASE GIVE PROPER AGE"

    return render(request,'votevalidation.html',{'age':age,'res':result})
 except:
    result="PLEASE GIVE PROPER AGE"
    return render(request, 'votevalidation.html', { 'res': result})