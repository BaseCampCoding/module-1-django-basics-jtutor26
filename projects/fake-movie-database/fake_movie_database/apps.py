from django.apps import AppConfig


class FakeMovieDatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_movie_database'
