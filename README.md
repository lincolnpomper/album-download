## Music collection downloader

This software downloads music from YouTube and convert to the content into mp3 splitting in several files based on input.

It should be used on long videos containing full albums or collections of music when in the description or comments it is available the beginning of each track. This information must be placed in a text file named `songs-info-input.txt` and placed on the same folder as this script.

The structure of the input is as follows:
 - `URL`: YouTube link
 - `ARTIST`: Artist
 - `ALBUM`: Album or collection name
 - `SEPARATOR`: This is what lies between the title and time, will be inserted in double quotes: "*SEPARATOR*"
 - `FORMAT`: The format of the lines that contains song and time information. Must be one of the following:
   - `TIME->TITLE` or `TIME->TITLE`
     - The time is the starting time of the current song.
 - And the body: 
    ```
    TIME SEPARATOR TITLE
    TIME SEPARATOR TITLE
    ...
    or
    TITLE SEPARATOR TIME
    TITLE SEPARATOR TIME
    ...
    ```

**Example:**
```
URL: https://www.youtube.com/watch?v=Hkz4SB6wJBM
ARTIST: Animal Crossing
ALBUM: Animal Crossing - Relaxing Music with Soft Rain
SEPARATOR: " - "
FORMAT: TIME->TITLE
00:00 - 2 AM ~ City Folk
02:32 - 1 AM ~ New Leaf
04:41 - Rainy Day ~ Animal Crossing GCN
```
