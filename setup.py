# SPDX-License-Identifier: BSD-3-Clause
from setuptools import setup, find_packages
from pathlib    import Path

REPO_ROOT   = Path(__file__).parent
README_FILE = (REPO_ROOT / 'README.md')


def vcs_ver():
	def scheme(version):
		if version.tag and not version.distance:
			return version.format_with("")
		else:
			return version.format_choice("+{node}", "+{node}.dirty")
	return {
		"relative_to": __file__,
		"version_scheme": "guess-next-dev",
		"local_scheme": scheme
	}

setup(
	name             = 'sphinx-bitutils',
	use_scm_version  = vcs_ver(),
	author           = 'Aki \'lethalbit\' Van Ness',
	author_email     = 'nya@catgirl.link',
	description      = 'A sphinx extension that adds utilities to describe bitwise and bytewise binary structures',
	license          = 'BSD-3-Clause',
	python_requires  = '~=3.7',
	url              = 'https://github.com/lethalbit/sphinx-bitutils',
	zip_safe         = True,
	long_description = README_FILE.read_text(),
	long_description_content_type = 'text/markdown',

	setup_requires   = [
		'wheel',
		'setuptools',
		'setuptools_scm'
	],

	install_requires = [
		'sphinx',
		'construct>=2.10.67',
	],

	extras_require   = {

	},

	packages         = find_packages(),
	package_data     = {
		'sphinx_bitutils.assets': [
			'bitutils.css',
		]
	},

	classifiers      = [
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: BSD License',

		'Intended Audience :: Developers',

		'Operating System :: OS Independent',

		'Programming Language :: Python',
		'Programming Language :: Python :: 3',

		'Topic :: Documentation',
		'Topic :: Utilities',

		'Framework :: Sphinx',
		'Framework :: Sphinx :: Extension',
	],

	project_urls     = {
		'Documentation': 'https://lethalbit.github.io/sphinx-bitutils',
		'Source Code'  : 'https://github.com/lethalbit/sphinx-bitutils',
		'Bug Tracker'  : 'https://github.com/lethalbit/sphinx-bitutils/issues',
	}
)
