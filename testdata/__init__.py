from django.utils.translation import ngettext_lazy as ngettext
from django.utils.translation import ugettext_lazy as _

_('Ohai!')
ngettext('I have %s monkey.', 'I have %s monkeys.', 13)
