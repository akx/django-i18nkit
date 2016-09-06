import pytest
from django.utils import translation
from django.utils.translation import npgettext, pgettext

from i18nkit import poison


@pytest.mark.parametrize('function', [
    'gettext',
    'ugettext',
])
def test_regular_poison_works(function):
    function = getattr(translation, function)
    with poison.override():
        assert function('hello') != 'hello'
    assert function('hello') == 'hello'


@pytest.mark.parametrize('function', [
    'ngettext',
    'ungettext',
])
@pytest.mark.parametrize('number', [0, 1, 2])
def test_n_poison_works(function, number):
    function = getattr(translation, function)
    with poison.override():
        assert not function('hello', 'hullo', number).startswith('h')
    assert function('hello', 'hullo', number).startswith('h')


def test_context_poison_works():
    with poison.override():
        assert pgettext('blah', 'hello') != 'hello'
        assert not npgettext('blah', 'hello', 'hullo', 42).startswith('h')


@pytest.mark.parametrize('format_string, formattee', [
    ('Hi, %(name)s', {'name': 'friend'}),
    ('Hi, %s!', ('friend',)),
    ('Many percent signs! %%%%%d%%', (8)),
    ('Hola, {}!', 'friend'),
    ('Hola, {}{}!', ('friend', 5)),
    ('Hola, {name}!', {'name': 'friend'}),
])
def test_poisoned_strings_remain_formattable(format_string, formattee):
    poisoned_format_string = poison.poison_string(format_string)
    if '%' in format_string:
        assert poisoned_format_string % formattee
    else:
        if isinstance(formattee, dict):
            assert poisoned_format_string.format(**formattee)
        else:
            assert poisoned_format_string.format(*formattee)
