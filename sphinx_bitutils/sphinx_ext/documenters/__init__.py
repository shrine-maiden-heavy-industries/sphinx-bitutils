# SPDX-License-Identifier: BSD-3-Clause

from sphinx.application import Sphinx

from .construct import SubconstructDocumenter

__all__ = (
	'ALL_DOCUMENTERS',
	'register_documenters',
)

ALL_DOCUMENTERS = (
	SubconstructDocumenter
)


def register_documenters(app: Sphinx = None) -> None:
	if app is None:
		raise ValueError('Application must be set')

	for documenter in ALL_DOCUMENTERS:
		app.add_autodocumenter(documenter)
