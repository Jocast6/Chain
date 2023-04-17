from setuptools import setup

setup(
    name='Chain',
    version='0.1',
    author='Joel Castro',
    py_modules=['Chain'],
    entry_points={
        'console_scripts': [
            'Chain = Chain:main'
        ]
    }
)

