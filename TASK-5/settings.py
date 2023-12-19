# myresume/settings.py

INSTALLED_APPS = [
    # ... other apps
    'resumeapp',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        # ... other settings
    },
]

