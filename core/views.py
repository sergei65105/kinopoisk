from django.contrib.auth import authenticate, login
from core.models import User
from django.shortcuts import render, redirect


def signup(request):
    if request.user.is_authenticated:
        return redirect('profile', id=request.user.id)
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        username = request.POST['username']
        repeat_password = request.POST['repeat_password']
        error = ''
        if password != repeat_password:
            error = 'Пароли не совпали'
        elif not password:
            error = 'Введите пароль'
        elif not username:
            error = 'Введите имя'
        elif not email:
            error = 'Введите почту'

        if error != '':
            return render(request, 'core/auth/signup.html', {'error': error})
        else:
            User.objects.create_user(username=username,
                                     email=email,
                                     password=password)
            return redirect('signin')
    return render(request, 'core/auth/signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('profile', id=request.user.id)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', id=user.id)

    return render(request, 'core/auth/signin.html')


def profile(request, id):
    if not request.user.is_authenticated:
        return redirect('signin')
    user = User.objects.get(id=id)
    return render(request, 'core/auth/profile.html', {'user': user})


def logout(request):
    from django.contrib.auth import logout
    if not request.user.is_authenticated:
        return redirect('signin')
    logout(request)
    return redirect('signin')
