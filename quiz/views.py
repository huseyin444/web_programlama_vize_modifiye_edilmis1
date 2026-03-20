from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Soru, Secenek

def index(request):
    son_sorular = Soru.objects.order_by("-yayinlanma_tarihi")[:5]
    context = {"son_sorular": son_sorular}
    return render(request, "quiz/index.html", context)

def detay(request, soru_id):
    soru = get_object_or_404(Soru, pk=soru_id)
    return render(request, "quiz/detay.html", {"soru": soru})

def sonuclar(request, soru_id):
    soru = get_object_or_404(Soru, pk=soru_id)
    # Sonuç sayfasında seçilen şıkkın durumunu göstermek için render kullanıyoruz
    return render(request, "quiz/sonuclar.html", {"soru": soru})

def cevapla(request, soru_id):
    soru = get_object_or_404(Soru, pk=soru_id)
    try:
        # Formdan gelen 'secenek' ID'sini alıyoruz
        secilen_secenek = soru.secenek_set.get(pk=request.POST["secenek"])
    except (KeyError, Secenek.DoesNotExist):
        # Eğer bir şık seçilmeden butona basıldıysa, hata mesajıyla detay sayfasına geri dön
        return render(request, "quiz/detay.html", {
            "soru": soru,
            "error_message": "Lütfen bir şık seçiniz.",
        })
    else:
        # Seçilen şık doğru mu değil mi kontrol ediyoruz
        if secilen_secenek.dogru_mu:
            sonuc_mesaji = "Tebrikler! Doğru cevap."
        else:
            sonuc_mesaji = "Maalesef yanlış cevap."

        # Sonuçları göstermek için sonuçlar sayfasına verileri gönderiyoruz
        return render(request, "quiz/sonuclar.html", {
            "soru": soru,
            "sonuc": sonuc_mesaji,
            "secilen": secilen_secenek
        })