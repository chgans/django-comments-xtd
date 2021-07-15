import os
import sys


my_plugins = [
    "django_comments_xtd.tests.pytest_fixtures.base",
]


def pytest_configure(config):
    os.chdir("django_comments_xtd")
    sys.path.insert(0, os.getcwd())
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"

    import django
    django.setup()

    # -------------------------------------
    # Load fixtures listed in 'my_plugins'.

    for plugin_module in my_plugins:
        config.pluginmanager.import_plugin(plugin_module)