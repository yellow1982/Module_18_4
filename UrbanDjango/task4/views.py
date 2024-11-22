from django.shortcuts import render
from django.views.generic import TemplateView

def main_page(request):
    return render(request, 'forth_task/platform.html')

def games(request):

    games = ['AtomicHeart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'games': games,

    }
    return render(request, 'forth_task/games.html', context)

def cart(request):
    return render(request, 'forth_task/cart.html')

def menu(request):
    return render(request, 'forth_task/menu.html')
