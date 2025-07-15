"""from flask import Flask, request, render_template, send_file
from yt_dlp import YoutubeDL
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save in downloads folder
    }
    
    try:
        # Download the video using yt-dlp
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url)
            video_title = ydl.prepare_filename(info)  # Get the file path
            
        # Send the file to the user
        return send_file(video_title, as_attachment=True)
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    # Ensure the downloads folder exists
    os.makedirs('downloads', exist_ok=True)
    app.run(debug=True)"""
    
from flask import Flask, request, render_template,jsonify
from yt_dlp import YoutubeDL
import json

app = Flask(__name__)

# @app.route('/',methods=['GET','POST'])
# def index():



#     return render_template('index.html')

@app.route('/download', methods=['GET','POST']) 
def download_video():
    if request.method == 'POST':
        data = request.json
        url = data.get('link')  # Get the video URL from the user
        try:
            # Use yt-dlp to get the direct download link
            ydl_opts = {
                'quiet': True,  # Suppress console output
                'format': 'best',  # Choose the best video format
            }
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)  # Fetch info without downloading
                direct_url = info['url']  # Get the direct video URL

            # Return the direct URL to the user
            return jsonify({'message':'Done','link': direct_url}),200
        
        except Exception as e:
            print(e)
            return jsonify({'message': f'error {e}'}), 400
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

