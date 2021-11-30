class Track(object):
    def __init__(
        self,
        track_id: str,
        track_name: str,
        album_id: str,
        album_name: str,
        artist_id: str,
        artist_name: str,
        track_share_url: str,
        track_rating: str,
    ) -> None:
        self.track_id = track_id
        self.track_name = track_name
        self.album_id = album_id
        self.album_name = album_name
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.track_share_url = track_share_url
        self.track_rating = track_rating
