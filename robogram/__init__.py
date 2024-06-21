"""
Robogram
~~~~~~~~

Minimal API Wrapper, utilizing Telegram Bot API
to send messages (to a user, channel, or group).


Sample Usage:
    >>> from pprint import pprint
    >>> from robogram import TeleBot
    >>> bot = TeleBot('TOKEN')
    >>> me = bot.get_me()
    >>> pprint(me)
    >>> chat_id = -123456789
    >>> bot.send_message(chat_id, 'Hello World!')


For full documentation and more advanced usage, please see
<https://robogram.readthedocs.io>.

:copyright: (c) 2024 by Ritvik Nag.
:license:MIT, see LICENSE for more details.
"""

__all__ = [
    'TeleBot',
    'ChatActions',
]

import logging
from .api_telegram_bot import (
    TeleBot,
    ChatActions,
)
from .errors import RobogramException

# Set up logging to ``/dev/null`` like a library is supposed to.
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
logging.getLogger('robogram').addHandler(logging.NullHandler())
