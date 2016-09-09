from babel.messages.pofile import read_po
from django.core.management import call_command
from tests.consts import EXPECTED_REGULAR_MESSAGES, EXPECTED_PLURAL_MESSAGES

from tests.utils import repo_root


def test_extract_command(tmpdir):
    filename = str(tmpdir.join('out.pot'))
    call_command(
        'ik_extract',
        dir_children=[repo_root],
        output=filename,
    )
    with open(filename, 'rb') as infp:
        assert len(read_po(infp)) == EXPECTED_REGULAR_MESSAGES + EXPECTED_PLURAL_MESSAGES


def test_extract_apps(tmpdir):
    filename = str(tmpdir.join('out.pot'))
    call_command(
        'ik_extract',
        apps=['testdata'],
        output=filename,
        verbosity=2,
    )
    with open(filename, 'rb') as infp:
        assert len(read_po(infp)) == EXPECTED_REGULAR_MESSAGES + EXPECTED_PLURAL_MESSAGES
