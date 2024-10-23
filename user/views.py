from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required  # Ensure the user is logged in before accessing the logout view
def LogoutView(request):
    logout(request)
    return redirect("main:index")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:index")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})
