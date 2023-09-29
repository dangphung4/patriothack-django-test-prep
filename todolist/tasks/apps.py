from django.apps import AppConfig

# Model: Represents a database table and is used to interact with the table.
# View: Contains the logic to handle requests and responses. It interacts with models and templates to display data to the user or accept data from the user.
# Template: An HTML file that displays data. It can incorporate dynamic data, which gets filled in at runtime.
# URL Dispatcher: Directs web requests to the appropriate view based on the request URL.
# Admin Site: A built-in Django feature that provides a web-based interface to manage database records easily.
# Migrations: These are files that Django generates to create or change database tables schematically. The migrate command applies these migrations to the database.

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
