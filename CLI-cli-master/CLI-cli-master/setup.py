from setuptools import setup
setup(
    name = 'CLI-cli',
    version = '0.1.0',
    packages = ['CLI'],
    entry_points = {
        'console_scripts': [
            'CLI = CLI.__main__:main'
        ]
    })
