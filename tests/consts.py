try:
    import django_jinja
except ImportError:
    django_jinja = None

REGULAR_MESSAGES_IN_PY_FILES = 1
REGULAR_MESSAGES_IN_DJANGO_FILES = 4
REGULAR_MESSAGES_IN_JINJA2_FILES = 2

PLURAL_MESSAGES_IN_PY_FILES = 1
PLURAL_MESSAGES_IN_DJANGO_FILES = 1
PLURAL_MESSAGES_IN_JINJA2_FILES = 2

EXPECTED_REGULAR_MESSAGES = sum([
    REGULAR_MESSAGES_IN_PY_FILES,
    REGULAR_MESSAGES_IN_DJANGO_FILES,
    (REGULAR_MESSAGES_IN_JINJA2_FILES if django_jinja else 0),
])

EXPECTED_PLURAL_MESSAGES = sum([
    PLURAL_MESSAGES_IN_PY_FILES,
    PLURAL_MESSAGES_IN_DJANGO_FILES,
    (PLURAL_MESSAGES_IN_JINJA2_FILES if django_jinja else 0),
])
