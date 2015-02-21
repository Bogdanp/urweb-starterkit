from __future__ import print_function

import logging
import os
import signal
import subprocess
import sys
import time

from functools import partial
from os import getenv

logging.basicConfig(level=logging.DEBUG)


def getenv_or_fail(variable):
    value = getenv(variable)
    assert value
    return value


def latest_mtime(predicate):
    max_ = 0
    for root, dirs, files in os.walk("."):
        for name in files:
            name = os.path.join(root, name)
            if not predicate(name):
                continue

            try:
                mtime = long(os.stat(name).st_mtime)
                if mtime > max_:
                    max_ = mtime
            except OSError:
                pass

    return max_


def poll_for_change_and_then(k, predicate=lambda _: True):
    last_change = 0
    while True:
        change = latest_mtime(predicate)
        if change > last_change:
            last_change = change
            k()
        time.sleep(0.5)


def main(args):
    try:
        pre_command = getenv("PRE_COMMAND")
        post_command = getenv("POST_COMMAND")
        compilation_command = getenv_or_fail("COMPILATION_COMMAND")
        run_command = getenv_or_fail("RUN_COMMAND")
        call = partial(subprocess.call, shell=True)
        popen = partial(subprocess.Popen, shell=True)
        state = {"child": None}

        def setup():
            logging.debug("Starting up!")
            if pre_command:
                logging.debug("Running: " + pre_command)
                call(pre_command)

        def teardown(_=None, __=None):
            logging.debug("Tearing down!")
            if post_command:
                logging.debug("Running" + post_command)
                call(post_command)

        def on_change():
            if state["child"]:
                logging.debug("Killing previous process...")
                state["child"].kill()
                state["child"] = None

            logging.debug("Running: " + compilation_command)
            res = call(compilation_command)
            if res:
                logging.error("Compilation failed!")
                return

            logging.debug("Running: " + run_command)
            state["child"] = popen(run_command)

        setup()
        signal.signal(signal.SIGTERM, teardown)
        poll_for_change_and_then(
            on_change, predicate=lambda f: ".ur" in f)
    except KeyboardInterrupt:
        teardown()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
