from setuptools import find_packages, setup


install_requires = [
    'Flask >= 0.10.1, < 1.0',
    'SQLAlchemy >= 0.9.9, < 1.0',
    'Flask-SQLAlchemy >= 2.0, < 3.0',
]


tests_require = [
    'coveralls >= 1.0a2, < 2.0',
    'pytest >= 2.6.4, < 3.0',
    'pytest-cov >= 1.8.1, < 2.0',
]


docs_require = [
    'Sphinx >= 1.3, < 2.0',
]


setup(
    name='simple_python_project',
    version='0.0.1',
    author='Ahn Kiwook',
    author_email='kiwook@outlook.com',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'tests': tests_require,
    }
)
