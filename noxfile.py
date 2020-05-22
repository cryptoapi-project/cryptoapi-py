import os
from typing import List, Union

import nox  # type: ignore

python_version: Union[str, bool, List[str]] = os.environ.get('PYTHON_VERSION', False)
if isinstance(python_version, str):
    python_version = python_version.split(':')
files: List[str] = ['cryptoapi', 'tests', 'noxfile.py', 'setup.py', 'test_runner.py']
install_requires: List[str] = ['pip', 'install', '-r', 'requirements-dev.txt', '--no-cache-dir']
run_tests: List[str] = ['python', 'test_runner.py']


@nox.session(python=python_version, name='isort')
def isort(session: nox.session) -> None:
    """Run isort import sorter."""
    if python_version:
        session.run(*install_requires)
    command: List[str] = ['isort', '-rc', '-y']
    if session.posargs:
        command[-1] = '-c'

    session.run(*(command + files))


@nox.session(python=python_version, name='yapf')
def yapf(session: nox.session) -> None:
    """Run yapf code formatter."""
    if python_version:
        session.run(*install_requires)
    command: List[str] = ['yapf', '-r', '-i']
    if session.posargs:
        command[-1] = '-d'

    session.run(*(command + files))


@nox.session(python=python_version, name='flake8')
def flake8(session: nox.session) -> None:
    """Run flake8 linter."""
    if python_version:
        session.run(*install_requires)
    session.run('flake8', *files)


@nox.session(python=python_version, name='mypy')
def mypy(session: nox.session) -> None:
    """Run mypy static typifier."""
    if python_version:
        session.run(*install_requires)
    session.run('mypy', *files)


@nox.session(python=python_version, name='mainnet-tests')
def mainnet_tests(session: nox.session) -> None:
    """Run mainnet tests."""
    if python_version:
        session.run(*install_requires)
    session.run(
        *run_tests, env={'MAINNET': 'true'}
    )


@nox.session(python=python_version, name='testnet-tests')
def testnet_tests(session: nox.session) -> None:
    """Run testnet tests."""
    if python_version:
        session.run(*install_requires)
    session.run(*run_tests)
