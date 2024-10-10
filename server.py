from flask import Flask, redirect, request, make_response, render_template
import requests

import downloader
app = Flask(__name__)

@app.route('/download/<url>')
def download(url):
    file_url = downloader.get_download_url(url)
    
    response = make_response(redirect(file_url))
    
    response.headers['Content-Disposition'] = 'attachment; filename="file.zip"'
    
    return response

@app.route('/preview/<url>')
def preview(url):
    if "=" in url:
        url = url[::-1].split("=",1)[0][::-1]
    
    image_url = f"https://i.ytimg.com/vi_webp/{url}/maxresdefault.webp"
    
    # Fetch the image
    response = requests.get(image_url)

    # Create a response with the image data
    response_to_client = make_response(response.content)
    response_to_client.headers['Content-Type'] = response.headers['Content-Type']
    response_to_client.headers['Access-Control-Allow-Origin'] = '*'

    return response_to_client
        
    thumbnail_url = downloader.get_video_thumbnail(url)
    
    return redirect(thumbnail_url)

@app.route('/')
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=False, port=14001)