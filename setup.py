from setuptools import setup


name = 'senic.cryptoyaml'


setup(
    name=name,
    version_format='{tag}.{commitcount}+{gitsha}',
    url='https://github.com/getsenic/senic.cryptoyaml',
    author='Senic GmbH',
    author_email='tom@senic.com',
    description='A python library to manage encrypted YAML files.',
    classifiers=[
        "Programming Language :: Python",
    ],
    packages=[name],
    include_package_data=True,
    package_dir={name: 'senic/cryptoyaml'},
    package_data={
        name: [
            '.coveragerc',
            'tests/*.py',
            'tests/data/*.*',
        ],
    },
    zip_safe=False,
    setup_requires=[
        'setuptools-git >= 0',
        'setuptools-git-version'
    ],
    install_requires=[
        'click',
        'ruamel.yaml',
        'cryptography',
    ],
    extras_require={
        'development': [
            'devpi-client',
            'docutils',
            'flake8',
            'mock',
            'pbr',
            'pdbpp',
            'pep8 < 1.6',
            'pyflakes',
            'pytest',
            'pytest-cov',
            'pytest-flakes',
            'pytest-pep8',
            'pytest-sugar',
            'repoze.sphinx.autointerface',
            'setuptools-git',
            'Sphinx',
            'tox',
        ],
    },
    entry_points="""
        [console_scripts]
        cryptoyaml = senic.cryptoyaml.commands:main
        [pytest11]
        cryptoyaml = senic.cryptoyaml.testing
    """,
)
