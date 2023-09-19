from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_page(request, recipe_name):
    servings = int(request.GET.get('servings', 1))
    recipe = {ingr: quantity * servings for ingr, quantity in DATA.get(recipe_name, {}).items()}
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

