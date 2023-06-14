from django.shortcuts import render


def count(request):

    para=request.POST.get('para')
    l=para.split(' ')
    return render(request,'index1.html',{'count':len(l)})
    