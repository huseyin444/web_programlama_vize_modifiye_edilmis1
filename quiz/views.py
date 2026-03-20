from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Soru

def index(request):
    son_sorular = Soru.objects.order_by("-yayinlanma_tarihi")[:5]
    context = {"son_sorular": son_sorular}
    return render(request, "quiz/index.html", context)

def detay(request, soru_id):
    # Soru bulunamazsa otomatik olarak 404 hata sayfası gösterir
    soru = get_object_or_404(Soru, pk=soru_id)
    return render(request, "quiz/detay.html", {"soru": soru})

def sonuclar(request, soru_id):
    response = "Soru %s sonuçlarına bakıyorsunuz."
    return HttpResponse(response % soru_id)

def cevapla(request, soru_id):
    return HttpResponse("Soru %s için cevap gönderiyorsunuz." % soru_id)