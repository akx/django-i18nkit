import os

from babel.messages.pofile import read_po
from django.core.management import call_command

import pytest
from tests.utils import repo_root


@pytest.mark.parametrize('noop', (False, True))
def test_import_command(settings, tmpdir, noop):
    settings.LANGUAGES = [('en', 'en'), ('fi', 'fi'), ('sv', 'sv'), ('fr', 'fr')]
    root = str(tmpdir.join('locales'))

    template = os.path.join(root, '{locale}.po')
    call_command(
        'ik_import',
        input=os.path.join(repo_root, 'testdata', 'import.xlsx'),
        output_template=(template if not noop else None),
    )
    for language in ('fi', 'sv', 'fr'):
        filename = template.replace('{locale}', language)
        if noop:
            assert not os.path.exists(filename)
            continue

        with open(filename, 'rb') as infp:
            catalog = read_po(infp)
            assert len(catalog) == 1
            assert catalog.get('Hello').string != 'Hello'
