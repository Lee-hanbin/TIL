from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dtl(request):
    # name = 'jun'
    # age = 20
    context = {
        'name' : 'ABCDEFGH',
        'age' : 20,
        'foods' : ['apple', 'grape']
    }
    return render(request, 'dtl.html', context)

def dtl2(request):
    # name = 'jun'
    # age = 20
    context = {
        'name' : 'ABCDEFGH',
        'age' : 20,
        'foods' : ['apple', 'grape']
    }
    return render(request, 'dtl2.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):                         
    # print(request.GET.get('search'))
    value = request.GET.get('search')
    name = 'jun'
    context = {
        'value' : value,
        'name' : name,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html',context)