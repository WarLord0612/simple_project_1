from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def count(request):

    para=request.POST.get('quantity')
    l=para.split(' ')
    print(len(l))
    return render(request,'index1.html',{'count':str(len(l))})
    