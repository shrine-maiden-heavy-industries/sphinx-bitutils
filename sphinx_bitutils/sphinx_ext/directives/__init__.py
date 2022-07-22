# SPDX-License-Identifier: BSD-3-Clause

from sphinx.application import Sphinx

from .bitfield          import BitfieldDirective
from .structure         import StructureDirective

__all__ = (
	'ALL_DIRECTIVES',
	'register_directives',
)

ALL_DIRECTIVES = (
	('bitfield',  BitfieldDirective ),
	('structure', StructureDirective),
)


def register_directives(app: Sphinx = None) -> None:
	if app is None:
		raise ValueError('Application must be set')

	for directive in ALL_DIRECTIVES:
		app.add_directive(*directive)
