import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
from veritabani import garson_ilgi_suresi_ekle, musteri_giris_ekle

def garson_qr_tanima(masa_no):
    print(f"📸 Kamera açılıyor... Masa {masa_no} için QR kod bekleniyor...")

    cap = cv2.VideoCapture(0)  # USB ya da laptop kamerası
    start_time = datetime.now()
    garson_tanindi = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⛔ Görüntü alınamadı.")
            break

        elapsed_time = (datetime.now() - start_time).total_seconds()

        if elapsed_time > 60 and not garson_tanindi:
            print("⏰ 60 saniye içinde garson gelmedi! UYARI ⚠️")
            musteri_giris_ekle(masa_no)
            garson_ilgi_suresi_ekle(masa_no, "gecikti", 999)
            break  # uyarı verildi, çıkış yap

        for barcode in decode(frame):
            qr_data = barcode.data.decode('utf-8')
            print(f"✅ Garson tanındı: {qr_data}")

            ilgi_suresi = int(elapsed_time)
            print(f"🕒 İlgi süresi: {ilgi_suresi} saniye")

            musteri_giris_ekle(masa_no)
            garson_ilgi_suresi_ekle(masa_no, qr_data, ilgi_suresi)

            garson_tanindi = True
            break  # Döngüden çık

        cv2.imshow("Garson QR Tanıma", frame)

        if garson_tanindi:
            break  # Garson tanındıysa döngüden çık

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("❌ İşlem iptal edildi.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    garson_qr_tanima(1)  # Masa 1 için başlatıyor
