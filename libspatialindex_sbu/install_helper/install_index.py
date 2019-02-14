import os
import subprocess


def current_folder():
    current_file = os.path.realpath(__file__)
    current_dir = os.path.dirname(current_file)
    return current_dir


def install_index():
    command = [current_folder() + '/install_spatialindex.sh']
    p = subprocess.Popen(
        command,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=current_folder())

    while True:
        output = p.stdout.readline()
        output = output.decode('utf-8')
        if output == '' and p.poll() is not None:
            break
        if output:
            print(output.strip())

    if p.returncode != 0:
        raise RuntimeError(
            'Command %s failed: exit code: %s' % (command, p.returncode))

