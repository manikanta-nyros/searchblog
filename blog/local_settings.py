
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "380c9756-1511-45e9-ad61-0f4d639d3743920fe574-c587-4cfb-85be-e1d62f307b158e09350e-e8cc-4b83-9003-e007755636bf"
NEVERCACHE_KEY = "e956a60c-165f-4720-bafb-da0822943682c5daea54-2784-45a1-a1c0-010bdc6fcf3e8863450b-3c7b-43c6-9363-87a318debafc"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "/home/nyros/manikanta/manikanta/Python/Django/django_haystack/searchproject/db.sqlite3",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
