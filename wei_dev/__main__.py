from __future__ import unicode_literals

from cmdtree import entry, argument, command, group, option

from wei_dev.sender import Sender


def _print(message):
    print message.encode("utf-8")


@command("gui")
def gui_main():
    from wei_dev.gui import start_app
    start_app()


@argument("url")
@group("cli")
def cli_commands():
    pass


@option("from-id", default=None)
@argument("message")
@cli_commands.command("text")
def text_msg(url, message, from_id):
    mgr = Sender(
        base_url=url,
        from_id=from_id,
    )
    _print(mgr.send_text_msg(message))


@option("from-id", default=None)
@argument("key")
@cli_commands.command("event")
def event_msg(url, key, from_id):
    mgr = Sender(
        base_url=url,
        from_id=from_id,
    )
    _print(mgr.send_click_event(key))


if __name__ == '__main__':
    entry()
