# Khai báo biến danh sách toàn cục
songs = []
def main():
    print("Chào mừng đến với chương trình quản lý playlist!")
    print("1. Hiển thị danh sách bài hát")
    print("2. Thêm bài hát")
    print("3. Thoát")
# Danh sách bài hát toàn cục
songs = []
def add_song(title, artist, duration):
    song = {
        'title': title,
        'artist': artist,
        'duration': duration
    }
    songs.append(song)
    print(f"Đã thêm bài hát: {title} - {artist} ({duration} giây)")
add_song("Lạc Trôi", "Sơn Tùng MTP", 240)
# Xem danh sách phát
def view_playlist():
    if not songs:
        print("Danh sách phát trống.")
    else:
        print("Danh sách phát:")
        for i, song in enumerate(songs, 1):
            print(f"{i}. {song['title']} - {song['artist']} ({song['duration']} giây)")