import re
from io import BytesIO

from babel.messages.extract import extract_python
from django.utils.encoding import force_text
from django.utils.translation import templatize


def django_extract(fileobj, keywords, comment_tags, options):
    src = force_text(fileobj.read())
    src = templatize(src, origin='')
    if 'gettext(' in src:
        src = re.sub(r'\n\s+', '\n', src)  # Remove indentation
        return extract_python(BytesIO(src.encode('utf8')), keywords, comment_tags, options)
    return ()
