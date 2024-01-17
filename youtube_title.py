from pytube import Playlist

def get_playlist_title(url):
    try:
        playlist = Playlist(url)
        return playlist.title
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
playlist_url = "https://www.youtube.com/playlist?list=PLULWS_YViqGuOa1F5oiUE9npeDuuw604U"
url = str(input("\nspecify you playlist url\n"))
title = get_playlist_title(url)

if title:
    print(f"The playlist title is: {title}")