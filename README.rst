========================
Robogram 🤖📨️ - Telegram Bot API
========================


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


**robogram** is a minimal wrapper package
utilizing the `Telegram Bot API`_
to send messages (to a user, channel, or group).

The only dependency is `requests`_ --
with `over 50K stars on GitHub`_.

* Free software: MIT license
* Documentation: https://robogram.readthedocs.io.
* Telegram Bot API Docs: https://core.telegram.org/bots/api

.. _requests: https://pypi.org/project/requests/
.. _over 50K stars on GitHub: https://github.com/psf/requests/stargazers
.. _Telegram Bot API: https://core.telegram.org/bots/api

Usage
-----

.. code-block:: python

    import json

    from robogram import Bot

    # Authentication token, that you get by:
    #   (1) opening a chat with `@BotFather`
    #   (2) using command `/newbot` to create a new bot
    API_TOKEN = 'TODO'

    # Chat ID, that you get by:
    #   (1) Add the new bot to personal chat, channel, or group
    #   (2) Send a message to bot
    CHAT_ID = -123456789

    bot = Bot(API_TOKEN)

    r = bot.send_message(CHAT_ID, 'Hello World!')
    print(r)

.. code-block:: python3

    me = bot.get_me()
    print(json.dumps(me, indent=2))

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



Credits
-------

This package was created with Cookiecutter_ and the `rnag/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _`rnag/cookiecutter-pypackage`: https://github.com/rnag/cookiecutter-pypackage
