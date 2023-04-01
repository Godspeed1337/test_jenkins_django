from django.http import HttpResponse


def index(request):
    return HttpResponse("Деплой с Дженкинса произошел успешно")
