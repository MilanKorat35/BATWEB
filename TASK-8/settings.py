# mysite/settings.py

INSTALLED_APPS = [
    # ...
    'authentication',
]

# ...

TEMPLATES = [
    {
        # ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # ...
    },
]
