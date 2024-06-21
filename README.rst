================================
Robogram 🤖📨️ - Telegram Bot API
================================


.. image:: https://img.shields.io/pypi/v/robogram.svg
        :target: https://pypi.org/project/robogram

.. image:: https://img.shields.io/pypi/l/robogram.svg
        :target: https://pypi.org/project/robogram

.. image:: https://img.shields.io/pypi/pyversions/robogram.svg
        :target: https://pypi.org/project/robogram

.. image:: https://github.com/rnag/robogram/actions/workflows/dev.yml/badge.svg
        :target: https://github.com/rnag/robogram/actions/workflows/dev.yml

.. image:: https://readthedocs.org/projects/robogram/badge/?version=latest
        :target: https://robogram.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/rnag/robogram/shield.svg
     :target: https://pyup.io/repos/github/rnag/robogram/
     :alt: Updates

**robogram** is an (unofficial) Minimal `Telegram Bot API`_ Wrapper
to send messages on `Telegram`_ - to user, channel, or group.

The only dependency is `requests`_ --
with `over 50K stars on GitHub`_.

.. _requests: https://pypi.org/project/requests/
.. _over 50K stars on GitHub: https://github.com/psf/requests/stargazers
.. _Telegram Bot API: https://core.telegram.org/bots/api
.. _Telegram: https://telegram.org/
.. _TeleBot: https://core.telegram.org/bots
.. _personal chat: https://telegram.org/tour/chat-folders
.. _channel: https://telegram.org/tour/channels
.. _group: https://telegram.org/tour/groups
.. _/getUpdates: https://core.telegram.org/bots/api#getupdates
.. _on PyPI: https://pypi.org/project/robogram
.. _in the docs: https://core.telegram.org/bots/tutorial#getting-ready

Install
-------

``robogram`` is available `on PyPI`_, and can be installed with ``pip``:

.. code-block:: shell

    $ pip install robogram

You'll also need to obtain an Bot Token as outlined `in the docs`_.

Usage
-----

Use a `TeleBot`_ to send a message to a `personal chat`_, `channel`_, or `group`_ on `Telegram`_:

.. code-block:: python

    from robogram import TeleBot

    # Authentication token, that you get by:
    #   (1) opening a chat with `@BotFather`
    #   (2) using command `/newbot` to create a new bot
    BOT_TOKEN = 'TOKEN'

    # Chat ID, that you get by:
    #   (1) Add the new bot to personal chat, channel, or group
    #   (2) Send a message to bot
    CHAT_ID = -123456789

    bot = TeleBot(BOT_TOKEN)

    r = bot.send_message(CHAT_ID, 'Hello World!')
    print(r)

Looking for an easier way to get the *Chat ID* for a personal chat, channel, or group?

Follow steps above, and add the Bot to chat. Then use ``TeleBot.get_chat_ids_from_updates``,
a convenience wrapper around `/getUpdates`_:

.. code-block:: python3

    import json

    # Get a mapping of Chat ID to Chat Type/Title,
    # based on `/getUpdates` response.
    #
    # Example Response:
    # {
    #   12345: '[PRIVATE] User321',
    #   -97531: '[CHANNEL] My Channel',
    # }
    chat_id_to_title = bot.get_chat_ids_from_updates()
    print(json.dumps(chat_id_to_title, indent=2))

To get info on the `TeleBot`_ associated with the token:

.. code-block:: python3

    me = bot.get_me()
    print(json.dumps(me, indent=2))


Credits
-------

This package was created with Cookiecutter_ and the `rnag/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _`rnag/cookiecutter-pypackage`: https://github.com/rnag/cookiecutter-pypackage
