from django.shortcuts import render

# Create your views for conditional statement.
def condition(request):
    d={'a':100}
    return render(request,'condition.html',context=d)

# Create your views for looping statement.
def loop(request):
    d={'name':'Abhisek'}
    return render(request,'loop.html',context=d)