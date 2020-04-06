from contextlib import contextmanager
from subprocess import PIPE
import logmux
import os.path
import pathlib
import pytest
import subprocess
import tempfile


@contextmanager
def logmux_process(paths, **kwargs):
    "Creates a logmux process that is ready for new input."

    command = ["logmux", "--verbose"] + paths
    with subprocess.Popen(command, stdout=PIPE, stderr=PIPE) as proc:
        # Wait for the process to print on stderr when it's ready
        proc.stderr.readline()
        try:
            yield proc
        finally:
            proc.terminate()


@contextmanager
def named_tempfiles(names):
    "Creates a set of named temporary files."

    with tempfile.TemporaryDirectory() as tmpdir:
        paths = [os.path.join(tmpdir, name) for name in names]

        for path in paths:
            pathlib.Path(path).touch()

        yield paths


def appendfile(path, bytestr):
    "Append bytes to a file."

    with open(path, "ab") as target:
        target.write(bytestr)


def test_basics():
    with named_tempfiles(["log1.log", "log2.log"]) as logpaths:
        print(logpaths)
        with logmux_process(logpaths) as proc:
            appendfile(logpaths[0], b"test line 1\n")
            appendfile(logpaths[0], b"test line 2\n")
            assert proc.stdout.readline() == b"log1: test line 1\n"


if __name__ == "__main__":
    test_basics()
