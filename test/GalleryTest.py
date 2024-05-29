import unittest
from unittest.mock import MagicMock
from dao.VirtualArtGalleryImpl import CrimeAnalysisService
from entity.Gallery import Gallery

class TestGalleryManagement(unittest.TestCase):
    def setUp(self):
        self.service = CrimeAnalysisService()

    def test_create_gallery_success(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.return_value = None
        gallery = Gallery(name="Test Gallery", description="Test Description", location="Test Location",
                          curator="Test Curator", opening_hours="Test Opening Hours")
        result = self.service.add_gallery(gallery)
        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_create_gallery_failure(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")
        gallery = Gallery(name="Test Gallery", description="Test Description", location="Test Location",
                          curator="Test Curator", opening_hours="Test Opening Hours")
        result = self.service.add_gallery(gallery)
        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_update_gallery_success(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.return_value = None
        gallery_id = 1
        updated_gallery = Gallery(gallery_id=gallery_id, name="Updated Gallery", description="Updated Description",
                                  location="Updated Location", curator="Updated Curator",
                                  opening_hours="Updated Opening Hours")
        result = self.service.update_gallery(updated_gallery)
        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_update_gallery_failure(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")
        gallery_id = 1
        updated_gallery = Gallery(gallery_id=gallery_id, name="Updated Gallery", description="Updated Description",
                                  location="Updated Location", curator="Updated Curator",
                                  opening_hours="Updated Opening Hours")
        result = self.service.update_gallery(updated_gallery)
        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_remove_gallery_success(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.return_value = None
        gallery_id = 1
        result = self.service.delete_gallery(gallery_id)
        self.assertTrue(result)
        cursor_mock.execute.assert_called_once()

    def test_remove_gallery_failure(self):
        self.service.connection = MagicMock()
        cursor_mock = self.service.connection.cursor.return_value
        cursor_mock.execute.side_effect = Exception("Mocked DB Error")
        gallery_id = 1
        result = self.service.delete_gallery(gallery_id)
        self.assertFalse(result)
        cursor_mock.execute.assert_called_once()

    def test_search_galleries_success(self):
        mock_cursor = MagicMock()
        self.service.connection.cursor = MagicMock(return_value=mock_cursor)
        mock_cursor.fetchall.return_value = [
            {'GalleryID': 1, 'Name': 'Gallery',
             'Description': 'A gallery featuring impressionist artworks', 'Location': '1st Floor', 'Curator': 1,
             'OpeningHours': '9 AM - 5 PM'},
            {'GalleryID': 2, 'Name': 'Renaissance', 'Description': 'A gallery featuring renaissance artworks',
             'Location': '2nd Floor', 'Curator': 2, 'OpeningHours': '10 AM - 6 PM'}
        ]
        search_term = "Gallery"
        galleries = self.service.search_galleries(search_term)
        self.assertEqual(len(galleries), 2)
        self.assertEqual(galleries[0].get_name(), 'Gallery')
        self.assertEqual(galleries[1].get_name(), 'Renaissance')
        print("Retrieved Galleries:")
        for gallery in galleries:
            print(gallery)

if __name__ == '__main__':
    unittest.main()
