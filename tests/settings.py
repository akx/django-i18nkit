SECRET_KEY = 'x'
USE_I18N = True
INSTALLED_APPS = [
    'i18nkit',
    'testdata',
]
TEMPLATES = [
    {
        'NAME': 'default',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

try:
    import django_jinja
    TEMPLATES.insert(0, {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
        }
    })
except ImportError:
    pass
