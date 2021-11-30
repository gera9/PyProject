import asyncio

from api.musixmatch_api import MusixmatchApi, Musixmatch
from config import configs
from errors.custom_errors import ArtistNotFound, AlbumNotFound
from helpers.util import artist_to_dict
from models.album import Album
from models.artist import Artist
from models.track import Track
from mongo.storage import Storage, MongoStorage


class PyProject(object):
    def __init__(self, api: MusixmatchApi, storage: Storage) -> None:
        self.api = api
        self.storage = storage

    async def delete_artist(self) -> str:
        artists = self.storage.get_all()
        for i in range(len(artists)):
            print(f'{i+1}.- {artists[i].__dict__}')

        artist_selected = int(input('Which one do you want to delete? '))
        if len(artists) < artist_selected <= 0:
            raise IndexError

        result = self.storage.delete(artists[artist_selected-1].__dict__['artist_id'])
        if not result:
            return 'Error!'

        return 'Done!'

    async def show_artists(self) -> list[Artist]:
        return self.storage.get_all()

    async def search_artists(self) -> str:
        artist_name = input('Type the artist name: ')

        artists = await self.search_artist(artist_name=artist_name)
        if not artists:
            raise ArtistNotFound

        artists_id = []
        for i in range(len(artists)):
            print('{}.- {}'.format(i + 1, artists[i]['artist']['artist_name']))
            artists_id.append(artists[i]['artist']['artist_id'])

        artist_selected = input('Select one artist: ')
        if len(artists_id) < int(artist_selected) <= 0:
            raise AlbumNotFound

        albums = await self.get_album_by_artist_id(artist_id=artists_id[int(artist_selected) - 1])

        albums_id = []
        for i in range(len(albums)):
            print('{}.- {}'.format(i + 1, albums[i]['album']['album_name']))
            albums_id.append(albums[i]['album']['album_id'])

        album_selected = input('Select one album: ')
        if len(albums_id) < int(album_selected) <= 0:
            raise IndexError

        tracks = await self.get_tracks_by_allbum_id(album_id=albums_id[int(album_selected) - 1])

        print('The tracks are: ')
        for i in range(len(tracks)):
            print('{}.- {}'.format(i + 1, tracks[i]['track']['track_name']))

        input('Type y/Y to continue: ')

        track_objects = []
        for track in tracks:
            track_objects.append(
                Track(
                    track_id=track['track']['track_id'],
                    track_name=track['track']['track_name'],
                    album_id=track['track']['album_id'],
                    album_name=track['track']['album_name'],
                    artist_id=track['track']['artist_id'],
                    artist_name=track['track']['artist_name'],
                    track_share_url=track['track']['track_share_url'],
                    track_rating=track['track']['track_rating'],
                )
            )

        album = Album(
                album_id=albums[int(album_selected) - 1]['album']['album_id'],
                album_name=albums[int(album_selected) - 1]['album']['album_name'],
                album_rating=albums[int(album_selected) - 1]['album']['album_rating'],
                album_release_date=albums[int(album_selected) - 1]['album']['album_release_date'],
                artist_id=albums[int(album_selected) - 1]['album']['artist_id'],
                artist_name=albums[int(album_selected) - 1]['album']['artist_name'],
                album_coverart='None',
                tracks=track_objects,
            )

        artist = artist_to_dict(Artist(
            artist_id=artists[int(artist_selected) - 1]['artist']['artist_id'],
            artist_name=artists[int(artist_selected) - 1]['artist']['artist_name'],
            artist_country=artists[int(artist_selected) - 1]['artist']['artist_country'],
            artist_rating=artists[int(artist_selected) - 1]['artist']['artist_rating'],
            artist_twitter_url=artists[int(artist_selected) - 1]['artist']['artist_twitter_url'],
            updated_time=artists[int(artist_selected) - 1]['artist']['updated_time'],
            albums=[album],
        ))

        print('Do you want to save this artist? ')
        print(artist)

        if input('Type y/N to continue: ') == ('n', 'N', 'no', 'NO'):
            return 'Done!'

        if self.save_artist(artist):
            return 'Done!'

        return 'Error!'

    def save_artist(self, artist: Artist) -> bool:
        return self.storage.save(artist=artist)

    async def search_artist(self, artist_name: str) -> list[dict]:
        return self.api.search_artist(artist_name=artist_name, page_size=5)

    async def get_album_by_artist_id(self, artist_id: int) -> list:
        return self.api.get_album_by_artist_id(artist_id=artist_id)

    async def get_tracks_by_allbum_id(self, album_id: int) -> list | None:
        return self.api.get_tracks_by_album(album_id=album_id, page=1, page_size=5)


async def menu(app: PyProject) -> None:
    while True:
        print(
            'Menu:\n1.- Search an artist from Musixmatch\n2.- Show my saved artists\n3.- Delete one of my saved '
            'artists\n4.- Exit\n')

        u_selection = int(input('-> '))

        if u_selection == 1:
                result = await app.search_artists()
                print(result)
        elif u_selection == 2:
            artists = await app.show_artists()
            for i in range(len(artists)):
                print(f'{i+1}.- {artists[i].__dict__}')
        elif u_selection == 3:
            result = await app.delete_artist()
            print(result)
        else:
            return


def main() -> None:
    config = configs['default']
    storage = MongoStorage(config=config, db_name='test', collection_name='test_collection')
    api = Musixmatch(config)

    app = PyProject(api=api, storage=storage)
    asyncio.run(menu(app))


if __name__ == '__main__':
    main()
