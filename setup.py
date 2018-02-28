from setuptools import setup, find_packages


setup(
    name='search-gists',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    version='0.1',
    description='Search pubic gists for user',
    author='Santiago Basulto',
    author_email='santiago.basulto@gmail.com',
    url='https://rmotr.com',
    install_requires=[
        'click==6.7',
        'requests==2.18.4'
    ],
    extras_require={  # Optional
        'dev': [
            'pytest==3.4.1',
            'responses==0.8.1'
        ]
    },
    entry_points={  # Optional
        'console_scripts': [
            'search-gists=main:main',
        ],
    },
)
