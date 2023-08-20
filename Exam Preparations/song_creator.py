def add_songs(*data):
    songs = {}
    output = ""

    for song_lyrics in data:
        song = song_lyrics[0]
        lyrics = song_lyrics[1]
        if song in songs:
            songs[song] += lyrics
        else:
            songs[song] = lyrics

    for key, value in songs.items():
        all_lyrics = "\n".join(value)
        current_song = key

        if all_lyrics:
            output += f"- {current_song}\n{all_lyrics}\n"
        else:
            output += f"- {current_song}\n"

    return output





print(add_songs(
            ("Love of my life",
             ["Love of my life, you've hurt me",
              "You've broken my heart, and now you leave me",
              "Love of my life, can't you see?",
              "Bring it back, bring it back"]),
            ("Beat It", []),
            ("Love of my life",
             ["Don't take it away from me",
              "Because you don't know",
              "What it means to me"]),
            ("Dream On",
             ["Every time that I look in the mirror"]),
        ))
#
#         self.assertEqual(result.strip(), """- Love of my life
# Love of my life, you've hurt me
# You've broken my heart, and now you leave me
# Love of my life, can't you see?
# Bring it back, bring it back
# Don't take it away from me
# Because you don't know
# What it means to me
# - Beat It
# - Dream On
# Every time that I look in the mirror""")

