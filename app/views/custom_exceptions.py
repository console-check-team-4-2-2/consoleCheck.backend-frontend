from django.shortcuts import render, redirect

def error404(request, exception):
    if not request.user.is_authenticated:
        return redirect("main_app:index")
    c = {
        'info' : 'Страница не найдена'
    }
    return render(request, '404.html', c, status=404)

def error500(request, *args, **argv):
    if not request.user.is_authenticated:
        return redirect("main_app:index")
    c = {
        'info' : 'Произошла ошибка'
    }
    return render(request, '500.html', c, status=500)