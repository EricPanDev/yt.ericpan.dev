import yt_dlp

def get_download_url(video_url):
    if not "youtube.com" in video_url:
        video_url = "https://www.youtube.com/watch?v=" + video_url

    ydl_opts = {
        'format': 'best',
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)

        best_format = next((f for f in info_dict['formats'] if f['format_id'] == info_dict['format_id']), None)

        if best_format:
            download_url = best_format['url']
            return download_url
        else:
            raise NotImplementedError("No suitable format found for download")
        
        
def get_video_thumbnail(video_url):
    if not "youtube.com" in video_url:
        video_url = "https://www.youtube.com/watch?v=" + video_url

    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
        "username": "oauth2",
        "password": ""
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        
        thumbnail_url = info_dict.get('thumbnail')
        
        if thumbnail_url:
            return thumbnail_url
        else:
            raise NotImplementedError("No thumbnail found for the video")