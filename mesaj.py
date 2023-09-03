import requests

def gonder(text):
    api_url = f"https://api.telegram.org/bot6372109892:AAEhkH7mMGwbiLOXDKzgpazL2oc0iAnYs5k/sendMessage"
    data = {
        'chat_id': "1571716280",
        'text': text,
    }

    response = requests.post(api_url, data=data)

    if response.status_code == 200:
        print("Mesaj başarıyla gönderildi!")
    else:
        print("Mesaj gönderme hatası:", response.status_code, response.text)
