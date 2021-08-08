"""Plugin's commands definition."""

import simplebot
from deltachat import Message
from pkg_resources import DistributionNotFound, get_distribution
from simplebot.bot import Replies

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = "0.0.0.dev0-unknown"


@simplebot.filter
def echo_filter(message: Message, replies: Replies) -> None:
    """I will echo back any text message you send me in private."""
    if not message.chat.is_group() and message.text:
        replies.add(text=message.text)


@simplebot.command
def echo(payload: str, replies: Replies) -> None:
    """Echo back received text.

    To use it send a message like:
    /echo hello world
    """
    replies.add(text=payload or "echo")


class TestPlugin:
    """Offline tests"""

    def test_echo(self, mocker):
        msg = mocker.get_one_reply("/echo")
        assert msg.text == "echo"

        msg = mocker.get_one_reply("/echo hello world")
        assert msg.text == "hello world"

    def test_filter(self, mocker):
        msg = mocker.get_one_reply("hello world")
        assert msg.text == "hello world"

        msgs = mocker.get_replies("hello world", group="TestGroup")
        assert not msgs
