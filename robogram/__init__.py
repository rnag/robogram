"""
Robogram
~~~~~~~~

Minimal API Wrapper, utilizing Telegram Bot API
to send messages (to a user, channel, or group).


Sample Usage:

    >>> import robogram

For full documentation and more advanced usage, please see
<https://robogram.readthedocs.io>.

:copyright: (c) 2024 by Ritvik Nag.
:license:MIT, see LICENSE for more details.
"""

__all__ = [
    'Bot',
    'ChatActions',
]

import logging
from .api_telegram_bot import (
    Bot,
    ChatActions,
)
from .errors import RobogramException

# Set up logging to ``/dev/null`` like a library is supposed to.
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
logging.getLogger('robogram').addHandler(logging.NullHandler())
