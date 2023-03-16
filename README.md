## Music collection downloader

This software downloads music from YouTube and convert to the content into mp3 splitting in several files based on input.

It should be used on long videos containing full albums or collections of music when in the description or comments it is available the beginning of each track. This information must be placed in a text file named `songs-info-input.txt` and placed on the same folder as this script.

The structure of the input is as follows:
 - `URL`: YouTube link
 - `ARTIST`: Artist
 - `ALBUM`: Album or collection name
 - `SEPARATOR`: This is what lies between the title and time and will be inserted in double quotes.
 - `FORMAT`: The format of the lines that contains song and time information. Must be one of the following:
   - `TIME->TITLE` or `TITLE->TIME`
     - The time is the starting time of the current song. Each element of time part must be separated by *":"* and can have two or three elements: minutes and seconds or hour, minutes and seconds.
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

**Examples:**
- Example 1
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

- Example 2
```
URL: https://www.youtube.com/watch?v=PSv37HwwojU
ARTIST: SimCity
ALBUM: SimCity 4
SEPARATOR: " - "
FORMAT: TITLE->TIME

Bumper to Bumper - 0:00:00
The Morning Commute - 0:07:10
Wheels of Progress - 0:11:53
Deserted - 0:17:54
Metropolis - 0:23:05
ElectriCITY - 0:28:10
Floating Population - 0:33:22
Chain Reaction - 0:38:35
Rush Hour - 0:44:53
By The Bay - 0:50:14
The New Hood - 0:56:20
No Gridlock - 1:01:37
Re-Development - 1:09:00
Bohemian Street Jam - 1:14:31
Urban Underground - 1:20:12
Street Sweeper - 1:25:18
```