=====
Usage
=====

**robogram** is a Minimal API Wrapper, utilizing Telegram Bot API
to send messages (to a user, channel, or group).


Sample Usage:

.. code-block:: python3

    from pprint import pprint
    from robogram import TeleBot

    bot_token = 'TOKEN'
    chat_id = -123456789

    bot = TeleBot(bot_token)

    me = bot.get_me()
    pprint(me)

    bot.send_message(chat_id, 'Hello World!')

