import os

import nox

python_version = os.environ.get('PYTHON_VERSION', False)
files = ['cryptoapi', 'tests', 'noxfile.py', 'setup.py']


@nox.session(python=python_version, name='isort')
def isort(session):
    """Run isort import sorter."""
    if python_version:
        session.run('pip', 'install', '--requirement', 'requirements_dev.txt')
    command = ['isort', '-rc', '-y']
    if session.posargs:
        command[-1] = '-c'

    session.run(*(command + files))


@nox.session(python=python_version, name='yapf')
def yapf(session):
    """Run yapf code formatter."""
    if python_version:
        session.run('pip', 'install', '--requirement', 'requirements_dev.txt')
    command = ['yapf', '-r', '-i']
    if session.posargs:
        command[-1] = '-d'

    session.run(*(command + files))


@nox.session(python=python_version, name='flake8')
def flake8(session):
    """Run flake8 linter."""
    if python_version:
        session.run('pip', 'install', '--requirement', 'requirements_dev.txt')
    session.run('flake8', *files)


@nox.session(python=python_version, name='tests')
def tests(session):
    """Run tests."""
    if python_version:
        session.run('pip', 'install', '--requirement', 'requirements_dev.txt')
    session.run('python', '-m', 'unittest', '--verbose')
