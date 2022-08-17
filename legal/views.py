from django.shortcuts import render, redirect




def privacy(request):
    return render(request, "privacy.html")
