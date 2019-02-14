import os
import subprocess
from distutils.command.build_ext import build_ext
from distutils.command.build import build
from distutils.command.install import install

import setuptools
import logging


def log(msg):
    print(msg)
    logging.info(msg)


class Build(build):
    sub_commands = build.sub_commands + [('build_ext', None)]



CUSTOM_COMMANDS = [
    ['./libspatialindex_sbu/install_helper/build_spatialindex.sh'],
]


class CommandRunner:
    def __init__(self, commands):
        self.commands = commands

    def _run_command(self, command_list):
        p = subprocess.Popen(
            command_list,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while True:
            output = p.stdout.readline()
            output = output.decode('utf-8')
            if output == '' and p.poll() is not None:
                break
            if output:
                print(output.strip())

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


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    return paths

packages = setuptools.find_packages()

extra_data = package_files('libspatialindex_sbu/libspatialindex')

setuptools.setup(
    name='libspatialindex',
    version='0.0.1',
    description='libspatialindex installation via pip',
    author='Severin Buhler',
    author_email='severin.buehler@apgsga.ch',
    packages=packages,
    install_requires=[],
    package_data={
        'libspatialindex_sbu.install_helper': [
            '*.sh'
        ],
        '': extra_data
    },
    cmdclass={
        # Command class instantiated and run during pip install scenarios.
        'build_ext': CustomBuildExtCommand,
        'build': Build,
        'bdist_ext': CustomBuildExtCommand,
    },
    entry_points={
        'console_scripts': [
            'libspatialindex_install = libspatialindex_sbu.install_helper:install'
        ]
    }
)
