from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.forms import UserEditForm
from django.contrib import messages

# Create your views here.


@login_required
def dashboard(request):
    return render(request, "dashboard/home.html", {"section": "dashboard"})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Profile updated " "successfully")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, "dashboard/edit.html", {"user_form": user_form})
