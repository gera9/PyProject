from .album import Album


class Artist(object):
    def __init__(
        self,
        artist_id: str,
        artist_name: str,
        artist_country: str,
        artist_rating: str,
        artist_twitter_url: str,
        updated_time: str,
        albums: list[Album]
    ) -> None:
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.artist_country = artist_country
        self.artist_rating = artist_rating
        self.artist_twitter_url = artist_twitter_url
        self.updated_time = updated_time
        self.albums = albums
