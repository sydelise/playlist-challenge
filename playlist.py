# playlist.py

SONGS = [
    ("Imagine", "John Lennon"),
    ("Blinding Lights", "The Weeknd"),
    ("Viva La Vida", "Coldplay"),
]

def print_playlist(songs):
    print("My Playlist")
    for number, (title, artist) in enumerate(songs, start=1):
        print(f"{number}. {title} - {artist}")
    print(f"Total songs: {len(songs)}")

if __name__ == "__main__":
    print_playlist(SONGS)