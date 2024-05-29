class Gallery:
    def __init__(self, gallery_id=None, name=None, description=None, location=None, curator=None, opening_hours=None):
        self.__gallery_id = gallery_id
        self.__name = name
        self.__description = description
        self.__location = location
        self.__curator = curator
        self.__opening_hours = opening_hours

    def get_gallery_id(self):
        return self.__gallery_id

    def set_gallery_id(self, gallery_id):
        self.__gallery_id = gallery_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_curator(self):
        return self.__curator

    def set_curator(self, curator):
        self.__curator = curator

    def get_opening_hours(self):
        return self.__opening_hours

    def set_opening_hours(self, opening_hours):
        self.__opening_hours = opening_hours
