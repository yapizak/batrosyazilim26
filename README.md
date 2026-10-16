GÖREV 2: OTONOM İHA HEDEF ÖNCELİKLENDİRME VE KİLİTLENME SİSTEMİ

Bu görevde, bilgisayarlı görü (YOLOv8) ile tespit edilen nesneler arasından otonom bir İHA'nın karar mekanizmasını simüle edeceksiniz. İHA aynı anda birden fazla araca yönelemez; en uygun hedefi seçmeli, hedefleme vektörünü hesaplamalı ve duruma göre manevra veya angajman kararı vermelidir.

1. KULLANILACAK DOSYALAR VE KÜTÜPHANELER
- Görsel: Repodaki mevcut img.jpg
- Model: yolov8n.pt
- İzin Verilen Kütüphaneler: ultralytics, opencv-python, math

2. ALGORİTMA ADIMLARI

A. Kamera Merkezi ve Tolerans Çemberi
1. Görüntünün tam merkezini (genişlik / 2, yükseklik / 2) piksel tam sayıları olarak hesaplayın.
2. Bu merkeze 6 piksel yarıçapında mavi, içi dolu bir nokta (cv2.circle) koyun (Kamera Nişangahı).
3. Bu merkezin etrafına yarıçapı 250 piksel olan, içi boş, 2 piksel kalınlığında Mavi bir çember çizin. Bu çember İHA'nın Kilit Menzilidir.

B. Nesne Tespiti ve Filtreleme
1. YOLOv8 ile görseldeki nesneleri tespit edin.
2. Güven Skoru Filtresi: Yalnızca güven skoru (conf) 0.50 üzerinde olan nesneleri dikkate alın.
3. Sınıf Filtresi: Yalnızca sınıfı araba (cls == 2) olan nesneleri işleme alın. Diğer sınıfları (insan, tabela, kamyon vb.) eleyin.

C. Hedef Seçim Algoritması
1. Filtreden geçen tüm araçların merkez noktalarını (hedef_x, hedef_y) piksel tam sayısı olarak hesaplayın.
2. Her bir aracın merkez noktasının, kamera merkezine olan kuş uçuşu piksel mesafesini (Öklid Mesafesi) hesaplayın:
Mesafe = math.hypot(hedef_x - ekran_x, hedef_y - ekran_y)
3. Kamera merkezine olan mesafesi en küçük olan tek bir aracı Birincil Hedef (Primary Target) olarak belirleyin.

D. Görsel Çıktı Kuralları (final_cikti.jpg)
- Birincil Hedef (En Yakın Araç):
Etrafına Kırmızı bir sınırlayıcı kutu (cv2.rectangle, kalınlık: 3) çizin.
Merkezine Kırmızı bir nokta (cv2.circle, yarıçap: 6) koyun.
Kamera merkezinden bu aracın merkezine Sarı bir kilitlenme çizgisi (cv2.line, kalınlık: 2) çekin.
- Diğer Araçlar (Bekleyen Hedefler):
Etraflarına Yeşil bir sınırlayıcı kutu (cv2.rectangle, kalınlık: 2) çizin.
Merkezlerine Yeşil bir nokta (cv2.circle, yarıçap: 4) koyun.

E. Konsol / Terminal Çıktı Standardı
Program çalıştığında terminale seçilen Birincil Hedef için aşağıdaki iki durumdan uygun olanı tek satır halinde yazdırmalısınız

Durum 1 (Hedef Menzil Çemberinin İçindeyse - Mesafe <= 250 px):
[KİLİT BAŞARILI] Hedef Menzilde (X.X px) | Ateş Serbest!

Durum 2 (Hedef Menzil Çemberinin Dışındaysa - Mesafe > 250 px):
[YÖNELİM] Mesafe: X.X px | Sapma: (dx=..., dy=...) | Komut: [Sağa/Sola] ve [Aşağı/Yukarı] Dön

Not: dx = hedef_x - merkez_x ve dy = hedef_y - merkez_y şeklindedir.

3. TESLİM KURALLARI VE UYARI
- Kodunuzu final.py, oluşturulan görseli final_cikti.jpg adıyla repoya yükleyin.
- Ayrıca teslim ettiğiniz kodları birebir görüşmede tahtaya yansıtacaksınız, üzerine sorular soracağım.İHA Yazılım 1. Hafta Görevi
