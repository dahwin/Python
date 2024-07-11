# setup.py

from setuptools import setup, Extension

setup(
	name='dahwin',
	ext_modules=[
		Extension(
			'dahwin',
			sources=['dahwin.c'],
		)
	],
)
