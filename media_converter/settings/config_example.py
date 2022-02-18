from .base import BASE_DIR

DEBUG = True
SECRET_KEY = "secret_key"
ALLOWED_HOSTS = ["your domen", "127.0.0.1"]
WEBHOOK = ALLOWED_HOSTS[0]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

BOT_TOKEN = "token"
