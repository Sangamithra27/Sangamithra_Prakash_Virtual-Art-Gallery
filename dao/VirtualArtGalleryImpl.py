from util.db_connection import DBConnection
from entity.artwork import Artwork
from entity.Gallery import Gallery
from typing import List
from exception.UserNotFoundException import UserException
from exception.UserNotFoundException import DateFormatException
import datetime

class CrimeAnalysisService:
    connection = None

    def __init__(self):
        self.connection = DBConnection.get_connection()

    def add_artwork(self, artwork):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Artwork (title, description, creationdate, medium, imageurl) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (artwork.get_title(), artwork.get_description(), artwork.get_creation_date(), artwork.get_medium(), artwork.get_image_url()))
            self.connection.commit()
            print("Artwork added")
            return True
        except Exception as e:
            print("Error adding artwork", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def add_artist(self, artist):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Artist (name, biography, birthdate, nationality, website, contactinformation) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
            artist.get_name(), artist.get_biography(), artist.get_birth_date(), artist.get_nationality(),
            artist.get_website(), artist.get_contact_info()))
            self.connection.commit()
            print("Artist added")
        except Exception as e:
            print("Error adding artist", e)
            self.connection.rollback()
        finally:
            cursor.close()

    def add_user(self, user):
        cursor = None
        try:

            date_of_birth = user.get_date_of_birth()
            try:
                datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
            except ValueError:
                raise DateFormatException("Date format must be YYYY-MM-DD")

            cursor = self.connection.cursor()
            query = "INSERT INTO User (username, password, email, firstname, lastname, dateofbirth, profilepicture) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
            user.get_username(), user.get_password(), user.get_email(), user.get_first_name(), user.get_last_name(),
            user.get_date_of_birth(), user.get_profile_picture()))
            self.connection.commit()
            print("User added")
        except (UserException, DateFormatException, Exception) as e:
            print("Error adding user", e)
            self.connection.rollback()

        finally:
            if cursor:
                cursor.close()

    def add_gallery(self, gallery):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Gallery (name, description, location, curator, openinghours) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (
            gallery.get_name(), gallery.get_description(), gallery.get_location(), gallery.get_curator(),
            gallery.get_opening_hours()))
            self.connection.commit()
            print("Gallery added")
            return True
        except Exception as e:
            print("Error adding gallery", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    # Update Artwork
    def update_artwork(self, artwork):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Artwork SET Title = %s, Description = %s, Creationdate = %s, Medium = %s, Imageurl = %s WHERE artworkid = %s"
            cursor.execute(query, (artwork.get_title(), artwork.get_description(), artwork.get_creation_date(), artwork.get_medium(), artwork.get_image_url(), artwork.get_artwork_id()))
            self.connection.commit()
            print("Artwork updated")
            return True
        except Exception as e:
            print("Error updating artwork", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def update_gallery(self, gallery):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Gallery SET name = %s, description = %s, location = %s, curator = %s, openinghours = %s WHERE GalleryID = %s"
            cursor.execute(query, (
                gallery.get_name(), gallery.get_description(), gallery.get_location(), gallery.get_curator(),
                gallery.get_opening_hours(), gallery.get_gallery_id()))
            self.connection.commit()
            print("Gallery updated")
            return True
        except Exception as e:
            print("Error updating gallery", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def delete_gallery(self, gallery_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Gallery WHERE GalleryID = %s"
            cursor.execute(query, (gallery_id,))
            self.connection.commit()
            print("Gallery deleted")
            return True
        except Exception as e:
            print("Error deleting gallery", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def delete_artwork(self, artwork_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Artwork WHERE artworkid = %s"
            cursor.execute(query, (artwork_id,))
            self.connection.commit()
            print("Artwork deleted")
            return True
        except Exception as e:
            print("Error deleting artwork", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()


    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Artwork WHERE artworkid = %s"  # Adjusted field name here
            cursor.execute(query, (artwork_id,))
            artwork_data = cursor.fetchone()
            if artwork_data:
                artwork = Artwork(
                    artwork_data['ArtworkID'],  # Adjusted field name here
                    artwork_data['Title'],
                    artwork_data['Description'],
                    artwork_data['CreationDate'],
                    artwork_data['Medium'],
                    artwork_data['ImageURL']
                )
                return artwork
            else:
                print("Artwork not found.")
                return None
        except Exception as e:
            print("Error retrieving artwork:", e)
            return None
        finally:
            cursor.close()

    def search_artworks(self, search_term: str) -> List[Artwork]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Artwork WHERE Title LIKE %s OR Medium LIKE %s"
            cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
            artworks_data = cursor.fetchall()
            artworks = []
            for artwork_data in artworks_data:
                artwork = Artwork(
                    artwork_data['ArtworkID'],
                    artwork_data['Title'],
                    artwork_data['Description'],
                    artwork_data['CreationDate'],
                    artwork_data['Medium'],
                    artwork_data['ImageURL']
                )
                artworks.append(artwork)
            return artworks
        except Exception as e:
            print("Error searching artworks:", e)
            return []
        finally:
            cursor.close()

    def search_galleries(self, search_term: str) -> List[Gallery]:
        cursor=None
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Gallery WHERE Name LIKE %s OR Description LIKE %s"
            cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
            galleries_data = cursor.fetchall()
            galleries = []
            for gallery_data in galleries_data:
                gallery = Gallery(
                    gallery_data['GalleryID'],
                    gallery_data['Name'],
                    gallery_data['Description'],
                    gallery_data['Location'],
                    gallery_data['Curator'],
                    gallery_data['OpeningHours']
                )
                galleries.append(gallery)
            return galleries
        except Exception as e:
            print("Error searching galleries:", e)
            return []
        finally:
            cursor.close()

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO User_Favorite_Artwork (UserID, ArtworkID) VALUES (%s, %s)"
            cursor.execute(query, (user_id, artwork_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error adding artwork to favorites:", e)
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM User_Favorite_Artwork WHERE UserID = %s AND ArtworkID = %s"
            cursor.execute(query, (user_id, artwork_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error removing artwork from favorites:", e)
            return False
        finally:
            cursor.close()

