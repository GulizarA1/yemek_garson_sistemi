import sqlite3
from datetime import datetime

def masa_reset(masa_no=None):
    """
    Masa reset fonksiyonu.
    - masa_no verilirse sadece o masanın sipariş, performans ve garson kayıtlarını siler.
    - masa_no verilmezse tüm masalar ve kayıtlar sıfırlanır.
    """
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()

    if masa_no is not None:
        # Belirli masanın kayıtlarını sil
        cursor.execute("DELETE FROM siparisler WHERE masa_no = ?", (masa_no,))
        cursor.execute("DELETE FROM performans WHERE masa_no = ?", (masa_no,))
        cursor.execute("DELETE FROM garson_kayitlari WHERE masa_no = ?", (masa_no,))
        print(f"✅ Masa {masa_no} başarıyla resetlendi.")
    else:
        # Tüm masaların kayıtlarını sil
        cursor.execute("DELETE FROM siparisler")
        cursor.execute("DELETE FROM performans")
        cursor.execute("DELETE FROM garson_kayitlari")
        print(f"✅ Tüm masalar ve siparişler {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} tarihinde sıfırlandı.")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Örnek kullanım:
    # masa_reset(2)  # Sadece masa 2 resetlenir
    # veya
    masa_reset()    # Tüm kayıtlar sıfırlanır
