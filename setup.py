from setuptools import setup

setup(
    name='Localization Generator 6000',
    version='0.1',
    py_modules=['locgen'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        locgen=locgen:recurse_files
    ''',
)