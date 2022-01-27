from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import get_object_or_404, render, reverse, HttpResponseRedirect


def index(request):
    template_name = "homepage/index.html"
    return render(request, template_name)


def login_user(request):
    template_name = "login.html"
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print("user", user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("baakiharu"))

    return render(request, template_name=template_name)
