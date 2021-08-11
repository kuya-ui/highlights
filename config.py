import os

class Config:

    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2021-08-11&sortBy=popularity&apiKey=API_KEY'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}