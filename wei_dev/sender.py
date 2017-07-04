from __future__ import unicode_literals

import time
from random import randint

import requests

from wei_dev import templates as tpls

from wei_dev.constants import DEFAULT_OPENID_FROM, DEFAULT_OPENID_TO


class Sender(object):

    def __init__(self, base_url, from_id=None, to_id=None):
        self.base_url = base_url
        self.from_id = from_id or DEFAULT_OPENID_FROM
        self.to_id = to_id or DEFAULT_OPENID_TO
        self.session = requests.session()

    @property
    def url(self):
        return self.base_url + "?openid=%s" % self.from_id

    @staticmethod
    def _get_msg_id():
        return randint(1, 10000000)

    def send_text_msg(self, content):
        message = tpls.MSG_TEXT.format(
            to_openid=self.from_id,
            from_openid=self.to_id,
            create_at=time.time(),
            message=content,
            message_id=self._get_msg_id(),
        )
        response = self.session.post(
            self.url,
            data=message,
            headers={
                "Content-Type": "application/octet-stream",
            }
        )
        return response.text

    def send_click_event(self, event_key):
        message = tpls.MSG_CLICK_EVENT.format(
            to_openid=self.from_id,
            from_openid=self.to_id,
            create_at=time.time(),
            message_id=self._get_msg_id(),
            event_key=event_key,
        )
        response = self.session.post(
            self.url,
            data=message,
            headers={
                "Content-Type": "application/octet-stream",
            }
        )
        return response.text
