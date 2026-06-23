from django.shortcuts import render


def about(request):
<<<<<<< HEAD
    return render(request, "pages/about.html")


def rules(request):
    return render(request, "pages/rules.html")
=======
    return render(request, 'pages/about.html')


def rules(request):
    return render(request, 'pages/rules.html')
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
