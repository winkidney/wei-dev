# coding:utf-8
from __future__ import unicode_literals

MSG_TEXT = """
<xml>
<ToUserName><![CDATA[{to_openid}]]></ToUserName>
<FromUserName><![CDATA[{from_openid}]]></FromUserName> 
<CreateTime>{create_at}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{message}]]></Content>
<MsgId>{message_id}</MsgId>
</xml>
"""

MSG_CLICK_EVENT = """
<xml>
<ToUserName><![CDATA[{to_openid}]]></ToUserName>
<FromUserName><![CDATA[{from_openid}]]></FromUserName>
<CreateTime>{create_at}</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[CLICK]]></Event>
<EventKey><![CDATA[{event_key}]]></EventKey>
</xml>
"""
