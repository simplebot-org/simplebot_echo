"""Plugin's commands definition."""

import simplebot
from pkg_resources import DistributionNotFound, get_distribution
from simplebot.bot import Replies

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = "0.0.0.dev0-unknown"


@simplebot.command
def echo(payload: str, replies: Replies) -> None:
    """Echoes back received text.

    To use it you can simply send a message starting with
    the command '/echo'. Example: `/echo hello world`
    """
    replies.add(text=payload or "echo")


class TestPlugin:
    """Offline tests"""

    def test_echo(self, mocker):
        msg = mocker.get_one_reply("/echo")
        assert msg.text == "echo"

        msg = mocker.get_one_reply("/echo hello world")
        assert msg.text == "hello world"
