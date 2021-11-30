import os


class Config(object):
    MONGO_URI = ''
    API_ROOT_URL = 'https://api.musixmatch.com/ws/1.1/'
    API_KEY = os.getenv('API_KEY') or '219443a8c934ba42eef1d50c72a3b725'


class DevelopmentConfig(Config):
    DATABASE_NAME = 'test'
    COLLECTION_NAME = 'test_collection'
    MONGO_URI = os.getenv('MONGO_URI') or 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false'


class ProductionConfig(Config):
    pass


configs = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,

    'default': DevelopmentConfig,
}
