from django.http import HttpResponse


def index(request):
    return HttpResponse('<html>'
                        '<body>'
                        '<img src="/media/pby59.jpg" width="100%">'
                        '</body>'
                        '</html>')
