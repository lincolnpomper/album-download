import os
import yt_dlp
import pydub
from pydub import AudioSegment

from songs_info_reader import SongsInfoReader
from songs_info_reader import SongInfo


class AlbumDownload:

    songs_info: SongsInfoReader

    def __init__(self, temp_file_name: str, track_list_file: str):
        self.temp_file_name = temp_file_name
        self.track_list_file = track_list_file

    def run(self):
        self.songs_info = SongsInfoReader(self.track_list_file)
        self.songs_info.read()

        self.download_video(self.temp_file_name, self.songs_info.youtube_link)
        mp3_file_all_songs = self.read_mp4_audio_segment(self.temp_file_name)
        self.create_destination_folder(self.songs_info.directory)
        self.export_all_songs(self.songs_info, mp3_file_all_songs)
        self.delete_temporary_file(self.temp_file_name)

    @staticmethod
    def download_video(temp_file_name: str, youtube_link: str):

        file_exists = os.path.isfile(temp_file_name)

        if not file_exists:
            print("Downloading video {}. this will take a while".format(youtube_link))
            parameters = {
                "outtmpl": temp_file_name,
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]",
                "verbose": True
            }
            with yt_dlp.YoutubeDL(parameters) as fileDownloader:
                fileDownloader.download([youtube_link])

        if file_exists:
            print("Skipping download the video, file already exists {}".format(temp_file_name))

    @staticmethod
    def read_mp4_audio_segment(temp_file_name: str):

        print("Reading local mp4 file")
        mp3_file = pydub.AudioSegment.from_file(temp_file_name, "mp4")
        return mp3_file

    @staticmethod
    def create_destination_folder(directory):
        if not os.path.exists(directory):
            os.mkdir(directory)

    def export_all_songs(self, songs_info_reader: SongsInfoReader, mp3_file_all_songs: AudioSegment):

        print("Exporting all songs")
        quantity_songs = len(songs_info_reader.song_info_list) - 1

        for index in range(len(songs_info_reader.song_info_list)):
            not_last_song = index != quantity_songs
            current_song_information = songs_info_reader.song_info_list[index]
            next_song_information = songs_info_reader.song_info_list[index + 1] if not_last_song else None

            song = self.extract_song(mp3_file_all_songs, current_song_information, next_song_information,
                                     not_last_song)

            self.export_song(current_song_information, index, song, songs_info_reader)

    def extract_song(self, mp3_file_all_songs, current_info: SongInfo, next_info: SongInfo, not_last_song):

        print("Extracting audio from time {}".format(current_info.time))
        time_start = self.time_to_milliseconds(current_info.time)
        if not_last_song:
            time_finish = self.time_to_milliseconds(next_info.time)
        else:
            time_finish = -1
        song = mp3_file_all_songs[time_start:time_finish]

        return song

    @staticmethod
    def time_to_milliseconds(time_str: str):

        if len(time_str.split(":")) == 2:
            m, s = time_str.split(':')
            return (int(m) * 60 + int(s)) * 1000
        else:
            h, m, s = time_str.split(':')
            return (int(h) * 3600 + int(m) * 60 + int(s)) * 1000

    @staticmethod
    def export_song(current_song_information: SongInfo, index, song, songs_info: SongsInfoReader):

        number_str = str(index + 1)
        quantity = len(songs_info.song_info_list)
        title = current_song_information.title
        tags = {"artist": songs_info.artist, "album": songs_info.album, "title": title, "track": index + 1}

        track_number_two_digits = number_str.zfill(2)
        file_name = "{} - {}.mp3".format(track_number_two_digits, title)

        print("Exporting song {} of {}: {}".format(number_str, quantity, current_song_information.title))
        song.export(os.path.join(songs_info.directory, file_name), format="mp3", tags=tags, id3v2_version="3")

    @staticmethod
    def delete_temporary_file(temp_file_name: str):
        print("Deleting temporary file {}".format(temp_file_name))
        os.remove(temp_file_name)
