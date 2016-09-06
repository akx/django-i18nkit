django-i18nkit
===============

Some utilities to make Django internationalization a little easier.

:exclamation: Work in progress.

Features
--------

* Sane Python/Django-HTML/Jinja2 message extraction
* Bidirectional Excel/gettext conversion, for those enterprise customers
* I18n poisoning, to make it easy to spot untranslated strings

Usage
-----

* Install with `pip` or whatever.
* Add `i18nkit` to your `INSTALLED_APPS`.

### Optional dependencies

* `django-jinja` is required for Jinja2 extraction.

Management Commands
-------------------

### `ik_export`

Exports internationalization data to non-gettext formats. (Currently Excel files.)

### `ik_extract`

Extracts translatables from Python, Django HTML and Jinja with sane defaults.

### `ik_import`

Imports non-gettext internationalization data to .po files. The inverse of `ik_export`.

### `ik_compile`

Compiles all `.po` files to `.mo` files.

Django Settings
---------------

### `I18NKIT_POISON`

(Boolean) Whether to globally enable i18n poisoning.

Note that this is only read during application initialization.

Be extra sure to have this disabled when creating migrations! :D
