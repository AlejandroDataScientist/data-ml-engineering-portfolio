from django.shortcuts import render

def politicas_privacidad(request):
    return render(request, 'Legal/politicas.html')
