from django.http import HttpResponse

def index(request):
    name = request.GET.get('name', 'name')
    message = request.GET.get('message', 'message')
    text = 'Hello ' + name + '! ' + message
    return HttpResponse(text)
