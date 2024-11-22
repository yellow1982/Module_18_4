from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

def sign_up_by_html(request):
    users = ['Alex', 'Mike', 'John']
    info = {}
    context = {'info': info}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users and password == repeat_password and int(age) >= 18:
            return HttpResponse(f'Приветсвуем, {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    users = ['Alex', 'Mike', 'John']
    info = {}
    form = UserRegister()
    context = {
        'info': info,
        'form': form,
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            if username in users:
                info['error'] = 'Пользователь уже существует'
        else:
            form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context)