from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'jujupa',
    })   # o django vai buscar em recipes/templates
    # sem precisar indicar o caminho e context vai como parametro
    # para ser acessado na chamada.(home.html do recipes)


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'jujupa',
    })
