from helpers.util import artist_to_dict, dict_to_artist
from models.album import Album
from models.artist import Artist
from models.track import Track

delete_artist_test_cases = [
    {
        'name': 'Case 1 successfull',
        'input': 1,
        'mocks': [
            [
                Artist(
                    artist_id=8274,
                    artist_name='Porcupine Tree',
                    artist_country='GB',
                    artist_rating=59,
                    artist_twitter_url='',
                    updated_time='2017-01-04T17:32:49Z',
                    albums=[
                        Album(
                            album_id=36941774,
                            album_name='Trains (Remastered) - Single',
                            album_rating=0,
                            album_release_date='2020-02-19',
                            artist_id=8274,
                            artist_name='Porcupine Tree',
                            album_coverart='None',
                            tracks=[
                                Track(
                                 track_id=193285536, track_name='Trains (Remastered)', album_id=36941774, album_name='Trains (Remastered) - Single', artist_id=8274,
                                 artist_name='Porcupine Tree', track_share_url='https://www.musixmatch.com/lyrics/Porcupine-Tree/Trains-Remastered?utm_source=application&utm_campaign=api&utm_medium=None%3A1409622073710', track_rating=21
                                )
                            ]
                        ),
                    ],
                )
            ],

        ],
        'expected_raise': False,
        'expected_output': 'Done!'
    },
    {
        'name': 'Case 1 successfull',
        'input': 10,
        'mocks': [
            [
                Artist(
                    artist_id=8274,
                    artist_name='Porcupine Tree',
                    artist_country='GB',
                    artist_rating=59,
                    artist_twitter_url='',
                    updated_time='2017-01-04T17:32:49Z',
                    albums=[
                        Album(
                            album_id=36941774,
                            album_name='Trains (Remastered) - Single',
                            album_rating=0,
                            album_release_date='2020-02-19',
                            artist_id=8274,
                            artist_name='Porcupine Tree',
                            album_coverart='None',
                            tracks=[
                                Track(
                                    track_id=193285536, track_name='Trains (Remastered)', album_id=36941774,
                                    album_name='Trains (Remastered) - Single', artist_id=8274,
                                    artist_name='Porcupine Tree',
                                    track_share_url='https://www.musixmatch.com/lyrics/Porcupine-Tree/Trains-Remastered?utm_source=application&utm_campaign=api&utm_medium=None%3A1409622073710',
                                    track_rating=21
                                )
                            ]
                        ),
                    ],
                )
            ],

        ],
        'expected_raise': True,
        'expected_output': 'Done!'
    }
]

search_artist_test_cases = [
    {
        'name': 'Case 1 successful',
        'input': 'Coldplay',
        'mocks':  [
            {
                "artist": {
                    "artist_id": 13774235,
                    "artist_mbid": "4a4ee089-93b1-4470-af9a-6ff575d32704",
                    "artist_name": 'Coldplay',
                    "artist_country": "GB",
                    "artist_alias_list": [
                        {
                            "artist_alias": "The Prodigy Vs. The Prodigy"
                        },
                        {
                            "artist_alias": "Prodigy"
                        },
                        {
                            "artist_alias": "Prodigy, the"
                        },
                        {
                            "artist_alias": "Prodigy, The"
                        }
                    ],
                    "artist_rating": 51,
                    "artist_twitter_url": "http:\/\/twitter.com\/THE_PRODIGY",
                    "updated_time": "2011-06-15T10:23:33Z"
                }
            },
        ],
        'expected_raise': False,
        'expected_output':
            {
                "artist": {
                    "artist_id": 13774235,
                    "artist_mbid": "4a4ee089-93b1-4470-af9a-6ff575d32704",
                    "artist_name": 'Coldplay',
                    "artist_country": "GB",
                    "artist_alias_list": [
                        {
                            "artist_alias": "The Prodigy Vs. The Prodigy"
                        },
                        {
                            "artist_alias": "Prodigy"
                        },
                        {
                            "artist_alias": "Prodigy, the"
                        },
                        {
                            "artist_alias": "Prodigy, The"
                        }
                    ],
                    "artist_rating": 51,
                    "artist_twitter_url": "http:\/\/twitter.com\/THE_PRODIGY",
                    "updated_time": "2011-06-15T10:23:33Z"
                }
            },

    }
]

get_album_by_artist_id_test_cases = [
    {
        'name': 'Case 1 successful',
        'input': 123,
        'mocks': [
            [
                {
                    "album": {
                        "album_id": 11339785,
                        "album_mbid": None,
                        "album_name": "Atlas (From \"The Hunger Games: Catching Fire\" Soundtrack)",
                        "album_rating": 0,
                        "album_track_count": 1,
                        "album_release_date": "2013-09-06",
                        "album_release_type": "Single",
                        "artist_id": 123,
                        "artist_name": "Coldplay",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 1166,
                                        "music_genre_parent_id": 16,
                                        "music_genre_name": "Musicals",
                                        "music_genre_name_extended": "Soundtrack \/ Musicals"
                                    }
                                }
                            ]
                        },
                        "secondary_genres": {
                            "music_genre_list": [

                            ]
                        },
                        "album_pline": "2013 Parlophone Records Ltd. under exclusive license to Republic Records, a Division of UMG Recordings, Inc.",
                        "album_copyright": "2013 Parlophone Records Ltd. under exclusive license to Republic Records, a Division of UMG Recordings, Inc.",
                        "album_label": "Hunger Games 2\/Catching Fire",
                        "updated_time": "2013-09-26T16:05:44Z",
                        "album_coverart_100x100": "http:\/\/static.musixmatch.com\/images\/albums\/7\/3\/5\/4\/1\/5\/26514537.jpg",
                    }
                },
            ],
        ],
        'expected_raise': False,
        'expected_output': [
            {
                "album": {
                    "album_id": 11339785,
                    "album_mbid": None,
                    "album_name": "Atlas (From \"The Hunger Games: Catching Fire\" Soundtrack)",
                    "album_rating": 0,
                    "album_track_count": 1,
                    "album_release_date": "2013-09-06",
                    "album_release_type": "Single",
                    "artist_id": 123,
                    "artist_name": "Coldplay",
                    "primary_genres": {
                        "music_genre_list": [
                            {
                                "music_genre": {
                                    "music_genre_id": 1166,
                                    "music_genre_parent_id": 16,
                                    "music_genre_name": "Musicals",
                                    "music_genre_name_extended": "Soundtrack \/ Musicals"
                                }
                            }
                        ]
                    },
                    "secondary_genres": {
                        "music_genre_list": [

                        ]
                    },
                    "album_pline": "2013 Parlophone Records Ltd. under exclusive license to Republic Records, a Division of UMG Recordings, Inc.",
                    "album_copyright": "2013 Parlophone Records Ltd. under exclusive license to Republic Records, a Division of UMG Recordings, Inc.",
                    "album_label": "Hunger Games 2\/Catching Fire",
                    "updated_time": "2013-09-26T16:05:44Z",
                    "album_coverart_100x100": "http:\/\/static.musixmatch.com\/images\/albums\/7\/3\/5\/4\/1\/5\/26514537.jpg",
                }
            },
        ]
    }
]

get_tracks_by_album_id_test_cases = [
    {
        'name': 'Case 1 successful',
        'input': 456,
        'mocks': [
            [{
                "track": {
                    "track_id": 15268687,
                    "track_mbid": "fb81a071-9c63-4e8c-ab60-77403e81c01d",
                    "track_length": 137,
                    "lyrics_id": 6291316,
                    "instrumental": 0,
                    "subtitle_id": 0,
                    "track_name": "Don't Panic",
                    "track_rating": 100,
                    "album_name": "Parachutes",
                    "album_id": 456,
                    "artist_id": 1039,
                    "album_coverart_100x100": "http:\/\/api.musixmatch.com\/images\/albums\/5\/9\/6\/5\/7\/4\/11475695.jpg",
                    "artist_mbid": "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
                    "artist_name": "Coldplay",
                    "updated_time": "2012-05-31T06:00:22Z"
                }
            }],
        ],
        'expected_raise': False,
        'expected_output': [
            {
                "track": {
                    "track_id": 15268687,
                    "track_mbid": "fb81a071-9c63-4e8c-ab60-77403e81c01d",
                    "track_length": 137,
                    "lyrics_id": 6291316,
                    "instrumental": 0,
                    "subtitle_id": 0,
                    "track_name": "Don't Panic",
                    "track_rating": 100,
                    "album_name": "Parachutes",
                    "album_id": 456,
                    "artist_id": 1039,
                    "album_coverart_100x100": "http:\/\/api.musixmatch.com\/images\/albums\/5\/9\/6\/5\/7\/4\/11475695.jpg",
                    "artist_mbid": "cc197bad-dc9c-440d-a5b5-d52ba2e14234",
                    "artist_name": "Coldplay",
                    "updated_time": "2012-05-31T06:00:22Z"
                },
            }
        ]
    },
]

save_artist_test_cases = [
    {
        'name': 'Case 1 successful',
        'mocks': [True],
        'input': Artist(
            artist_id="",
            artist_name="",
            artist_country="",
            artist_rating="",
            artist_twitter_url="",
            updated_time="",
            albums=[],
        ),
        'expected_raise': False,
        'expected_output': True,
    }
]

search_artists_test_cases = [
    {
        'name': 'Case 1 successful',
        'input': ['Porcupine Tree', 1, 5, 'y', 'y'],
        'expected_raise': False,
        'mocks': [
            [{'artist': {'artist_id': 8274, 'artist_name': 'Porcupine Tree', 'artist_name_translation_list': [],
                         'artist_comment': '', 'artist_country': 'GB', 'artist_alias_list': [], 'artist_rating': 59,
                         'artist_twitter_url': '', 'artist_credits': {'artist_list': []}, 'restricted': 0,
                         'updated_time': '2017-01-04T17:32:49Z', 'begin_date_year': '1987', 'begin_date': '1987-00-00',
                         'end_date_year': '2010', 'end_date': '2010-00-00'}}, {
                'artist': {'artist_id': 26075264, 'artist_name': 'Yoko Ono & Porcupine Tree',
                           'artist_name_translation_list': [
                               {'artist_name_translation': {'language': 'EN', 'translation': 'Porcupine Tree'}}],
                           'artist_comment': '', 'artist_country': '',
                           'artist_alias_list': [{'artist_alias': 'Porcupine Tree'}], 'artist_rating': 6,
                           'artist_twitter_url': '', 'artist_credits': {'artist_list': [{'artist': {'artist_id': 37216,
                                                                                                    'artist_name': 'Yoko Ono',
                                                                                                    'artist_name_translation_list': [
                                                                                                        {
                                                                                                            'artist_name_translation': {
                                                                                                                'language': 'JA',
                                                                                                                'translation': 'オノ・ヨーコ'}}],
                                                                                                    'artist_comment': '',
                                                                                                    'artist_country': 'US',
                                                                                                    'artist_alias_list': [
                                                                                                        {
                                                                                                            'artist_alias': 'オノ・ヨーコ'},
                                                                                                        {
                                                                                                            'artist_alias': 'Ono'}],
                                                                                                    'artist_rating': 37,
                                                                                                    'artist_twitter_url': 'https://twitter.com/yokoono',
                                                                                                    'artist_credits': {
                                                                                                        'artist_list': []},
                                                                                                    'restricted': 0,
                                                                                                    'updated_time': '2014-06-18T02:08:40Z',
                                                                                                    'begin_date_year': '1933',
                                                                                                    'begin_date': '1933-02-18',
                                                                                                    'end_date_year': '',
                                                                                                    'end_date': '0000-00-00'}},
                                                                                        {'artist': {'artist_id': 8274,
                                                                                                    'artist_name': 'Porcupine Tree',
                                                                                                    'artist_name_translation_list': [],
                                                                                                    'artist_comment': '',
                                                                                                    'artist_country': 'GB',
                                                                                                    'artist_alias_list': [],
                                                                                                    'artist_rating': 59,
                                                                                                    'artist_twitter_url': '',
                                                                                                    'artist_credits': {
                                                                                                        'artist_list': []},
                                                                                                    'restricted': 0,
                                                                                                    'updated_time': '2017-01-04T17:32:49Z',
                                                                                                    'begin_date_year': '1987',
                                                                                                    'begin_date': '1987-00-00',
                                                                                                    'end_date_year': '2010',
                                                                                                    'end_date': '2010-00-00'}}]},
                           'restricted': 0, 'updated_time': '2014-01-24T11:01:57Z', 'begin_date_year': '',
                           'begin_date': '0000-00-00', 'end_date_year': '', 'end_date': '0000-00-00'}}, {
                'artist': {'artist_id': 34333925, 'artist_name': 'Wilson feat. Porcupine Tree',
                           'artist_name_translation_list': [], 'artist_comment': '', 'artist_country': '',
                           'artist_alias_list': [], 'artist_rating': 15, 'artist_twitter_url': '', 'artist_credits': {
                               'artist_list': [{'artist': {'artist_id': 24457026, 'artist_name': 'Wilson',
                                                           'artist_name_translation_list': [{'artist_name_translation': {
                                                               'language': 'ZH', 'translation': 'WILSON'}}],
                                                           'artist_comment': '', 'artist_country': 'GB',
                                                           'artist_alias_list': [{'artist_alias': 'うぃるそん'},
                                                                                 {'artist_alias': 'WILSON'}],
                                                           'artist_rating': 33, 'artist_twitter_url': '',
                                                           'artist_credits': {'artist_list': []}, 'restricted': 0,
                                                           'updated_time': '2016-06-30T16:53:07Z', 'begin_date_year': '2012',
                                                           'begin_date': '2012-01-00', 'end_date_year': '',
                                                           'end_date': '0000-00-00'}}, {
                                   'artist': {'artist_id': 8274, 'artist_name': 'Porcupine Tree',
                                               'artist_name_translation_list': [], 'artist_comment': '',
                                               'artist_country': 'GB', 'artist_alias_list': [],
                                               'artist_rating': 59, 'artist_twitter_url': '',
                                               'artist_credits': {'artist_list': []}, 'restricted': 0,
                                               'updated_time': '2017-01-04T17:32:49Z',
                                               'begin_date_year': '1987', 'begin_date': '1987-00-00',
                                               'end_date_year': '2010', 'end_date': '2010-00-00'}}]},
                           'restricted': 0, 'updated_time': '2017-09-11T12:36:33Z', 'begin_date_year': '',
                           'begin_date': '0000-00-00', 'end_date_year': '', 'end_date': '0000-00-00'}}, {
                'artist': {'artist_id': 34333926,
                           'artist_name': 'Wilson feat. Edwin, Maitland, Edwards & Porcupine Tree',
                           'artist_name_translation_list': [], 'artist_comment': '', 'artist_country': '',
                           'artist_alias_list': [], 'artist_rating': 1, 'artist_twitter_url': '', 'artist_credits': {
                               'artist_list': [{'artist': {'artist_id': 24457026, 'artist_name': 'Wilson',
                                                           'artist_name_translation_list': [{'artist_name_translation': {
                                                               'language': 'ZH', 'translation': 'WILSON'}}],
                                                           'artist_comment': '', 'artist_country': 'GB',
                                                           'artist_alias_list': [{'artist_alias': 'うぃるそん'},
                                                                                 {'artist_alias': 'WILSON'}],
                                                           'artist_rating': 33, 'artist_twitter_url': '',
                                                           'artist_credits': {'artist_list': []}, 'restricted': 0,
                                                           'updated_time': '2016-06-30T16:53:07Z', 'begin_date_year': '2012',
                                                           'begin_date': '2012-01-00', 'end_date_year': '',
                                                           'end_date': '0000-00-00'}}, {
                                   'artist': {'artist_id': 16445, 'artist_name': 'Edwin',
                                               'artist_name_translation_list': [], 'artist_comment': '',
                                               'artist_country': 'CA',
                                               'artist_alias_list': [{'artist_alias': 'Edwin Ghazal'}],
                                               'artist_rating': 11, 'artist_twitter_url': '',
                                               'artist_credits': {'artist_list': []}, 'restricted': 0,
                                               'updated_time': '2013-11-05T11:25:25Z',
                                               'begin_date_year': '1968', 'begin_date': '1968-09-09',
                                               'end_date_year': '', 'end_date': '0000-00-00'}}, {
                                   'artist': {'artist_id': 24817630, 'artist_name': 'Maitland',
                                               'artist_name_translation_list': [], 'artist_comment': '',
                                               'artist_country': '', 'artist_alias_list': [],
                                               'artist_rating': 11, 'artist_twitter_url': '',
                                               'artist_credits': {'artist_list': []}, 'restricted': 0,
                                               'updated_time': '2013-11-09T03:30:28Z', 'begin_date_year': '',
                                               'begin_date': '0000-00-00', 'end_date_year': '',
                                               'end_date': '0000-00-00'}}, {
                                   'artist': {'artist_id': 34079823, 'artist_name': 'Edwards',
                                               'artist_name_translation_list': [], 'artist_comment': '',
                                               'artist_country': '', 'artist_alias_list': [],
                                               'artist_rating': 1, 'artist_twitter_url': '',
                                               'artist_credits': {'artist_list': []}, 'restricted': 0,
                                               'updated_time': '2017-08-08T20:47:21Z', 'begin_date_year': '',
                                               'begin_date': '0000-00-00', 'end_date_year': '',
                                               'end_date': '0000-00-00'}}, {
                                   'artist': {'artist_id': 8274, 'artist_name': 'Porcupine Tree',
                                               'artist_name_translation_list': [], 'artist_comment': '',
                                               'artist_country': 'GB', 'artist_alias_list': [],
                                               'artist_rating': 59, 'artist_twitter_url': '',
                                               'artist_credits': {'artist_list': []}, 'restricted': 0,
                                               'updated_time': '2017-01-04T17:32:49Z',
                                               'begin_date_year': '1987', 'begin_date': '1987-00-00',
                                               'end_date_year': '2010', 'end_date': '2010-00-00'}}]},
                           'restricted': 0, 'updated_time': '2017-09-11T12:36:33Z', 'begin_date_year': '',
                           'begin_date': '0000-00-00', 'end_date_year': '', 'end_date': '0000-00-00'}}, {
                'artist': {'artist_id': 31924070, 'artist_name': 'Porcupine Tree', 'artist_name_translation_list': [],
                           'artist_comment': '', 'artist_country': '', 'artist_alias_list': [], 'artist_rating': 1,
                           'artist_twitter_url': '', 'artist_credits': {'artist_list': []}, 'restricted': 0,
                           'updated_time': '2016-06-10T15:22:34Z', 'begin_date_year': '', 'begin_date': '0000-00-00',
                           'end_date_year': '', 'end_date': '0000-00-00'}}],
            [{'album': {'album_id': 48009031, 'album_mbid': '', 'album_name': 'CLOSURE / CONTINUATION',
                        'album_rating': 29, 'album_release_date': '2022-06-24', 'artist_id': 8274,
                        'artist_name': 'Porcupine Tree', 'primary_genres': {'music_genre_list': [{'music_genre': {
                            'music_genre_id': 34, 'music_genre_parent_id': 0, 'music_genre_name': 'Music',
                            'music_genre_name_extended': 'Music', 'music_genre_vanity': 'Music'}}]},
                        'album_pline': '℗ 2021 Sony Music Entertainment UK Ltd under license from Porcupine 3 Ltd',
                        'album_copyright': '℗ 2021 Sony Music Entertainment UK Ltd under license from Porcupine 3 Ltd',
                        'album_label': 'Music For Nations', 'restricted': 0, 'updated_time': '2021-11-14T22:44:42Z',
                        'external_ids': {'spotify': [], 'itunes': ['1592575933'], 'amazon_music': []}}}, {
                'album': {'album_id': 47762519, 'album_mbid': '', 'album_name': 'Harridan', 'album_rating': 51,
                          'album_release_date': '2021-11-01', 'artist_id': 8274, 'artist_name': 'Porcupine Tree',
                          'primary_genres': {'music_genre_list': []},
                          'album_pline': '(P) 2021 Sony Music Entertainment UK Limited under exclusive licence from Porcupine 3 Limited',
                          'album_copyright': '', 'album_label': 'Music For Nations', 'restricted': 0,
                          'updated_time': '2021-11-01T10:25:59Z',
                          'external_ids': {'spotify': ['3vjYPAzHWD2jB3SeIpoAp0'], 'itunes': [], 'amazon_music': []}}},
             {'album': {'album_id': 44887695, 'album_mbid': '',
                        'album_name': 'The Sound of No One Listening (Remastered)', 'album_rating': 28,
                        'album_release_date': '2020-11-20', 'artist_id': 8274, 'artist_name': 'Porcupine Tree',
                        'primary_genres': {'music_genre_list': []}, 'album_pline': '(P) 2020 Snapper Music Ltd',
                        'album_copyright': '(C) 2020 Snapper Music Ltd', 'album_label': 'Kscope', 'restricted': 0,
                        'updated_time': '2021-06-17T03:29:01Z',
                        'external_ids': {'spotify': ['2jn7dMydnJxqJ35Jhe95rp'], 'itunes': [], 'amazon_music': []}}}, {
                 'album': {'album_id': 43766915, 'album_mbid': '', 'album_name': 'Transmission IV', 'album_rating': 16,
                           'album_release_date': '2020-11-20', 'artist_id': 8274, 'artist_name': 'Porcupine Tree',
                           'primary_genres': {'music_genre_list': [{'music_genre': {'music_genre_id': 34,
                                                                                    'music_genre_parent_id': 0,
                                                                                    'music_genre_name': 'Music',
                                                                                    'music_genre_name_extended': 'Music',
                                                                                    'music_genre_vanity': 'Music'}}]},
                           'album_pline': '(P) 2020 Kscope, a division of Snapper Music Ltd',
                           'album_copyright': '(C) 2020 Snapper Music Ltd', 'album_label': 'Kscope', 'restricted': 0,
                           'updated_time': '2021-04-25T05:12:16Z',
                           'external_ids': {'spotify': ['4oQxUXOAEUD8h4vBFgMxfx'], 'itunes': ['1560246334'],
                                            'amazon_music': []}}}, {
                 'album': {'album_id': 36941774, 'album_mbid': '', 'album_name': 'Trains (Remastered) - Single',
                           'album_rating': 0, 'album_release_date': '2020-02-19', 'artist_id': 8274,
                           'artist_name': 'Porcupine Tree', 'primary_genres': {'music_genre_list': [{'music_genre': {
                               'music_genre_id': 34, 'music_genre_parent_id': 0, 'music_genre_name': 'Music',
                               'music_genre_name_extended': 'Music', 'music_genre_vanity': 'Music'}}]},
                           'album_pline': '℗ 2020 Kscope, a division of Snapper Music Ltd',
                           'album_copyright': '℗ 2020 Kscope, a division of Snapper Music Ltd', 'album_label': 'Kscope',
                           'restricted': 0, 'updated_time': '2021-11-14T22:44:42Z',
                           'external_ids': {'spotify': ['0LjIr4pS7hXTKTiDRUf8J1'],
                                            'itunes': ['1496969115', '1573068949'], 'amazon_music': []}}}, {
                 'album': {'album_id': 36699664, 'album_mbid': '', 'album_name': 'Blackest Eyes (Remastered) - Single',
                           'album_rating': 0, 'album_release_date': '2020-02-06', 'artist_id': 8274,
                           'artist_name': 'Porcupine Tree', 'primary_genres': {'music_genre_list': [{'music_genre': {
                               'music_genre_id': 34, 'music_genre_parent_id': 0, 'music_genre_name': 'Music',
                               'music_genre_name_extended': 'Music', 'music_genre_vanity': 'Music'}}]},
                           'album_pline': '℗ 2020 Kscope, a division of Snapper Music Ltd',
                           'album_copyright': '℗ 2020 Kscope, a division of Snapper Music Ltd', 'album_label': 'Kscope',
                           'restricted': 0, 'updated_time': '2021-11-14T22:44:42Z',
                           'external_ids': {'spotify': ['6GEa913Hwxd648929Ab0l7'], 'itunes': ['1573072867'],
                                            'amazon_music': []}}}, {
                 'album': {'album_id': 10302628, 'album_mbid': '10fe0c6a-a079-4163-ba91-8ce02e319cb2',
                           'album_name': 'Stupid Dream', 'album_rating': 44, 'album_release_date': '2014-12-16',
                           'artist_id': 8274, 'artist_name': 'Porcupine Tree', 'primary_genres': {'music_genre_list': [{
                               'music_genre': {
                                   'music_genre_id': 21,
                                   'music_genre_parent_id': 34,
                                   'music_genre_name': 'Rock',
                                   'music_genre_name_extended': 'Rock',
                                   'music_genre_vanity': 'Rock'}}]},
                           'album_pline': '1999 Porcupine Tree Ltd Under Licence To Snapper Music Plc',
                           'album_copyright': '2013 Snapper Music Plc', 'album_label': 'Kscope', 'restricted': 0,
                           'updated_time': '2014-12-22T10:03:08Z',
                           'external_ids': {'spotify': [], 'itunes': ['271495406', '948887431'], 'amazon_music': []}}},
             {'album': {'album_id': 16276745, 'album_mbid': '', 'album_name': '6 Pack of Hits', 'album_rating': 14,
                        'album_release_date': '2013-05-27', 'artist_id': 8274, 'artist_name': 'Porcupine Tree',
                        'primary_genres': {'music_genre_list': [{'music_genre': {'music_genre_id': 21,
                                                                                 'music_genre_parent_id': 34,
                                                                                 'music_genre_name': 'Rock',
                                                                                 'music_genre_name_extended': 'Rock',
                                                                                 'music_genre_vanity': 'Rock'}}]},
                        'album_pline': '2013 Snapper', 'album_copyright': '2013 Snapper', 'album_label': 'Snapper',
                        'restricted': 0, 'updated_time': '2014-01-21T10:51:19Z',
                        'external_ids': {'spotify': [], 'itunes': ['654635934'], 'amazon_music': []}}}, {
                 'album': {'album_id': 16280732, 'album_mbid': '', 'album_name': 'Octane Twisted', 'album_rating': 10,
                           'album_release_date': '2012-11-19', 'artist_id': 8274, 'artist_name': 'Porcupine Tree',
                           'primary_genres': {'music_genre_list': [{'music_genre': {'music_genre_id': 21,
                                                                                    'music_genre_parent_id': 34,
                                                                                    'music_genre_name': 'Rock',
                                                                                    'music_genre_name_extended': 'Rock',
                                                                                    'music_genre_vanity': 'Rock'}}]},
                           'album_pline': '2012 Porcupine Tree Under Exclusive Licence To Kscope',
                           'album_copyright': '2012 Porcupine Tree Ltd', 'album_label': 'Kscope', 'restricted': 0,
                           'updated_time': '2014-01-21T15:32:20Z',
                           'external_ids': {'spotify': [], 'itunes': ['573798538', '684102949'], 'amazon_music': []}}},
             {'album': {'album_id': 10769206, 'album_mbid': '9db58b74-ded7-412a-96c8-fefa167b01b7',
                        'album_name': 'Nil Recurring', 'album_rating': 10, 'album_release_date': '2011-04-01',
                        'artist_id': 8274, 'artist_name': 'Porcupine Tree', 'primary_genres': {'music_genre_list': [{
                            'music_genre': {
                                'music_genre_id': 21,
                                'music_genre_parent_id': 34,
                                'music_genre_name': 'Rock',
                                'music_genre_name_extended': 'Rock',
                                'music_genre_vanity': 'Rock'}}]},
                        'album_pline': '2007 Porcupine Tree Ltd', 'album_copyright': '2010 Porcupine Tree Ltd',
                        'album_label': 'Kscope', 'restricted': 0, 'updated_time': '2016-09-19T08:35:36Z',
                        'external_ids': {'spotify': [], 'itunes': ['371357219', '428190007', '428503543'],
                                         'amazon_music': []}}}],
            [{'track': {'track_id': 193285536, 'track_name': 'Trains (Remastered)', 'track_name_translation_list': [],
                        'track_rating': 21, 'commontrack_id': 107210211, 'instrumental': 0, 'explicit': 0,
                        'has_lyrics': 1, 'has_subtitles': 1, 'has_richsync': 0, 'num_favourite': 2,
                        'album_id': 36941774, 'album_name': 'Trains (Remastered) - Single', 'artist_id': 8274,
                        'artist_name': 'Porcupine Tree',
                        'track_share_url': 'https://www.musixmatch.com/lyrics/Porcupine-Tree/Trains-Remastered?utm_source=application&utm_campaign=api&utm_medium=None%3A1409622073710',
                        'track_edit_url': 'https://www.musixmatch.com/lyrics/Porcupine-Tree/Trains-Remastered/edit?utm_source=application&utm_campaign=api&utm_medium=None%3A1409622073710',
                        'restricted': 0, 'updated_time': '2020-02-28T15:49:23Z', 'primary_genres': {
                'music_genre_list': [{'music_genre': {'music_genre_id': 34, 'music_genre_parent_id': 0,
                                                      'music_genre_name': 'Music',
                                                      'music_genre_name_extended': 'Music',
                                                      'music_genre_vanity': 'Music'}}, {
                        'music_genre': {'music_genre_id': 5, 'music_genre_parent_id': 34,
                                                             'music_genre_name': 'Classical',
                                                             'music_genre_name_extended': 'Classical',
                                                             'music_genre_vanity': 'Classical'}}]}}}]
        ],
        'expected_output': 'Done!'
    },
{
        'name': 'Case 2 ArtistNotFound error',
        'input': ['cdncjds', 1, 5, 'y', 'y'],
        'expected_raise': True,
        'mocks': [[], [], []],
        'expected_output': 'Done!',
    },
{
        'name': 'Case 3 AlbumNotFound error',
        'input': ['PorcupineTree', 1000, 5, 'y', 'y'],
        'expected_raise': True,
        'mocks': [[], [], []],
        'expected_output': 'Done!',
    },
{
        'name': 'Case 4 IndexError error',
        'input': ['PorcupineTree', 1, 500, 'y', 'y'],
        'expected_raise': True,
        'mocks': [[], [], []],
        'expected_output': 'Done!',
    },

]

show_artists_test_cases = [
    {
        'name': 'Case 1 successful',
        'expected_raise': False,
        'expected_output': [

                Artist(
                    artist_id=8274,
                    artist_name='Porcupine Tree',
                    artist_country='GB',
                    artist_rating=59,
                    artist_twitter_url='',
                    updated_time='2017-01-04T17:32:49Z',
                    albums=[
                        Album(
                            album_id=36941774,
                            album_name='Trains (Remastered) - Single',
                            album_rating=0,
                            album_release_date='2020-02-19',
                            artist_id=8274,
                            artist_name='Porcupine Tree',
                            album_coverart='None',
                            tracks=[
                                Track(
                                    track_id=193285536, track_name='Trains (Remastered)', album_id=36941774,
                                    album_name='Trains (Remastered) - Single', artist_id=8274,
                                    artist_name='Porcupine Tree',
                                    track_share_url='https://www.musixmatch.com/lyrics/Porcupine-Tree/Trains-Remastered?utm_source=application&utm_campaign=api&utm_medium=None%3A1409622073710',
                                    track_rating=21
                                )
                            ]
                        ),
                    ],
                )

        ],
        'mocks':[
            [
Artist(
                    artist_id=8274,
                    artist_name='Porcupine Tree',
                    artist_country='GB',
                    artist_rating=59,
                    artist_twitter_url='',
                    updated_time='2017-01-04T17:32:49Z',
                    albums=[
                        Album(
                            album_id=36941774,
                            album_name='Trains (Remastered) - Single',
                            album_rating=0,
                            album_release_date='2020-02-19',
                            artist_id=8274,
                            artist_name='Porcupine Tree',
                            album_coverart='None',
                            tracks=[
                                Track(
                                    track_id=193285536, track_name='Trains (Remastered)', album_id=36941774,
                                    album_name='Trains (Remastered) - Single', artist_id=8274,
                                    artist_name='Porcupine Tree',
                                    track_share_url='https://www.musixmatch.com/lyrics/Porcupine-Tree/Trains-Remastered?utm_source=application&utm_campaign=api&utm_medium=None%3A1409622073710',
                                    track_rating=21
                                )
                            ]
                        ),
                    ],
                )
            ]
        ],
    }
]
