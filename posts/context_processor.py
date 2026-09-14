def categories(request):
    categories = [
    'programming',
    'Food',
    'Travel'
]
    #Alwayys it will return the dictionary
    return {'categories' : categories}
