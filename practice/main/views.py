from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def clients(request):
    return render(request, 'main/clients.html')

def moihiki(request):
    return render(request, 'main/moihiki.html')

def zapisi(request):
    return render(request, 'main/zapisi.html')

def zapisi_change(request):
    return render(request, 'main/zapisi_change.html')

def moihiki_change(request):
    return render(request, 'main/moihiki_change.html')

def clients_change(request):
    return render(request, 'main/clients_change.html')
