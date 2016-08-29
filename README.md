django-i18nkit
===============

Some utilities to make Django internationalization a little easier.

:exclamation: Work in progress.

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
