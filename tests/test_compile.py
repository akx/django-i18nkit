import os

from django.core.management import call_command

from tests.utils import repo_root


def test_export_command():
    call_command(
        'ik_compile',
        dir_children=[repo_root]
    )
    assert os.path.isfile(os.path.join(repo_root, 'testdata', 'foo.mo'))
