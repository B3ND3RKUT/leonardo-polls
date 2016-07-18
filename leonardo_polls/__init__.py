
from django.apps import AppConfig

default_app_config = 'leonardo_polls.Config'


LEONARDO_APPS = ['leonardo_polls']


class Config(AppConfig):
    name = 'leonardo_polls'
    verbose_name = "leonardo-polls"
