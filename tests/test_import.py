import os

from django.core.management import call_command

from babel.messages.pofile import read_po
from tests.utils import repo_root


def test_import_command(settings, tmpdir):
    settings.LANGUAGES = [('en', 'en'), ('fi', 'fi'), ('sv', 'sv'), ('fr', 'fr')]
    root = str(tmpdir.join('locales'))

    template = os.path.join(root, '{locale}.po')
    call_command(
        'ik_import',
        input=os.path.join(repo_root, 'testdata', 'import.xlsx'),
        output_template=template,
    )
    for language in ('fi', 'sv', 'fr'):
        filename = template.replace('{locale}', language)

        with open(filename, 'rb') as infp:
            catalog = read_po(infp)
            assert len(catalog) == 1
            assert catalog.get('Hello').string != 'Hello'
