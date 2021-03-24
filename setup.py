"""Setup module installation."""

import re

from setuptools import setup

if __name__ == "__main__":
    MODULE_NAME = "simplebot_echo"
    DESC = "An example plugin for SimpleBot, a Delta Chat(http://delta.chat/) bot"

    with open(MODULE_NAME + ".py") as fh:
        version = re.search(r"__version__ = \"(.*?)\"", fh.read(), re.M).group(1)

    with open("README.rst") as fh:
        long_description = fh.read()
    with open("CHANGELOG.rst") as fh:
        long_description += fh.read()
    with open("LICENSE") as fh:
        long_description += fh.read()

    setup(
        name=MODULE_NAME,
        version=version,
        description=DESC,
        long_description=long_description,
        long_description_content_type="text/x-rst",
        keywords="simplebot plugin deltachat",
        license="MPL",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Plugins",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
            "Operating System :: OS Independent",
            "Topic :: Utilities",
        ],
        zip_safe=False,
        include_package_data=True,
        py_modules=[MODULE_NAME],
        install_requires=[
            "simplebot",
        ],
        entry_points={
            "simplebot.plugins": "{0} = {0}".format(MODULE_NAME),
        },
    )
