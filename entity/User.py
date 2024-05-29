class User:
    def __init__(self, user_id=None, username=None, password=None, email=None, first_name=None, last_name=None, date_of_birth=None, profile_picture=None, favorite_artworks=None):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__profile_picture = profile_picture
        self.__favorite_artworks = favorite_artworks if favorite_artworks is not None else []

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_profile_picture(self):
        return self.__profile_picture

    def set_profile_picture(self, profile_picture):
        self.__profile_picture = profile_picture

    def get_favorite_artworks(self):
        return self.__favorite_artworks

    def set_favorite_artworks(self, favorite_artworks):
        self.__favorite_artworks = favorite_artworks