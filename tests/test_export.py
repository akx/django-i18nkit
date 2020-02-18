from django.core.management import call_command

import openpyxl
from tests.consts import EXPECTED_REGULAR_MESSAGES
from tests.utils import repo_root


def test_export_command(settings, tmpdir):
    settings.LANGUAGES = [('en', 'en'), ('fi', 'fi'), ('sv', 'sv'), ('fr', 'fr')]
    pot_filename = str(tmpdir.join('out.pot'))
    xlsx_filename = str(tmpdir.join('out.xlsx'))
    call_command(
        'ik_extract',
        dir_children=[repo_root],
        output=pot_filename,
    )
    call_command(
        'ik_export',
        input=[pot_filename],
        output=xlsx_filename,
    )
    ws = openpyxl.load_workbook(xlsx_filename)
    rows = [[c.value for c in row] for row in list(ws)[0]]
    assert len(rows) == (
        1 +  # Header
        EXPECTED_REGULAR_MESSAGES
    )
