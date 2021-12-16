
from download_youtube_album import AlbumDownload

if __name__ == '__main__':

    temp_file_name = "tmp.mp4"
    track_list_file = "songs-info-input.txt"

    album_download = AlbumDownload(temp_file_name, track_list_file)
    album_download.run()
