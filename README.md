# 🍽️ Yemek Fiyatı ve Garson Performansı Ölçme Sistemi

Bu proje, bir restoranda masa üzerine monte edilen kameralar aracılığıyla müşterilere getirilen yemeklerin bilgisayarlı görü teknikleriyle tanınmasını, fiyatlandırılmasını ve garsonların performansının ölçülmesini amaçlar. Kullanıcılar sipariş verdikten sonra yemekler otomatik olarak sayılır ve fiyatlandırılır. Müşteri masadan kalktığında garson masayı işaretleyip hesabı sıfırlar. Günlük ve geçmiş raporlar oluşturularak garson bazlı performans değerlendirmesi yapılır.

---

## 🎯 Proje Amaçları

- Müşteri siparişlerinin doğru tanınması ve fiyatlandırılması  
- Siparişlerin otomatik olarak veritabanına kaydedilmesi  
- Garsonların masalara gösterdiği ilgi süresinin takibi  
- 1 dakika içinde garson gelmezse uyarı verilmesi ve performans puanının düşürülmesi  
- Günlük ve geçmişe yönelik detaylı performans ve sipariş raporlarının sunulması  
- QR kod / yüz tanıma ile garson kimlik doğrulama  
- Kullanıcı dostu web arayüzü ile kolay sistem yönetimi  

---

## 🚀 Özellikler

- 🔍 **Nesne Tanıma:** Yemekler ve garsonlar masa üzerindeki kameralarla tanımlanır.  
- 📦 **Sipariş Takibi:** Masa bazlı sipariş verileri veritabanında saklanır.  
- ⏱️ **Garson Performansı:** İlgi süreleri ölçülür, gecikmeler tespit edilerek sistem tarafından uyarı verilir.  
- 📊 **Raporlama:** Sipariş ve performans raporları web arayüzü üzerinden Excel dosyası olarak görüntülenebilir.  
- 🔄 **Resetleme:** Masalar sıfırlanarak yeni müşteri için hazır hale getirilir.  
- 🧩 **Modüler Yapı:** Flask tabanlı backend ile HTML/CSS frontend uyumlu çalışır.  

---

## 🛠️ Kullanılan Teknolojiler

- Python 3.10  
- [YOLOv8 (Ultralytics)](https://github.com/ultralytics/ultralytics) — Yemek nesne tanıma  
- OpenCV — Kamera görüntüsü işleme  
- Pyzbar — QR kod tanıma  
- Flask — Web tabanlı kontrol paneli  
- SQLite — Hafif veritabanı  
- Pandas & openpyxl — Excel raporlama  
- HTML5, CSS3  

---

## ⚙️ Kurulum ve Çalıştırma

```bash
# 1. Python 3.10 veya üstü kurulu olmalı
python3 --version

# 2. Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 4. Uygulamayı başlatın
python main.py


yemek_garson_sistemi/
│
├── app/
│   ├── veritabani.py         # Veritabanı işlemleri
│   ├── masa_reset.py         # Masa sıfırlama işlemleri
│   ├── raporlayici.py        # Günlük raporlama modülü
│   ├── kamera_garson.py      # QR kod ile garson tanıma
│   ├── kamera_yemek.py       # YOLOv8 ile yemek tanıma
│
├── templates/
│   ├── index.html
│   ├── garson.html
│   ├── yemek.html
│   ├── siparisler.html
│   ├── masa_reset.html
│   └── rapor.html
│
├── main.py                   # Ana uygulama dosyası
├── requirements.txt          # Gerekli kütüphaneler
├── restoran.db               # (GİZLİ) SQLite veritabanı


🧪 Kullanım Senaryosu
Müşteri masaya oturur.

Garson, QR kodunu kameraya göstererek sisteme giriş yapar.

Müşteriye getirilen yemekler sistem tarafından tanınır ve fiyatlandırılır.

Müşteri masadan kalktığında garson masayı sıfırlar.

Sistem günlük ve haftalık performans raporlarını otomatik oluşturur.

🧱 Karşılaşılan Zorluklar ve Çözümler
Zorluk	Çözüm
🍝 Yemeklerin üst üste gelmesi	Kamera açısı optimize edildi
💡 Işıklandırma sorunları	Görüntü filtreleme teknikleri eklendi
📷 QR kod görünmemesi	Garson kartlarının yüksekliği standartlaştırıldı
🕐 Gerçek zamanlı performans takibi	Uyarı sistemi ile zamanlı ölçüm eklendi

🔮 Geliştirme Önerileri
📱 Mobil uygulama ile garsonlara anlık bildirim

🗣️ Sesli asistan entegrasyonu

💳 Gerçek zamanlı ödeme takibi

⭐ Müşteri memnuniyet puanlama sistemi

Bu proje, bilgisayarlı görü, zaman takibi ve insan etkileşimlerinin bir araya geldiği modern bir restoran deneyimi sunmayı amaçlar.

