from abc import ABC, abstractmethod
from models.artist import Artist
from pymongo import MongoClient
from helpers.util import artist_to_dict, dict_to_artist
from config import Config


class Storage(ABC):
    @abstractmethod
    def save(self, artist: Artist) -> bool:
        pass

    @abstractmethod
    def delete(self, artist_id: int) -> bool:
        pass

    @abstractmethod
    def update(self, update_filter: dict, artist: Artist) -> bool:
        pass

    @abstractmethod
    def get_one(self, get_one_filter: dict) -> Artist:
        pass

    @abstractmethod
    def get_all(self) -> list[Artist]:
        pass


class MongoStorage(Storage):
    """MongoDB connection class."""

    def __init__(self, config: Config, db_name: str = '', collection_name: str = '') -> None:
        self.__uri = config.MONGO_URI
        self.__db_name = db_name
        self.__collection_name = collection_name
        self.__connection = MongoClient(self.__uri)[self.__db_name][self.__collection_name]

    def save(self, artist: Artist) -> bool:
        return bool(self.__connection.insert_one(artist_to_dict(artist)).inserted_id)

    def delete(self, artist_id: int) -> bool:
        return bool(self.__connection.delete_one(filter={'artist_id': artist_id}).deleted_count)

    def update(self, update_filter: dict, artist: Artist) -> bool:
        # Values to be updated.
        new_values = {"$set": artist_to_dict(artist)}
        return bool(self.__connection.update_one(update_filter, new_values))

    def get_one(self, get_one_filter: dict) -> Artist | None:
        artist = self.__connection.find_one(filter=get_one_filter)
        if not artist:
            return None

        return dict_to_artist(artist)

    def get_all(self) -> list[Artist]:
        return [dict_to_artist(artist) for artist in self.__connection.find({})]
