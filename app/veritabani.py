import sqlite3
import sqlite3
import pandas as pd

# app/veritabani.py

from datetime import datetime

def tablo_olustur():
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS musteri_giris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        masa_no INTEGER NOT NULL,
        giris_zamani DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()
    print("✅ musteri_giris tablosu oluşturuldu veya zaten mevcut.")
    
if __name__ == "__main__":
    tablo_olustur()

def musteri_oturdu(masa_no):
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO musteri_giris (masa_no) VALUES (?)
    """, (masa_no,))
    
    conn.commit()
    conn.close()
    print(f"✅ Masa {masa_no} için müşteri giriş kaydı oluşturuldu.")

def musteri_giris_ekle(masa_no):
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO musteri_giris (masa_no, giris_zamani) VALUES (?, ?)", (masa_no, datetime.now()))
    conn.commit()
    conn.close()


def garson_ilgi_suresi_ekle(masa_no, garson_id, ilgi_suresi_saniye):
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO performans (garson_id, masa_no, ilgi_suresi, tarih)
        VALUES (?, ?, ?, ?)
    """, (garson_id, masa_no, ilgi_suresi_saniye, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    conn.commit()
    conn.close()
    print(f"✅ Garson {garson_id} için masa {masa_no} ilgi süresi {ilgi_suresi_saniye}s olarak kaydedildi.")

def test_siparis_ekle():
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()

    siparisler = [
        (1, 'g1', 'Çorba', 1, 25.0, datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        (2, 'g1', 'Izgara', 2, 80.0, datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        (3, 'g2', 'Tatlı', 1, 30.0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    ]

    cursor.executemany("""
        INSERT INTO siparisler (masa_no, garson_id, urun, miktar, fiyat, zaman)
        VALUES (?, ?, ?, ?, ?, ?)
    """, siparisler)

    conn.commit()
    conn.close()
    print("✅ Test siparişleri başarıyla eklendi.")

def uyarilari_kontrol_et():
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()

    # 1 dakika içinde garson gelmeyen masaları buluyoruz
    cursor.execute("""
        SELECT mg.masa_no, mg.giris_zamani
        FROM musteri_giris mg
        LEFT JOIN performans p ON mg.masa_no = p.masa_no AND p.tarih > mg.giris_zamani
        WHERE p.id IS NULL
          AND datetime(mg.giris_zamani, '+1 minutes') < datetime('now')
    """)

    gec_kalan_masalar = cursor.fetchall()
    for masa_no, giris_zamani in gec_kalan_masalar:
        print(f"⚠️ Masa {masa_no} için garson 1 dakikada gelmedi! Performans negatif etki kaydı yapılmalı.")
        # Burada performans tablosuna negatif ilgi süresi veya başka bir mekanizma eklenebilir.
        # Örnek negatif kayıt:
        cursor.execute("""
            INSERT INTO performans (garson_id, masa_no, ilgi_suresi, tarih)
            VALUES (?, ?, ?, ?)
        """, ('unknown', masa_no, -60, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        # Müşteri giriş kaydını da silebiliriz ki uyarı tekrar olmasın:
        cursor.execute("DELETE FROM musteri_giris WHERE masa_no = ?", (masa_no,))

    conn.commit()
    conn.close()

def garson_ilgi_suresi_ekle(masa_no, garson_id, ilgi_suresi):
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()
    
    zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute("""
        INSERT INTO performans (garson_id, masa_no, ilgi_suresi, tarih)
        VALUES (?, ?, ?, ?)
    """, (garson_id, masa_no, ilgi_suresi, zaman))
    
    conn.commit()
    conn.close()
    print(f"✅ Garson {garson_id} için masa {masa_no} ilgi süresi {ilgi_suresi}s kaydedildi.")

def tum_siparisleri_getir():
    """
    Tüm siparişleri veritabanından çekip pandas DataFrame olarak döner.
    """
    conn = sqlite3.connect('restoran.db')
    query = """
        SELECT masa_no, urun, miktar, fiyat, zaman
        FROM siparisler
        ORDER BY zaman DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def veritabani_olustur():
    conn = sqlite3.connect('restoran.db')
    cursor = conn.cursor()

    # Sipariş tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS siparisler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            masa_no INTEGER,
            garson_id TEXT,
            urun TEXT,
            miktar INTEGER,
            fiyat REAL,
            zaman DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Garson performans tablosu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS performans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            garson_id TEXT,
            masa_no INTEGER,
            ilgi_suresi INTEGER,
            tarih DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 💡 Yeni eklenen tablo: garson QR tanımlama kayıtları
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS garson_kayitlari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            masa_no TEXT,
            garson_id TEXT,
            zaman TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Veritabanı başarıyla oluşturuldu.")

if __name__ == "__main__":
    veritabani_olustur()

if __name__ == "__main__":
    from veritabani import tablo_olustur, musteri_oturdu, garson_ilgi_suresi_ekle, uyarilari_kontrol_et
    
    tablo_olustur()  # Tablo yoksa oluşturur

    # Test müşteri giriş kaydı
    musteri_oturdu(1)  # Masa 1 için müşteri geldi
    
    # Test garson ilgi süresi (örneğin 45 saniye)
    garson_ilgi_suresi_ekle(1, 'g1', 45)
    
    # Test uyarı kontrolü (burada hemen çalıştırırsan 1 dakikayı geçmediği için kayıt olmayabilir)
    uyarilari_kontrol_et()
