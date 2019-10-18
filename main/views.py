from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (response):
    return render (response, "main/home.html",{})

def about(response):
    return render(response, "main/about_test.html",{})

def results(request):
    main_dict={
        0:'Monkey',
        1:'Rooster',
        2:'Dog',
        3:'Pig',
        4:'Rat',
        5:'Ox',
        6:'Tiger',
        7:'Rabbit',
        8:'Dragon',
        9:'Snake',
        10:'Horse',
        11:'Sheep'
    }
    name= request.POST.get('Name')
    byear=int(request.POST.get('Byear'))
    byear2=int(byear%12)
    byear2=main_dict[byear2]
    source=byear2+".jpg"
    context={'name':name, 'byear':byear2, 'source':source}
    
    return render(request, "main/results.html",context)