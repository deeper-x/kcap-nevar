from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def proxy_auth(request):
    username = request.POST.get('form-username')
    password = request.POST.get('form-password')
    next_page = request.POST.get('next_page')

    obj_user = authenticate(username=username, password=password)

    if obj_user is not None:
        login(request, obj_user)

        # if get parameter ?next= is set, redirect there
        if next_page != "home_page":
            return redirect(next_page)

        # redirect to main page
        return redirect("home_page")

    else:
        return redirect("login")


def signup(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()

            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home_page')
    else:
        signup_form = UserCreationForm()

    return render(request, 'registration/signup.html', {'signup_form': signup_form})


@login_required
def logout_view(request):
    logout(request)

    return redirect('login')
