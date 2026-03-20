from django.http import HttpResponse

def index(request):
    return HttpResponse("Merhaba! Bilgi Yarışması projemizin ilk sayfasına hoş geldiniz.")