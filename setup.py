import setuptools
import sys


if not sys.version_info.major == 3:
    sys.exit('requires Python 3')

requirements = ['requests']
if sys.version_info.minor < 4:
    requirements.append('pathlib')

setuptools.setup(
    name='tawi',
    version='0.0.1',
    description='Helper scripts for git feature branch workflow.',
    author='Carl George',
    author_email='carl@cgtx.us',
    url='https://github.com/cgtx/tawi',
    packages=['tawi'],
    install_requires=requirements,
    entry_points={'console_scripts': ['git-token=tawi.token:entry_point']},
    classifiers=['Programming Language :: Python :: 3']
)
