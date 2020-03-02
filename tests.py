import pytest
import subprocess
import tempfile
from multiprocessing import Process

import logmux


def test_basics():
    with tempfile.NamedTemporaryFile() as log1,
         tempfile.NamedTemporaryFile() as log2,
         tempfile.NamedTemporaryFile() as log3:

        paths = [log1.name, log2.name, log3.name]
        
        process = Process(logmux.main, paths)
