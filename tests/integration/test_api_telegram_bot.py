"""Integration test package for robogram."""
import os
from pprint import pprint

import pytest

from robogram import Bot


BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

CHAT_ID_PERSONAL = os.getenv('CHAT_ID_PERSONAL')
CHAT_ID_CHANNEL = os.getenv('CHAT_ID_CHANNEL')
CHAT_ID_GROUP = os.getenv('CHAT_ID_GROUP')


@pytest.fixture
def bot():
    assert BOT_API_TOKEN, '`BOT_API_TOKEN` missing from environment'
    return Bot(BOT_API_TOKEN)


@pytest.fixture
def chat_id_personal():
    assert CHAT_ID_PERSONAL, '`CHAT_ID_PERSONAL` missing from environment'
    return CHAT_ID_PERSONAL


@pytest.fixture
def chat_id_channel():
    assert CHAT_ID_CHANNEL, '`CHAT_ID_CHANNEL` missing from environment'
    return CHAT_ID_CHANNEL


@pytest.fixture
def chat_id_group():
    assert CHAT_ID_GROUP, '`CHAT_ID_GROUP` missing from environment'
    return CHAT_ID_GROUP


def test_get_my(bot):
    me = bot.get_me()
    print(me)


def test_send_message_to_personal(bot, chat_id_personal):
    r = bot.send_message(chat_id_personal, 'Hello, person!')
    print(r)


def test_send_message_to_channel(bot, chat_id_channel):
    r = bot.send_message(chat_id_channel, 'Hello, channel!')
    print(r)


def test_send_message_to_group(bot, chat_id_group):
    r = bot.send_message(chat_id_group, 'Hello, group!')
    print(r)


def test_get_updates(bot):
    updates = bot.get_updates()
    pprint(updates)


def test_get_chat_ids_from_updates(bot):
    updates = bot.get_chat_ids_from_updates()
    pprint(updates)
