# setup.py

from setuptools import setup, Extension

setup(
	name='speed_vanila',
	ext_modules=[
		Extension(
			'speed_vanila',
			sources=['speed_vanila.c'],
		)
	],
)
