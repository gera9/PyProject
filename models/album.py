from .track import Track


class Album(object):
    def __init__(
        self,
        album_id: str,
        album_name: str,
        album_rating: str,
        album_release_date: str,
        artist_id: str,
        artist_name: str,
        album_coverart: str,
        tracks: list[Track],
    ) -> None:
        self.album_id = album_id
        self.album_name = album_name
        self.album_rating = album_rating
        self.album_release_date = album_release_date
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.album_coverart = album_coverart
        self.tracks = tracks
