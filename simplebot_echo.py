import simplebot
from simplebot.bot import Replies

__version__ = "1.0.0"


@simplebot.command
def echo(payload: str, replies: Replies) -> None:
    """Echoes back received text.

    To use it you can simply send a message starting with
    the command '/echo'. Example: `/echo hello world`
    """
    replies.add(text=payload or "echo")


class TestEcho:
    def test_echo(self, mocker):
        msg = mocker.get_one_reply("/echo")
        assert msg.text == "echo"

        msg = mocker.get_one_reply("/echo hello world")
        assert msg.text == "hello world"
