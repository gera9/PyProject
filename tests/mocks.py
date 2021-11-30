from api.musixmatch_api import MusixmatchApi
from models.artist import Artist
from mongo.storage import Storage


class MockStorage(Storage):
    def __init__(self, data: object = False):
        self.data = data

    def save(self, artist: Artist) -> bool:
        return self.data

    def delete(self, artist: Artist) -> bool:
        return self.data

    def update(self, update_filter: dict, artist: Artist) -> bool:
        return self.data

    def get_one(self, get_one_filter: dict) -> Artist:
        return self.data

    def get_all(self) -> list[Artist]:
        return self.data


class MockApi(MusixmatchApi):
    def __init__(self, data: dict = {}) -> None:
        self.data = data

    def search_track(self, track_name: str = '', artist_name: str = '') -> list[dict]:
        return self.data

    def search_artist(self, artist_name: str, page_size: int = 0) -> list[dict]:
        return self.data

    def get_album_by_artist_id(self, artist_id: int = 0) -> list[dict]:
        return self.data

    def get_tracks_by_album(self, album_id: int = 0, page: int = 0, page_size: int = 0) -> list[dict]:
        return self.data
