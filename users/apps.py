from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Import app signals in order to the triggers to work
    def ready(self):
        import users.signals
