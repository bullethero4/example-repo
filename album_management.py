# task 1 
# album_management.py


# designing a class called Album
class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        # Note: order is album_name, number_of_songs, album_artist
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
        
    def __str__(self): 
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
    
    def __repr__(self):
        # Makes printing a list of albums look clean
        return self.__str__()

def display_albums(albums):
    """Display a list of Album objects."""
    for album in albums:
        print(album)

def sort_number_of_songs(albums):
    """Sort a list of albums by number of songs in ascending order
    and display it.
    Args:
        albums (list): The list of Album objects to sort by number of songs.
    """
    albums.sort(key=lambda album: album.number_of_songs)
    print("\nAlbums sorted by number of songs:")
    display_albums(albums)

def swap_positions(albums, position1, position2):
    """Swap two albums in a list based on their positions
    and display the result.

    Args:
        albums (list): The list of Album objects.
        position1 (int): The position of the first album to swap.
        position2 (int): The position of the second album to swap.
    """
    # Convert 1-based positions to 0-based indices
    albums[position1 - 1], albums[position2 - 1] = (
        albums[position2 - 1],
        albums[position1 - 1],
    )
    print(f"\nAlbums after swapping positions {position1} and {position2}:")
    display_albums(albums)

def find_index(albums, album_name):
    """Find and display the index of a specific album in a list.

    Args:
        albums (list): The list of Album objects to search.
        album_name (str): The name of the album to find.
    """
    for index, album in enumerate(albums):
        if album.album_name == album_name:
            print(f"\nIndex of '{album_name}' in the list: {index}")
            return index
    print(f"\n'{album_name}' not found in the list.")
    return -1

# Create albums1 with 5 Album objects
albums1 = [
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("Abbey Road", 17, "The Beatles"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("21", 11, "Adele")
]

print("Album 1:")
display_albums(albums1)

# Sort by number_of_songs
sort_number_of_songs(albums1)

# Swap position 1 and position 2 (indices 0 and 1)
swap_positions(albums1, 1, 2)

# Create albums2 with 5 Album objects
albums2 = [
    Album("Led Zeppelin IV", 8, "Led Zeppelin"),
    Album("The Wall", 26, "Pink Floyd"),
    Album("Nevermind", 12, "Nirvana"),
    Album("1989", 13, "Taylor Swift"),
    Album("Bad", 11, "Michael Jackson")
]

print("\nAlbum 2:")
display_albums(albums2)

# Copy all albums from albums1 into albums2
albums2.extend(albums1)
print("\nAlbum 2 after copying Album 1 into it:")
display_albums(albums2)

# Add two more albums to albums2
albums2.extend([
    Album("Dark Side of the Moon", 9, "Pink Floyd"),
    Album("Oops!. I Did It Again", 16, "Britney Spears")
])

# Sort albums2 alphabetically by album name
albums2.sort(key=lambda album: album.album_name.lower())
print("\nAlbum 2 sorted alphabetically:")
display_albums(albums2)

# Search for 'Dark Side of the Moon' and print index
find_index(albums2, "Dark Side of the Moon")