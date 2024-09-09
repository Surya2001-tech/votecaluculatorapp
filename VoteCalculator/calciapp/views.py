from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'calculator.html')


def read_data(request):
    n1 = int(request.POST["txt1"])
    n2 = int(request.POST["txt2"])
    operation = request.POST["operation"]
    # print(n1)
    # print(n2)
    # print(operation)
    if operation =="Add":
        result =n1 + n2
    elif operation=="Sub":
        result = n1 - n2
    elif operation=="Mul" :
        result = n1 * n2
    else:
        try:
           result=n1/n2
        except:
            result="second number is 0 please change"

    return render(request, 'calculator.html',{"n1":n1,"n2":n2,"res":result})

