import sqlite3
import pandas as pd
from datetime import datetime

def siparis_raporu():
    """
    Masalara göre günlük veya geçmişe dönük sipariş raporu oluşturur.
    """
    conn = sqlite3.connect('restoran.db')
    query = """
    SELECT masa_no, urun, SUM(miktar) AS toplam_miktar, SUM(fiyat * miktar) AS toplam_fiyat, DATE(zaman) AS tarih
    FROM siparisler
    GROUP BY masa_no, urun, tarih
    ORDER BY tarih DESC, masa_no
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    if df.empty:
        print("📋 Sipariş raporu boş.")
    else:
        print("📋 Sipariş Raporu:")
        print(df)
    
    # İstersen Excel olarak da kaydedebilirsin:
    # df.to_excel('siparis_raporu.xlsx', index=False)

    return df

def performans_raporu():
    """
    Garson bazlı performans raporu oluşturur.
    """
    conn = sqlite3.connect('restoran.db')
    query = """
    SELECT garson_id, masa_no, COUNT(*) AS ziyaret_sayisi, AVG(ilgi_suresi) AS ortalama_ilgi_suresi, DATE(tarih) AS tarih
    FROM performans
    GROUP BY garson_id, masa_no, tarih
    ORDER BY tarih DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    if df.empty:
        print("📊 Performans raporu boş.")
    else:
        print("📊 Performans Raporu:")
        print(df)
    
    # İstersen Excel olarak da kaydedebilirsin:
    # df.to_excel('performans_raporu.xlsx', index=False)

    return df


if __name__ == "__main__":
    print("🔎 Raporlayıcı çalışıyor...\n")
    siparis_raporu()
    print("\n")
    performans_raporu()
