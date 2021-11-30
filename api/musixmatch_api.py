from abc import ABC, abstractmethod
from helpers.util import slugify
from config import Config
import requests


class MusixmatchApi(ABC):
    @abstractmethod
    def search_track(self, track_name: str, artist_name: str) -> list[dict] | None:
        pass

    @abstractmethod
    def search_artist(self, artist_name: str, page_size: int) -> list[dict] | None:
        pass

    @abstractmethod
    def get_album_by_artist_id(self, artist_id: int) -> list[dict] | None:
        pass

    @abstractmethod
    def get_tracks_by_album(self, album_id: int, page: int, page_size: int) -> list[dict] | None:
        pass


class Musixmatch(MusixmatchApi):
    def __init__(self, config: Config):
        self.config = config

    def search_track(self, track_name: str, artist_name: str) -> list[dict] | None:
        """Search a track by name and track name and, then, returns a json."""

        url = '{}track.search?q_artist={}&q_track=trains&page_size=3&page=1&s_track_rating=desc&apikey={}'.format(
            self.config.API_ROOT_URL, artist_name, self.config.API_KEY
        )
        tracks = requests.get(url).json()

        if not tracks['message']['body']:
            return None

        return tracks['message']['body']['track_list']

    def search_artist(self, artist_name: str, page_size: int) -> list[dict] | None:
        """Search an artist by name and, then, returns a json list."""

        url = '{}artist.search?q_artist={}&page_size={}&apikey={}'.format(
            self.config.API_ROOT_URL, slugify(artist_name), page_size, self.config.API_KEY
        )
        artists = requests.get(url).json()

        if not artists['message']['body']:
            return None

        return artists['message']['body']['artist_list']

    def get_album_by_artist_id(self, artist_id: int) -> list[dict] | None:
        """Get an artist by id and, then, returns a json."""

        url = '{}artist.albums.get?artist_id={}&s_release_date=desc&g_album_name=1&apikey={}'.format(
            self.config.API_ROOT_URL, artist_id, self.config.API_KEY
        )
        albums = requests.get(url).json()

        if not albums['message']['body']:
            return None

        return albums['message']['body']['album_list']

    def get_tracks_by_album(self, album_id: int, page: int, page_size: int) -> list[dict] | None:
        """Get tracks by album_id and, then, returns a json list."""

        url = '{}album.tracks.get?album_id={}&page={}&page_size={}&apikey={}'.format(
            self.config.API_ROOT_URL, album_id, page, page_size, self.config.API_KEY
        )
        tracks = requests.get(url).json()

        if not tracks['message']['body']:
            return None

        return tracks['message']['body']['track_list']
