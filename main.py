import os
import json
import urllib.request
import urllib.parse

def main(context):
    # Değişkenleri al
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')

    if not token or not chat_id:
        return context.res.send("Hata: Değişkenler eksik!")

    # Telegram Mesajı Gönderme (urllib kullanarak - Kütüphane gerektirmez)
    message = "🚀 LegacyEngine: Dış kütüphane bağımlılığı kaldırıldı, sistem aktif!"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    data = urllib.parse.urlencode({
        'chat_id': chat_id,
        'text': message
    }).encode('utf-8')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            return context.res.send("Mesaj başarıyla gönderildi!")
    except Exception as e:
        return context.res.send(f"Hata oluştu: {str(e)}")
