from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    #return HttpResponse('<html><title>Listy rzeczy do zrobienia</title></html>')
    
    return render(request,'home.html',{'new_item_text':request.POST.get('item_text','')})


# Create your views here.
