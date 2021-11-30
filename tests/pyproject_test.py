from unittest import main, mock, IsolatedAsyncioTestCase
from main import PyProject
from test_cases import (save_artist_test_cases,
                        get_tracks_by_album_id_test_cases,
                        search_artist_test_cases,
                        get_album_by_artist_id_test_cases,
                        search_artists_test_cases,
                        delete_artist_test_cases,
                        show_artists_test_cases,
                        )
from tests.mocks import MockApi, MockStorage


class TestPyProject(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.c = PyProject

    async def test_show_artists(self) -> None:
        for test in show_artists_test_cases:
            app = PyProject(MockApi(), MockStorage(data=test['mocks'][0]))

            if test['expected_raise']:
                with self.assertRaises(Exception):
                    await app.show_artists()
            else:
                got = await app.show_artists()

                self.assertTrue(test['expected_output'], list)
                self.assertTrue(got, list)

    @mock.patch('builtins.input')
    async def test_delete_artist(self, m_input) -> None:
        for test in delete_artist_test_cases:
            app = PyProject(MockApi(), MockStorage(test['mocks'][0]))
            m_input.return_value = test['input']

            if test['expected_raise']:
                with self.assertRaises(IndexError):
                    await app.delete_artist()
            else:
                got = await app.delete_artist()

                self.assertEqual(got, test['expected_output'])

    @mock.patch('main.PyProject.save_artist')
    @mock.patch('main.PyProject.get_tracks_by_allbum_id')
    @mock.patch('main.PyProject.get_album_by_artist_id')
    @mock.patch('main.PyProject.search_artist')
    @mock.patch('builtins.input')
    async def test_search_artists(self, m_input,  m_search_artist, m_get_album_by_artist_id,
                                  m_get_tracks_by_allbum_id, m_save_artist) -> None:
        for test in search_artists_test_cases:
            app = PyProject(MockApi(), MockStorage())

            m_input.side_effect = test['input']
            m_search_artist.return_value = test['mocks'][0]
            m_get_album_by_artist_id.return_value = test['mocks'][1]
            m_get_tracks_by_allbum_id.return_value = test['mocks'][2]
            m_save_artist.return_value = True

            if test['expected_raise']:
                with self.assertRaises(Exception):
                    await app.search_artists()
            else:
                got = await app.search_artists()

                self.assertEqual(got, test['expected_output'])

    async def test_search_artist(self):
        for test in search_artist_test_cases:
            app = PyProject(MockApi(test['mocks'][0]), MockStorage())

            if test['expected_raise']:
                self.assertRaises(Exception, app.search_artist, test['input'])
            else:
                got = await app.search_artist(artist_name=test['input'])

                self.assertEqual(got, test['expected_output'])

    async def test_get_album_by_artist_id(self):
        for test in get_album_by_artist_id_test_cases:
            app = PyProject(MockApi(test['mocks'][0]), MockStorage())

            if test['expected_raise']:
                self.assertRaises(Exception, app.get_album_by_artist_id, test['input'])
            else:
                got = await app.get_album_by_artist_id(artist_id=test['input'])

                self.assertEqual(got, test['expected_output'])

    async def test_get_tracks_by_allbum_id(self):
        for test in get_tracks_by_album_id_test_cases:
            app = PyProject(MockApi(test['mocks'][0]), MockStorage())

            if test['expected_raise']:
                self.assertRaises(Exception, app.get_tracks_by_allbum_id, test['input'])
            else:
                got = await app.get_tracks_by_allbum_id(album_id=test['input'])

                self.assertEqual(got, test['expected_output'])

    def test_save_artist(self):
        for test in save_artist_test_cases:
            app = PyProject(MockApi(test['mocks'][0]), MockStorage(True))

            if test['expected_raise']:
                self.assertRaises(Exception, app.save_artist, test['input'])
            else:
                got = app.save_artist(test['input'])

                self.assertEqual(got, test['expected_output'])


if __name__ == '__main__':
    main()
