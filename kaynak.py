import requests

# Hedef web sitesinin URL'sini belirtin
url = "https://www.urfanatik.com/haberleri/viransehir"

# Web sayfasının kaynak kodlarını alın
response = requests.get(url)

# Yanıtı kontrol edin: İstek başarılı mı?
if response.status_code == 200:
    # Kaynak kodları bir dosyaya yazın
    with open('kaynak.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    print('Kaynak kodlar "kaynak.txt" dosyasına kaydedildi.')
else:
    print('İstek başarısız oldu. Durum kodu:', response.status_code)
