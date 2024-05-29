import unittest
from unittest.mock import MagicMock
from dao.VirtualArtGalleryImpl import CrimeAnalysisService
from entity.artwork import Artwork

class TestArtworkManagement(unittest.TestCase):
    def setUp(self):
        self.service = CrimeAnalysisService()

    def test_add_artwork_success(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.return_value = None
        artwork = Artwork(title="Testing", description="Test Description", creation_date="2024-03-31",
                          medium="english", image_url="http://test.jpg")
        result = self.service.add_artwork(artwork)
        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_add_artwork_failure(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")
        artwork = Artwork(title="Testing", description="Test Description", creation_date="2024-03-31",
                          medium="english", image_url="http://test.jpg")
        result = self.service.add_artwork(artwork)
        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_update_artwork_success(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.return_value = None
        updated_artwork = Artwork(artwork_id=1, title="Updated Title", description="Updated Description",
                                  creation_date="2024-05-13", medium="french",
                                  image_url="http://updated_artwork.jpg")
        result = self.service.update_artwork(updated_artwork)
        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_update_artwork_failure(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")
        updated_artwork = Artwork(artwork_id=1, title="Updated Title", description="Updated Description",
                                  creation_date="2024-05-13", medium="french",
                                  image_url="http://updated_artwork.jpg")
        result = self.service.update_artwork(updated_artwork)
        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_remove_artwork_success(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.return_value = None
        artwork_id = 1
        result = self.service.delete_artwork(artwork_id)
        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_remove_artwork_failure(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")
        artwork_id = 1
        result = self.service.delete_artwork(artwork_id)
        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_search_artworks_success(self):
        mock_cursor = MagicMock()
        self.service.connection.cursor = MagicMock(return_value=mock_cursor)
        mock_cursor.fetchall.return_value = [
            {'ArtworkID': 1, 'Title': 'Artwork 1', 'Description': 'Description 1', 'CreationDate': '2024-05-15',
             'Medium': 'Medium 1', 'ImageURL': 'image1.jpg'},
            {'ArtworkID': 2, 'Title': 'Artwork 2', 'Description': 'Description 2', 'CreationDate': '2024-05-16',
             'Medium': 'Medium 2', 'ImageURL': 'image2.jpg'}
        ]
        search_term = "Artwork"
        artworks = self.service.search_artworks(search_term)
        self.assertEqual(len(artworks), 2)
        self.assertEqual(artworks[0].get_title(), 'Artwork 1')
        self.assertEqual(artworks[1].get_title(), 'Artwork 2')
        print("Retrieved Artworks:")
        for artwork in artworks:
            print(artwork)

if __name__ == '__main__':
    unittest.main()

