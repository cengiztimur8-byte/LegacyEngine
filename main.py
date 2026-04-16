import os
import requests
import google.generativeai as genai

def main(context):
    # 1. Appwrite Global Variables'tan anahtarları çekiyoruz
    tg_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    tg_chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    gemini_key = os.environ.get('GEMINI_API_KEY')

    # 2. Gemini Yapılandırması (Bağlantı testi için)
    try:
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Gemini'ye ufak bir selam verelim
        gemini_response = model.generate_content("Merhaba, sistem aktif mi?")
        gemini_status = "Gemini Bağlantısı: Tamam ✅"
    except Exception as e:
        gemini_status = f"Gemini Hatası: {str(e)} ❌"

    # 3. Telegram Bildirimi Gönderme
    try:
        url = f"https://api.telegram.org/bot{tg_token}/sendMessage"
        payload = {
            "chat_id": tg_chat_id,
            "text": f"🚀 LegacyEngine Ateşlendi!\n\n{gemini_status}\n\nSistem artık Flutter'dan gelecek verileri işlemeye hazır."
        }
        requests.post(url, data=payload)
        
        return context.res.json({
            "status": "success",
            "message": "Sinyal başarıyla gönderildi!"
        })
    except Exception as e:
        return context.res.json({
            "status": "error",
            "message": f"Telegram Hatası: {str(e)}"
        })
