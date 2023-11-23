from django.apps import AppConfig
import os

print(os.getenv("test"))

if os.path.exists("env.py"):
    import env

print(os.getenv("envpy_test"))


class SocialMediaLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_media_log'
