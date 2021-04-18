def add_variable_to_context(request):
    return {
        'is_author': request.user.groups.filter(name='authors').exists()
    }