import nox
import os

python_version = os.environ.get('PYTHON_VERSION', False)


@nox.session(python=python_version, name='tests')
def tests(session):
    """Run tests."""
    if python_version:
        session.run('pip', 'install', '-r', 'requirements_dev.txt')
    session.run('python', '-m', 'unittest', '-v')


@nox.session(python=python_version, name='flake8')
def flake8(session):
    """Run flake8 linter."""
    if python_version:
        session.run('pip', 'install', '-r', 'requirements_dev.txt')
    session.run('flake8', '--max-line-length=115', 'cryptoapi', 'tests', 'noxfile.py', 'setup.py')


@nox.session(python=python_version, name='isort')
def isort(session):
    """Run isort import sorter."""
    if python_version:
        session.run('pip', 'install', '-r', 'requirements_dev.txt')
    session.run('isort', '-c', '-rc', 'cryptoapi', 'tests', 'noxfile.py', 'setup.py')
