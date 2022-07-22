# SPDX-License-Identifier: BSD-3-Clause

from .directives  import register_directives
from .documenters import register_documenters

__all__ = (
	'register_directives',
	'register_documenters',
)
