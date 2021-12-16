import unittest
import os
from unittest.mock import MagicMock
from download_youtube_album import AlbumDownload


class AlbumDownloadTest(unittest.TestCase):
    TEMP_FILE_NAME = "test/tmp.mp4"
    TRACK_LIST_FILE = "test/input-test.txt"

    def test_download(self):
        album_download = AlbumDownload(self.TEMP_FILE_NAME, self.TRACK_LIST_FILE)
        album_download.delete_temporary_file = MagicMock()

        album_download.run()

        self.assertEqual(album_download.temp_file_name, self.TEMP_FILE_NAME)

        self.assertTrue(len(album_download.songs_info.song_info_list) == 3)

        for index, item in enumerate(album_download.songs_info.song_info_list):
            number_str = str(index + 1)
            track_number_two_digits = number_str.zfill(2)
            file_name = track_number_two_digits + " - " + item.title + ".mp3"

            full_file_name = album_download.songs_info.directory + "/" + file_name

            self.assertTrue(os.path.exists(full_file_name))


if __name__ == '__main__':
    unittest.main()
