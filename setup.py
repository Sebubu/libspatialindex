import subprocess
from distutils.command.build_ext import build_ext
from distutils.command.build import build
from distutils.command.install import install

import setuptools
import logging


def log(msg):
    print(msg)
    logging.info(msg)


class CustomInstall(install):
    def _install_spatialindex(self):
        command = ['./install_helper/install_spatialindex.sh']
        p = subprocess.Popen(
            command,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # Can use communicate(input='y\n'.encode()) if the command run requires
        # some confirmation.
        stdout_data, _ = p.communicate()

        log(stdout_data.decode('utf-8'))
        if p.returncode != 0:
            raise RuntimeError(
                'Command %s failed: exit code: %s' % (command, p.returncode))

    def run(self):
        self._install_spatialindex()
        install.run(self)


class Build(build):
    sub_commands = [('build_ext', None)] + build.sub_commands



CUSTOM_COMMANDS = [
    ['./install_helper/build_spatialindex.sh'],
]


class CommandRunner:
    def __init__(self, commands):
        self.commands = commands

    def _run_command(self, command_list):
        p = subprocess.Popen(
            command_list,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # Can use communicate(input='y\n'.encode()) if the command run requires
        # some confirmation.
        stdout_data, _ = p.communicate()

        log(stdout_data.decode('utf-8'))
        if p.returncode != 0:
            raise RuntimeError(
                'Command %s failed: exit code: %s' % (command_list, p.returncode))

    def run(self):
        for command in self.commands:
            log('Run %s' % command)
            self._run_command(command)


class CustomBuildExtCommand(build_ext):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        log("Run custom commands")

        runner = CommandRunner(CUSTOM_COMMANDS)
        runner.run()

        log('run super build')
        build_ext.run(self)



packages = setuptools.find_packages()
packages.append('install_helper')

setuptools.setup(
    name='libspatialindex',
    version='0.0.1',
    description='libspatialindex installation via pip',
    author='Severin Buhler',
    author_email='severin.buehler@apgsga.ch',
    packages=packages,
    install_requires=[],
    package_data={
        'install_helper': [
            '*.sh'
        ],
        'libspatialindex': [
            '*'
        ]
    },
    cmdclass={
        # Command class instantiated and run during pip install scenarios.
        'build_ext': CustomBuildExtCommand,
        'build': Build,
        'bdist_ext': CustomBuildExtCommand,
        'install': CustomInstall
    }
)
