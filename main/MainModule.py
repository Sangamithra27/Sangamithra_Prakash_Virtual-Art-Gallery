from dao.VirtualArtGalleryImpl import CrimeAnalysisService
from entity.Artist import Artist
from entity.User import User
from entity.Gallery import Gallery
from dao.IVirtualArtGallery import *
class MainModule:
    @staticmethod
    def get_artwork_details():
        title = input("Enter artwork title: ")
        description = input("Enter artwork description: ")
        creation_date = input("Enter artwork creation date: ")
        medium = input("Enter artwork medium: ")
        image_url = input("Enter artwork image URL: ")
        artwork = Artwork()
        artwork.set_title(title)
        artwork.set_description(description)
        artwork.set_creation_date(creation_date)
        artwork.set_medium(medium)
        artwork.set_image_url(image_url)
        return artwork
    @staticmethod
    def get_artist_details():
        name = input("Enter artist name: ")
        biography = input("Enter artist biography: ")
        birth_date = input("Enter artist birth date: ")
        nationality = input("Enter artist nationality: ")
        website = input("Enter artist website: ")
        contact_info = input("Enter artist contact information: ")
        artist = Artist()
        artist.set_name(name)
        artist.set_biography(biography)
        artist.set_birth_date(birth_date)
        artist.set_nationality(nationality)
        artist.set_website(website)
        artist.set_contact_info(contact_info)
        return artist
    @staticmethod
    def get_user_details():
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth: ")
        profile_picture = input("Enter profile picture URL: ")
        user = User()
        user.set_username(username)
        user.set_password(password)
        user.set_email(email)
        user.set_first_name(first_name)
        user.set_last_name(last_name)
        user.set_date_of_birth(date_of_birth)
        user.set_profile_picture(profile_picture)
        return user
    @staticmethod
    def get_gallery_details():
        name = input("Enter gallery name: ")
        description = input("Enter gallery description: ")
        location = input("Enter gallery location: ")
        curator = input("Enter curator ID: ")
        opening_hours = input("Enter opening hours: ")
        gallery = Gallery()
        gallery.set_name(name)
        gallery.set_description(description)
        gallery.set_location(location)
        gallery.set_curator(curator)
        gallery.set_opening_hours(opening_hours)
        return gallery
    @staticmethod
    def main():
        # Create an instance of the service implementation
        service = CrimeAnalysisService()
        while True:
            # Display menu options
            print("\nMenu:")
            print("1. Add Artwork")
            print("2. Add Artist")
            print("3. Add User")
            print("4. Add Gallery")
            print("5. Update Artwork")
            print("6. Delete Artwork")
            print("7. Get Artwork By Id")
            print("8. Search Artworks")
            print("9. Add Artwork To Favorite")
            print("10.Remove Artwork From Favorite")
            print("11.Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                artwork = MainModule.get_artwork_details()
                service.add_artwork(artwork)

            elif choice == '2':
                artist = MainModule.get_artist_details()
                service.add_artist(artist)

            elif choice == '3':
                user = MainModule.get_user_details()
                service.add_user(user)

            elif choice == '4':
                gallery = MainModule.get_gallery_details()
                service.add_gallery(gallery)

            elif choice == '5':
                        # Update Artwork
                        artwork_id = input("Enter artwork ID to update: ")
                        artwork = service.get_artwork_by_id(artwork_id)
                        if artwork:
                            print("Enter new details for the artwork:")
                            new_title = input("Enter new title: ")
                            new_description = input("Enter new description: ")
                            new_creation_date = input("Enter new creation date: ")
                            new_medium = input("Enter new medium: ")
                            new_image_url = input("Enter new image URL: ")
                            new_artwork = Artwork(artwork_id, new_title, new_description, new_creation_date, new_medium,
                                                  new_image_url)
                            service.update_artwork(new_artwork)

            elif choice == '6':
                    artwork_id = input("Enter artwork ID to delete: ")
                    service.delete_artwork(artwork_id)

            elif choice == '7':
                artwork_id = input("Enter artwork ID: ")
                artwork = service.get_artwork_by_id(artwork_id)
                if artwork:
                      print("Artwork found:")
                      print(artwork)
                else:
                      print("Artwork not found.")

            elif choice == '8':
                search_term = input("Enter search term: ")
                artworks = service.search_artworks(search_term)
                if artworks:
                    print("Search results:")
                    for artwork in artworks:
                        print(artwork)
                else:
                    print("No artworks found matching the search term.")

            elif choice == '9':
                user_id = input("Enter your user ID: ")
                artwork_id = input("Enter artwork ID to add to favorites: ")
                success = service.add_artwork_to_favorite(int(user_id), int(artwork_id))
                if success:
                    print("Artwork added to favorites successfully.")
                else:
                    print("Failed to add artwork to favorites.")

            elif choice == '10':
                user_id = input("Enter your user ID: ")
                artwork_id = input("Enter artwork ID to remove from favorites: ")
                success = service.remove_artwork_from_favorite(int(user_id), int(artwork_id))
                if success:
                    print("Artwork removed from favorites successfully.")
                else:
                    print("Failed to remove artwork from favorites.")

            elif choice == '11':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    MainModule.main()