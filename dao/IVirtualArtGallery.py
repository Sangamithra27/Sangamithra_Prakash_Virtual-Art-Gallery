from abc import ABC, abstractmethod
from typing import List
from entity.artwork import Artwork

class IVirtualArtGallery(ABC):
    @abstractmethod
    def add_artwork(self, artwork):
        pass

    @abstractmethod
    def add_artist(self, artist):
        pass

    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def add_gallery(self, gallery):
        pass

    @abstractmethod
    def update_artwork(self, artwork):
        pass

    @abstractmethod
    def delete_artwork(self, artwork_id):
        pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        pass

    @abstractmethod
    def search_artworks(self, search_term: str) -> List[Artwork]:
        pass

    @abstractmethod
    def add_artwork_to_favorite(self, user_id, artwork_id):
        pass

    @abstractmethod
    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        pass

