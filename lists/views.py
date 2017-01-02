from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


def home_page(request):
    #return HttpResponse('<html><title>Listy rzeczy do zrobienia</title></html>')
    
    if request.method == 'POST':
        Item.objects.create(text = request.POST['item_text'])
        return redirect('/')

    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()
    items = Item.objects.all()
    return render(request,'home.html',{'items':items})


# Create your views here.
