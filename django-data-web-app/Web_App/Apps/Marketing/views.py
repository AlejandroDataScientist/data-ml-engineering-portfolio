from django.shortcuts import render

def marketing_blog(request):
    return render(request, 'marketing/blog.html')
