import os

ALBUM_FIELD = "ALBUM: "
ARTIST_FIELD = "ARTIST: "
URL_FIELD = "URL: "
SEPARATOR_FIELD = "SEPARATOR: "
FORMAT_FIELD = "FORMAT: "
TIME_TITLE_TYPE = "TIME->TITLE"
TITLE_TIME_TYPE = "TITLE->TIME"


class SongsInfoReader:
    track_list_file = ""

    def __init__(self, track_list_file: str):
        self.track_list_file = track_list_file

        self.youtube_link = ""
        self.artist = ""
        self.album = ""
        self.separator = ""
        self.is_format_time_title = True
        self.directory = ""
        self.song_info_list = []

    def read(self):
        with open(self.track_list_file, "r") as file:

            try:
                self.youtube_link = file.readline().split(URL_FIELD)[1].strip("\n")
                self.artist = file.readline().split(ARTIST_FIELD)[1].strip("\n")
                self.album = file.readline().split(ALBUM_FIELD)[1].strip("\n")
                self.separator = file.readline().split(SEPARATOR_FIELD)[1].strip("\n").strip("\"")

                format_time_title = file.readline().split(FORMAT_FIELD)[1].strip("\n")
                if format_time_title != TIME_TITLE_TYPE and format_time_title != TITLE_TIME_TYPE:
                    raise ValueError
                self.is_format_time_title = format_time_title == TIME_TITLE_TYPE

            except (ValueError, IndexError):
                raise ValueError("Invalid header input")

            self.directory = os.path.dirname(os.path.realpath(__file__)) + "/" + self.artist + " - " + self.album

            file.readline()

            lines = file.readlines()
            for item in lines:
                param1, param2 = item.strip("\n").split(self.separator)
                if self.is_format_time_title:
                    time = param1
                    title = param2
                else:
                    time = param2
                    title = param1

                self.song_info_list.append(SongInfo(title, time))

            if len(self.song_info_list) == 0:
                raise ValueError("Invalid songs information input")

            for index, item in enumerate(self.song_info_list):
                if isinstance(item, list) and len(item) != 2:
                    raise ValueError("Invalid songs information input for {} at index {}".format(item, index))


class SongInfo:
    def __init__(self, title: str, time: str):
        self.title = title
        self.time = time
