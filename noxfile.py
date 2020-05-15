import os

import nox

python_version = '3.7'#os.environ.get('PYTHON_VERSION', False)
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


@nox.session(python=python_version, name='mainnet-tests')
def mainnet_tests(session):
    """Run mainnet tests."""
    if python_version:
        session.run('pip', 'install', '--requirement', 'requirements_dev.txt')
    session.run(
        'python',
        '-m',
        'unittest',
        '--verbose',
        env={'MAINNET': 'true'}
    )


@nox.session(python=python_version, name='testnet-tests')
def testnet_tests(session):
    """Run testnet tests."""
    if python_version:
        session.run('pip', 'install', '--requirement', 'requirements_dev.txt')
    session.run('python', '-m', 'unittest', '--verbose')
