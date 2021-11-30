from collections import namedtuple
from models.artist import Artist
from models.track import Track


def artist_to_dict(artist: Artist) -> dict:
    if isinstance(artist, (dict, list)):
        return artist

    for i in range(len(artist.albums)):
        for j in range(len(artist.albums[i].tracks)):
            artist.albums[i].tracks[j] = vars(artist.albums[i].tracks[j])
        artist.albums[i] = vars(artist.albums[i])

    return vars(artist)


def dict_to_artist(artist: dict) -> Artist:
    if isinstance(artist, Artist):
        return artist

    for i in range(len(artist['albums'])):
        for j in range(len(artist['albums'][i]['tracks'])):
            artist['albums'][i]['tracks'][j] = namedtuple(
                'Track', artist['albums'][i]['tracks'][j].keys()
            )(
                *artist['albums'][i]['tracks'][j].values()
            )
        artist['albums'][i] = namedtuple(
            'Album', artist['albums'][i].keys()
        )(
            *artist['albums'][i].values()
        )

    return Artist(
        artist_id=artist['artist_id'],
        artist_name=artist['artist_name'],
        artist_country=artist['artist_country'],
        artist_rating=artist['artist_rating'],
        artist_twitter_url=artist['artist_twitter_url'],
        updated_time=artist['updated_time'],
        albums=artist['albums']
    )


def slugify(text: str) -> str:
    return text.replace(' ', '-')
