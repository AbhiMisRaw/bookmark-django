from django.shortcuts import render

from django.shortcuts import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Account disabled")
            else:
                return HttpResponse("Invalid Login credentials")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # created a user object without saving it.
            new_user = user_form.save(commit=False)
            # setting the choosen password
            new_user.set_password(user_form.cleaned_data["password"])
            # after setting up the password saving the user object.
            new_user.save()
            return render(request, "account/register_done.html", {"new_user": new_user})
        else:
            return render(request, "account/register.html", {"user_form": user_form})
    else:
        user_form = UserRegistrationForm()
        return render(request, "account/register.html", {"user_form": user_form})


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})
