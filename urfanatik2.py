from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import sys,os

def yeni_dosya_indir():
    url = "https://raw.githubusercontent.com/nusretcakir/urfanatik/main/urfanatik2.py"
    r = requests.get(url)
    open('urfanatik2.py', 'wb').write(r.content)

    url = "https://raw.githubusercontent.com/nusretcakir/urfanatik/main/v.txt"
    r = requests.get(url)
    open('v.txt', 'wb').write(r.content)

def version_test():

    #programin yerel surumu
    with open("v.txt","r") as f:
        version = int(f.read())  
    
    #programin net surumu
    url = "https://raw.githubusercontent.com/nusretcakir/urfanatik/main/v.txt"
    new_version = int(str((BeautifulSoup(requests.get(url).content,"html.parser"))))
    
    if version != new_version:
        yeni_dosya_indir()
        print("Program güncellendi,yeniden başlatılıyor...")
        os.execv(sys.executable, [sys.executable] + sys.argv)
        sys.exit()

# 1411945130 hc chat id
# 1571716280 me chatid
# 6343655697 fa chat id

def gonder(text):

    chat_ids = ["1571716280","1219734793",]
    
    api_url = f"https://api.telegram.org/bot6372109892:AAEhkH7mMGwbiLOXDKzgpazL2oc0iAnYs5k/sendMessage"

    for chat_id in chat_ids:
        data = {
            'chat_id': chat_id,
            'text': text,
        }
        response = requests.post(api_url, data=data)

def veritabani_olustur():
    conn = sqlite3.connect("haberler.db")
    # Bir Cursor objesi oluştur
    cursor = conn.cursor()
    
    # Haberler tablosunu oluştur
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS haberler (
            id INTEGER PRIMARY KEY,
            baslik TEXT NOT NULL,
            url TEXT NOT NULL
        )
    """)
    
    # Değişiklikleri kaydet ve bağlantıyı kapat
    conn.commit()
    conn.close()

def haber_ekle(baslik, url):
    try:
        # Veritabanına bağlan
        conn = sqlite3.connect("haberler.db")
        # Bir Cursor objesi oluştur
        cursor = conn.cursor()
        
        # URL'nin veritabanında zaten var olup olmadığını kontrol et
        cursor.execute("SELECT * FROM haberler WHERE url = ?", (url,))
        existing_news = cursor.fetchone()
        
        if existing_news:
            print("Bu URL zaten veritabanında var.")
        else:
            # Haberi tabloya ekle
            cursor.execute("INSERT INTO haberler (baslik, url) VALUES (?, ?)", (baslik, url))
            print("Haber başarıyla eklendi.")
            mesaj = baslik + "\n" + url
            gonder(mesaj)
        
        # Değişiklikleri kaydet ve bağlantıyı kapat
        conn.commit()
        conn.close()
    except Exception as e:
        print("Haber ekleme hatası:", e)

def haber_cek_urfanatik():

    url = "https://www.urfanatik.com/haberleri/viransehir"

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

    headers = {
    'User-Agent': user_agent
    }
    try:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        print("Sayfa okunamadi yada internet baglantisi kotu")
        pass

    try:
        tum_divler = soup.find_all('div', class_='row c-nb c-nb-ms gut-1 gut-0-ms')
        for i in tum_divler:
            
            a_href_etiketi = i.find('a', href=True)
            url2 = "https://www.urfanatik.com"+a_href_etiketi['href']

            i = str(i.text.strip()).split("\n")
            
            baslik = i[0]
            ozet = i[3]
            haber_ekle(baslik, url2)
            
   
    except:
        print("HTML parsta sıkıntı var")
        pass

def haber_cek_urfanatik_jandarma():

    url = "https://www.urfanatik.com/haberleri/jandarma"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

    headers = {
    'User-Agent': user_agent
    }
    try:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        print("Sayfa okunamadi yada internet baglantisi kotu")
        pass

    try:
        tum_divler = soup.find_all('div', class_='row c-nb c-nb-ms gut-1 gut-0-ms')
        for i in tum_divler:
            
            a_href_etiketi = i.find('a', href=True)
            url2 = "https://www.urfanatik.com"+a_href_etiketi['href']

            i = str(i.text.strip()).split("\n")
            
            baslik = i[0]
            ozet = i[3]
            haber_ekle(baslik, url2)
            
    
    except:
        print("HTML parsta sıkıntı var")
        pass

def haber_cek_ajansurfa():

    url = "https://www.ajansurfa.com/haberleri/viransehir"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

    headers = {
    'User-Agent': user_agent
    }
    try:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        print("Sayfa okunamadi yada internet baglantisi kotu")
        pass

    try:
        tum_divler = soup.find_all('div', class_='row c-nb c-nb-ms gut-1 gut-0-ms')
        for i in tum_divler:
            
            a_href_etiketi = i.find('a', href=True)
            url2 = "https://www.ajansurfa.com"+a_href_etiketi['href']

            i = str(i.text.strip()).split("\n")
            
            baslik = i[0]
            ozet = i[3]
            haber_ekle(baslik, url2)
            
   
    except:
        print("HTML parsta sıkıntı var")
        pass

def haber_cek_urfadasin():

    url = "https://www.urfadasin.com/haberleri/viransehir"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

    headers = {
    'User-Agent': user_agent
    }
    try:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        print("Sayfa okunamadi yada internet baglantisi kotu")
        pass

    try:
        tum_divler = soup.find_all('div', class_='card border-0 h-100 rounded-0')
        for i in tum_divler:
            
            a_href_etiketi = i.find('a', href=True)
            url2 = "https://www.urfadasin.com"+a_href_etiketi['href']

            i = str(i.text.strip()).split("\n")

            baslik = i[0]
            haber_ekle(baslik, url2)
                
    except:
        print("HTML parsta sıkıntı var")
        pass

if __name__ == "__main__":
    try: 
        veritabani_olustur()
    except:
        print("veritabanı oluşturmada hata")
    while True:
        try:
            version_test()
            haber_cek_urfanatik()
            haber_cek_urfanatik_jandarma()
            haber_cek_ajansurfa()
            haber_cek_urfadasin()
        except:
            print("bir yerlerde hata var onu bul neo..")
        time.sleep(60)