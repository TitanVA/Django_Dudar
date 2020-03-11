from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/homePage.html')


def contact(request):
    return render(request, 'mainapp/basic.html', {'values':
    ['Если у Вас остались вопросы, то задавайте их мне по телефону',
     '(000) 000-00-00', 'example@mail.ru']})
