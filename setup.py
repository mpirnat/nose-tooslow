from setuptools import setup
import tooslow

setup(
    name='nose-tooslow',
    version=tooslow.__version__,

    description='Treat tests that execute too slowly as failed',
    long_description='',
    author='Mike Pirnat',
    author_email='mpirnat@gmail.com',
    license='MIT',
    url='https://github.com/mpirnat/nose-tooslow',

    packages=['tooslow'],
    entry_points={
        'nose.plugins': [
            'tooslow = tooslow:TooSlow',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2',
    ],
)
