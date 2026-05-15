import os
from flask import Flask, render_template, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indir', methods=['POST'])
def indir():
    url = request.form.get('url')
    try:
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({
                "title": info.get('title', 'Video'),
                "url": info.get('url') or (info.get('formats')[-1]['url'] if info.get('formats') else None),
                "thumb": info.get('thumbnail', '')
            })
    except:
        return jsonify({"error": "Hata"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
