import os

import nox    # type: ignore

python_version = os.environ.get('PYTHON_VERSION', False)
files = ['cryptoapi', 'tests', 'noxfile.py', 'setup.py', 'test_runner.py']
install_requires = ['pip', 'install', '-r', 'requirements_dev.txt', '--no-cache-dir']
run_tests = ['python', 'test_runner.py']


@nox.session(python=python_version, name='isort')
def isort(session):
    """Run isort import sorter."""
    if python_version:
        session.run(*install_requires)
    command = ['isort', '-rc', '-y']
    if session.posargs:
        command[-1] = '-c'

    session.run(*(command + files))


@nox.session(python=python_version, name='yapf')
def yapf(session):
    """Run yapf code formatter."""
    if python_version:
        session.run(*install_requires)
    command = ['yapf', '-r', '-i']
    if session.posargs:
        command[-1] = '-d'

    session.run(*(command + files))


@nox.session(python=python_version, name='flake8')
def flake8(session):
    """Run flake8 linter."""
    if python_version:
        session.run(*install_requires)
    session.run('flake8', *files)


@nox.session(python=python_version, name='mypy')
def mypy(session):
    """Run mypy static typifier."""
    if python_version:
        session.run(*install_requires)
    session.run('mypy', *files)


@nox.session(python=python_version, name='mainnet-tests')
def mainnet_tests(session):
    """Run mainnet tests."""
    if python_version:
        session.run(*install_requires)
    session.run(
        *run_tests,
        env={'MAINNET': 'true'}
    )


@nox.session(python=python_version, name='testnet-tests')
def testnet_tests(session):
    """Run testnet tests."""
    if python_version:
        session.run(*install_requires)
    session.run(*run_tests)
