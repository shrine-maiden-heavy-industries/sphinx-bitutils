# SPDX-License-Identifier: BSD-3-Clause
try:
	try:
		from importlib import metadata as importlib_metadata # py3.8
	except ImportError:
		import importlib_metadata # py3.7
	__version__ = importlib_metadata.version(__package__)
except ImportError:
	__version__ = ':nya_confused:' # :nocov:

from sphinx.application import Sphinx

from .assets            import init_assets
from .sphinx_ext        import register_directives, register_documenters

__all__ = (
	'setup',
	'Config',
)

class Config:
	_config_values = {
		'sphinx_bitutils_construct': (True, 'env'),
	}

	def __init__(self, **kwargs):
		for k, (d, r) in self._config_values.items():
			setattr(self, k, d)

		for k, v in kwargs.items():
			setattr(self, k, v)

def setup(app: Sphinx) -> dict:
	ext = {
		'version'           : __version__,
		'parallel_read_safe': True
	}

	app.setup_extension('sphinx.ext.autodoc')

	for k, (d, r) in Config._config_values.items():
		app.add_config_value(k, d, r)

	init_assets(app)

	register_directives(app)
	register_documenters(app)

	return ext
