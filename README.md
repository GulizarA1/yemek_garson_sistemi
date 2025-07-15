# 🍽️ Yemek ve Garson Performans Sistemi

Bu proje, bir restoranda masalara gelen yemeklerin otomatik olarak tanınmasını, fiyatlandırılmasını ve garsonların performansının izlenmesini sağlayan bir **bilgisayarlı görü tabanlı akıllı sistemdir**.

---

## 🎯 Amaç

- Masalara gelen yemekleri kamera aracılığıyla tanımak.
- Siparişleri otomatik olarak veritabanına kaydetmek.
- Garsonun müşteriye ilgisini ölçmek ve geç müdahale durumlarında performans cezası vermek.
- Günlük ve geçmişe yönelik raporlar oluşturmak.

---

## 🔧 Kullanılan Teknolojiler

- 💻 **Python 3.10+**
- 🔥 **Flask** - Web Arayüzü
- 🎥 **OpenCV** - Kamera İşleme
- 📦 **YOLOv8 (isteğe bağlı)** - Yemek Tanıma
- 📊 **SQLite** - Veritabanı
- 📷 **Pyzbar** - QR Kod ile Garson Tanıma

---

## 🧱 Klasör Yapısı

yemek_garson_sistemi/
│
├── app/
│ ├── veritabani.py # Veritabanı işlemleri
│ ├── masa_reset.py # Masa sıfırlama
│ ├── raporlayici.py # Performans raporları
│ ├── kamera_garson.py # QR kod ile garson tanıma
│ ├── kamera_yemek.py # Yemek tanıma (YOLOv8)
│
├── templates/
│ ├── index.html
│ ├── garson.html
│ ├── yemek.html
│ ├── siparisler.html
│ ├── masa_reset.html
│ └── rapor.html
│
├── main.py # Flask ana uygulama dosyası
├── requirements.txt # Bağımlılıklar
├── restoran.db # (GİZLİ) SQLite veritabanı



---

## 🚀 Kurulum

### 1. Sanal ortam oluştur
```bash
python -m venv venv
venv\Scripts\activate   # Windows
2. Gerekli kütüphaneleri yükle

pip install -r requirements.txt
3. Uygulamayı çalıştır

python main.py
Tarayıcıdan şu adrese git:
http://127.0.0.1:5000



## 🧪 Temel Özellikler

📋 Sipariş takibi ve görselleştirme

👤 Garson tanıma (QR ile)

🕒 İlgi süresi hesaplama

⚠️ Garson gecikme uyarı sistemi

📊 Performans raporları

🔄 Masa sıfırlama



##🧠 Gelecek Geliştirmeler (Opsiyonel)

Yüz tanıma ile garson tanıma

Mobil arayüz entegrasyonu

YOLOv8 ile gelişmiş yemek tanıma modeli

E-posta ile günlük rapor gönderimi


##🤝 Katkıda Bulunmak

Bu repoyu fork'la

Kendi branch'ini oluştur: git checkout -b yenilik

Değişikliklerini commit et: git commit -m "Yeni özellik"

Push et: git push origin yenilik

Pull Request gönder 🚀

##🧑‍🎓 Hazırlayan

Gülizar A.
Bilgisayar Mühendisliği 
GitHub

🏁 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

---
