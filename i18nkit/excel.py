import logging

from babel.messages import Catalog
from django.conf import settings
from django.utils import translation

from i18nkit.utils import raise_if_no_module

try:
    import openpyxl
except ImportError:  # pragma: no cover
    openpyxl = None

log = logging.getLogger(__name__)


def write_catalog_workbook(outfp, catalog, languages=None, source_locale=None, prefill=True):
    raise_if_no_module('openpyxl')
    if not languages:
        languages = settings.LANGUAGES
    if not source_locale:
        source_locale = languages[0][0]

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    target_locales = sorted([lc for (lc, name) in languages if lc != source_locale])
    sheet.append([source_locale] + target_locales)
    for message in catalog:
        original = message.id
        if not original:
            continue
        if isinstance(original, tuple):
            log.warning('Unable to represent plural message %s in Excel catalog', message)
            continue
        row = [original]
        if prefill:
            for locale in target_locales:
                with translation.override(locale):
                    translated = translation.gettext(original)
                    row.append(translated if (translated != original) else '')
        sheet.append(row)
    workbook.save(outfp)


def read_catalog_workbook(infp, source_locale=None):
    raise_if_no_module('openpyxl')
    workbook = openpyxl.load_workbook(infp, read_only=True)
    catalogs = {}
    for sheet in workbook:
        languages = []
        for y, row in enumerate(sheet):
            texts = [cell.value for cell in row]
            if y == 0:
                languages = texts[:]
                if not source_locale:
                    source_locale = languages[0]
                for language in set(languages) - set(catalogs):
                    catalogs[language] = Catalog(language)
            else:
                texts = dict(zip(languages, texts))
                for language, text in texts.items():
                    if not text:  # pragma: no cover
                        continue
                    strip_text = text.strip()
                    if not strip_text:  # pragma: no cover
                        continue
                    catalogs[language].add(texts[source_locale], text)
    return catalogs
