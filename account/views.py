from django.shortcuts import render, redirect


# Create your views here.
def home_page(request):
    return render(request, 'account/home.html')


def guest_login(request):
    return redirect("slot_machine")


def register(request):
    # logic pending
    return render(request, 'account/register.html')