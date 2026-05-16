# کلیلەکەت لە بەشی Settingsی گیتهەبەکەت دروست دەکەیت (PAT)
GITHUB_TOKEN = "لێرە_کلیلە_بەخۆڕاییەکەی_گیتهەب_دابنێ"

@app.route('/api/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_message = user_data.get('message', '')

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        # بەکارهێنانی مۆدێلی لاما ٣ لەسەر سێرڤەرەکانی گیتهەب
        "model": "meta-llama-3-8b-instruct", 
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post("https://models.inference.ai.azure.com/chat/completions", json=payload, headers=headers)
    # ... پاشان وەڵامەکە بە هەمان شێوە دەگەڕێنێتەوە بۆ ماڵپەڕەکەت
