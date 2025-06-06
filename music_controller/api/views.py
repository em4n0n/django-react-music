from django.http import HttpResponse

def main(request):
    return HttpResponse("<h1>Welcome to the Music Controller API!</h1>")
