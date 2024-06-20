# -*- coding: utf-8 -*-
""" Telegram Bot API. """

from enum import Enum
from typing import Union

from requests import HTTPError, RequestException
import requests
import os


from .errors import RobogramException


class ChatActions(Enum):
    TYPING = 'typing'
    UPLOAD_PHOTO = 'upload_photo'
    RECORD_VIDEO = 'record_video'
    UPLOAD_VIDEO = 'upload_video'
    RECORD_AUDIO = 'record_audio'
    UPLOAD_AUDIO = 'upload_audio'
    UPLOAD_DOCUMENT = 'upload_document'
    FIND_LOCATION = 'find_location'


from functools import wraps

JSONType = Union[dict, list]


def handle_requests_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)

        try:
            r.raise_for_status()
            return r.json()
        except RequestException as he:
            raise RobogramException('Request Error', he)

    return wrapper


class Bot:

    def __init__(self, token):
        self.baseurl = f'https://api.telegram.org/bot{token}/'
        self.token = token
        self.hook = None
        self.hook_port = None
        self.hook_host = None

    def _req(self, method, path, **kwargs):
        requests.request(method, f'{self.baseurl}{path}', **kwargs)

    @handle_requests_errors
    def _get(self, path, params=None) -> JSONType:
        return requests.get(f'{self.baseurl}{path}', params=params)

    @handle_requests_errors
    def _post(self, path, data=None, json=None, **kwargs) -> JSONType:
        return requests.post(f'{self.baseurl}{path}', data, json, **kwargs)

    def set_webhook(self, hook=None):
        self.hook = hook or ''
        return self._post('setWebhook', json={'url': hook})

    def get_me(self):
        return self._get('getMe')

    def send_message(self, chat_id, text, parse_mode='Markdown', disable_web_page_preview=True, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': parse_mode,
            'disable_web_page_preview': disable_web_page_preview,
            'disable_notification': disable_notification
        }

        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            data['reply_markup'] = reply_markup

        return self._post('sendMessage', json=data)

    def forward_message(self, chat_id, from_chat_id, message_id, disable_notification=None):
        data = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }

        if disable_notification:
            data['disable_notification'] = disable_notification

        return self._post('forwardMessage', json=data)

    def send_file(self, method, chat_id, filepath, **optional):
        data = {'chat_id': chat_id}

        for key, value in optional.items():
            if value:
                data[key] = value

        with open(filepath, 'rb') as file:
            files = {method.replace('/send', '').lower(): (os.path.basename(filepath), file)}
            return self._post(method, data=data, files=files)

    def send_photo(self, chat_id, photo_path, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        return self.send_file('/sendPhoto', chat_id, photo_path, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    def send_audio(self, chat_id, audio_path, duration=None, performer=None, title=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        return self.send_file('/sendAudio', chat_id, audio_path, duration=duration, performer=performer, title=title, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    def send_document(self, chat_id, document_path, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        return self.send_file('/sendDocument', chat_id, document_path, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    def send_sticker(self, chat_id, sticker_path, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        return self.send_file('/sendSticker', chat_id, sticker_path, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    def send_video(self, chat_id, video_path, duration=None, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        return self.send_file('/sendVideo', chat_id, video_path, duration=duration, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    def send_voice(self, chat_id, voice_path, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        return self.send_file('/sendVoice', chat_id, voice_path, duration=duration, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    def send_location(self, chat_id, latitude, longitude, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        data = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude
        }

        if disable_notification:
            data['disable_notification'] = disable_notification

        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id

        if reply_markup:
            data['reply_markup'] = reply_markup

        return self._post('sendLocation', json=data)

    def send_chat_action(self, chat_id, action: ChatActions):
        data = {
            'chat_id': chat_id,
            'action': action.value
        }
        return requests.post(self.baseurl + 'sendChatAction', json=data)

    def get_user_profile_photos(self, user_id, offset=None, limit=None):
        data = {'user_id': user_id}
        if offset:
            data['offset'] = offset
        if limit:
            data['limit'] = limit
        return requests.post(self.baseurl + 'getUserProfilePhotos', json=data)

    def get_file(self, file_id, filename=None, directory=None):
        data = {'file_id': file_id}
        json_response = self._post('getFile', json=data)
        if json_response['ok']:
            file_path = json_response['result']['file_path']
            extension = file_path.split('.')[-1]
            import uuid
            download_name = f'{filename if filename else str(uuid.uuid4())}.{extension}'
            save_path = os.path.join(directory, download_name) if directory else download_name
            download_link = f'https://api.telegram.org/file/bot{self.token}/{file_path}'
            with requests.get(download_link, stream=True) as r:
                r.raise_for_status()
                with open(save_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            return True
        return False

    def get_chat_ids_from_updates(self, offset=None, limit=None, timeout=None):
        """
        Get a mapping of Chat ID to Chat Type/Title,
        based on `/getUpdates` response.

        Example Response:
        {
          12345: '[PRIVATE] User321',
          -97531: '[CHANNEL] My Channel',
        }

        """
        r = self.get_updates(offset, limit, timeout)
        assert r['ok']

        r = r['result']

        return {c['id']: f"[{c['type'].upper()}] {c.get('username') or c.get('title')}"
                for m in r
                for v in m.values()
                if isinstance(v, dict) and (c := v.get('chat'))}

    def get_updates(self, offset=None, limit=None, timeout=None):
        data = {}
        if offset:
            data['offset'] = offset
        if limit:
            data['limit'] = limit
        if timeout:
            data['timeout'] = timeout

        return self._get('getUpdates', params=data)

    # def get_keyboard(self, keyboard, resize_keyboard=None, one_time_keyboard=None, selective=None):
    #     data = {'keyboard': keyboard}
    #     if resize_keyboard:
    #         data['resize_keyboard'] = resize_keyboard
    #     if one_time_keyboard:
    #         data['one_time_keyboard'] = one_time_keyboard
    #     if selective:
    #         data['selective'] = selective
    #     return data

    # def get_hidden_keyboard(self, selective=None):
    #     data = {'hide_keyboard': True}
    #     if selective:
    #         data['selective'] = selective
    #     return data
    #
    # def get_forced_reply_keyboard(self, selective=None):
    #     data = {'force_reply': True}
    #     if selective:
    #         data['selective'] = selective
    #     return data
