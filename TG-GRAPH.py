import os
from colorama import Fore,init
from pyrogram import Client, filters, idle , errors ,enums
from pyrogram import raw
from telegraph import upload_file
from pyrogram.errors import ChatWriteForbidden
from threading import Timer
import aiohttp
from PIL import Image, ImageFilter, ImageEnhance
import os
import aiofiles
import os
# بعد از این import ها:
from pyrogram.raw import functions , base , types
from pyrogram.raw.functions.auth import ResetAuthorizations

# این import رو اضافه کن:
from pyrogram.raw import types
from urllib.parse import urlparse
from html import escape
from thisapidoesnotexist import get_cat, get_person
from random import randint
import re, sys, os, requests
from datetime import date,datetime
import jdatetime
import urllib
import sqlite3
from pathlib import Path
import openai
import sys
import traceback
import html
from countryinfo import CountryInfo
from currency_converter import CurrencyConverter
import random
import re
import threading
import aiohttp
import requests
from pyrogram.types import InputMediaPhoto, InputMediaVideo
import asyncio
import shutil
import math
from bs4 import *
import requests
import base64
import logging
import importlib
from pyrogram.types import Message, ChatPermissions, ReplyKeyboardMarkup, InlineQueryResultArticle, \
    InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton as button, InlineQueryResultPhoto, CallbackQuery
from pyrogram.raw import functions , base , types
from pyrogram.raw.functions.auth import ResetAuthorizations
from pyrogram.raw.functions.contacts import GetBlocked
from pyrogram.raw.functions.messages import GetAllStickers
from requests import get as GET
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from wikipedia import search,page
import pytz
from translate import Translator
from datetime import date,datetime
import instagram_private_api as insta
from pyrogram.filters import create
from random import choice
import instagram_private_api as insta
from os import name
from plugins import *
from time import time
from gtts import gTTS
from ipapi import location
from socket import gethostbyname
from platform import python_version,uname
from urllib.request import Request
#from youtube_dl import YoutubeDL
from uptime import uptime
from time import strftime, gmtime
from re import match,findall
from time import sleep
from qrcode import make
from psutil import virtual_memory,cpu_freq,cpu_percent,cpu_count
import psutil
from base64 import b64encode
from decimal import Decimal,getcontext
import json
import sys
import pytz
from io import StringIO
from requests import get as make_get_request
from bs4 import BeautifulSoup
from pySmartDL import SmartDL
import zipfile
from pyrogram.types import InputMediaPhoto
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pathlib import Path
from shutil import copyfile
from pyrogram import filters, Client 
from pyrogram.raw import functions
from pyrogram.enums import ChatType, UserStatus
from pyrogram.errors.exceptions.flood_420 import FloodWait
from io import BytesIO
import math
import shlex
from datetime import datetime, timezone
from typing import Tuple
from pymediainfo import MediaInfo
import shlex
import textwrap
from typing import Tuple
from bs4 import BeautifulSoup as bs
from pyrogram import Client, emoji, filters
from pyrogram.enums import ParseMode
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from PIL import Image, ImageOps
import time
from pyrogram import ContinuePropagation
from pyrogram.errors import RPCError
from pyrogram.raw.functions.account import GetAuthorizations, ResetAuthorization
from pyrogram.raw.types import UpdateServiceNotification
from bs4 import BeautifulSoup
from typing import Union
from time import perf_counter
import pickle
from pyrogram.errors.exceptions.bad_request_400 import ChatNotModified
from pyrogram.types import ChatPermissions, Message
import datetime
users = []
my_users = []
users = filters.user(my_users)
enemy = []
love = []
fal = []
mutey = []
tabchitimer = []
admin = 8324661572
last_response_time = {}
keep_online_timer = None
title_lock_chats = {}
lock_profile_chats = []
silent_chats = {}
auto_leave_chats = []
filter_words = {}
allow_words = {}
silent_users = {}
welcome_settings = {}
ban_all_users = []
slow_mode_chats = {}
chat_histories = {}
API_ID = 32723346
API_HASH = '00b5473e6d13906442e223145510676e'

# |====================================| #

fonts = {
    'Font1': {'0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔', '7': '𝟕', '8': '𝟖', '9': '𝟗'},
    'Font2': {'0': '𝟘', '1': '𝟙', '2': '𝟚', '3': '𝟛', '4': '𝟜', '5': '𝟝', '6': '𝟞', '7': '𝟟', '8': '𝟠', '9': '𝟡'},
    'Font3': {'0': '⓪', '1': '①', '2': '②', '3': '③', '4': '④', '5': '⑤', '6': '⑥', '7': '⑦', '8': '⑧', '9': '⑨'},
    'Font4': {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'},
    'Font5': {'0': '𝟶', '1': '𝟷', '2': '𝟸', '3': '𝟹', '4': '𝟺', '5': '𝟻', '6': '𝟼', '7': '𝟽', '8': '𝟾', '9': '𝟿'},
    'Font6': {'0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵'},
    'Font7': {'0': '０', '1': '１', '2': '２', '3': '３', '4': '４', '5': '５', '6': '６', '7': '７', '8': '８', '9': '９'},
    'Font8': {'0': '0̴', '1': '1̴', '2': '2̴', '3': '3̴', '4': '4̴', '5': '5̴', '6': '6̴', '7': '7̴', '8': '8̴', '9': '9̴'},
    'Font9': {'0': '0̸', '1': '1̸', '2': '2̸', '3': '3̸', '4': '4̸', '5': '5̸', '6': '6̸', '7': '7̸', '8': '8̸', '9': '9̸'},
    'Font10': {'0': '⓿', '1': '➊', '2': '➋', '3': '➌', '4': '➍', '5': '➎', '6': '➏', '7': '➐', '8': '➑', '9': '➒'},
    'Font11': {'0': '0⃨', '1': '1⃨', '2': '2⃨', '3': '3⃨', '4': '4⃨', '5': '5⃨', '6': '6⃨', '7': '7⃨', '8': '8⃨', '9': '9⃨'},
    'Font12': {'0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵'},
    'Font13': {'0': '0͟', '1': '1͟', '2': '2͟', '3': '3͟', '4': '4͟', '5': '5͟', '6': '6͟', '7': '7͟', '8': '8͟', '9': '9͟'},
    'Font14': {'0': '0͙', '1': '1͙', '2': '2͙', '3': '3͙', '4': '4͙', '5': '5͙', '6': '6͙', '7': '7͙', '8': '8͙', '9': '9͙'},
    'Font15': {'0': '0⃗', '1': '1⃗', '2': '2⃗', '3': '3⃗', '4': '4⃗', '5': '5⃗', '6': '6⃗', '7': '7⃗', '8': '8⃗', '9': '9⃗'},
    'Font16': {'0': '0꣠', '1': '1꣡', '2': '2꣢', '3': '3꣣', '4': '4꣤', '5': '5꣥', '6': '6꣦', '7': '7꣧', '8': '8꣨', '9': '9꣩'},
    'Font17': {'0': '0͓̽', '1': '1͓̽', '2': '2͓̽', '3': '3͓̽', '4': '4͓̽', '5': '5͓̽', '6': '6͓̽', '7': '7͓̽', '8': '8͓̽', '9': '9͓̽'},
    'Font18': {'0': 'օ', '1': 'յ', '2': 'շ', '3': 'Յ', '4': 'կ', '5': 'Տ', '6': 'ճ', '7': 'Դ', '8': 'Ց', '9': 'գ'}
}

# |====================================| #

def TimeName():
    try:
        a = json_read("data.json")
        if a.get("timename") == "on":
            tz = pytz.timezone(a.get("timezone", "Asia/Tehran"))
            now = datetime.now(tz)
            
            # فقط در ثانیه ۰۰ هر دقیقه آپدیت شود
            if now.strftime("%S") == "00":
                number = now.strftime("%H:%M")
                FONT = a.get("font", "Font1")
                
                if FONT == "Random":
                    selected_font = random.choice(list(fonts.keys()))
                    current_time = now.strftime("%H:%M")
                    converted_time = ''.join([fonts[selected_font].get(char, char) for char in current_time])
                    app.invoke(functions.account.UpdateProfile(last_name=converted_time))
                else:
                    number_unicode = ''.join([fonts.get(FONT, {}).get(c, c) for c in str(number)])
                    app.invoke(functions.account.UpdateProfile(last_name=number_unicode))
                    
    except Exception:
        pass  # هیچ خطایی نمایش داده نمی‌شود

# |====================================| #

def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Y', suffix)

# |====================================| #

def get_cast(casttype, movie):
    mov_casttype = ""
    if casttype in list(movie.keys()):
        i = 0
        for j in movie[casttype]:
            if i < 1:
                mov_casttype += str(j)
            elif i < 5:
                mov_casttype += ", " + str(j)
            else:
                break
            i += 1
    else:
        mov_casttype += "Not Data"
    return mov_casttype

# |====================================| #

now = ""
galbe = ["🤍","🖤","🤎","💜","💙","💚","💛","🧡","❤️"]

# |====================================| #

ez_emoji = ["😀", "😃", "😄", "😁", "😆", "😅", "🗿", "🤣", "😭", "😗", "😙", "😚", "😘", "🥰", "😍", "🤩", "🥳", "🤗", "🙃", "🙂", "☺️", "😊", "😏", "😌", "😉", "🤭", "😶", "🤔", "🤪", "😜", "😝", "😛", "😋", "😔", "😑", "😐", "🤨", "🧐", "🙄", "😒", "😤", "😠", "😡", "🤬", "☹️", "😰", "🤫", "🤐", "😬", "😳", "🥺", "😟", "😕", "🙁", "😨", "😧", "😦", "😮", "😯", "😲", "😱", "🤯", "😢", "😥", "😓", "😞", "😣", "😖", "😩", "😫", "🤤", "🥱", "🤮", "😇", "😵", "🤥", "🤓", "😎", "🤑", "🤠"]
answer = []
javab = []
Src_vrsion = "V1"

# |====================================| #

if not os.path.isfile("data.json"):
 with open("data.json" , "w") as fjr:
  fjr.write('{"language": "fa", "limitDel": 4, "welcome": "off", "firstcom": "off", "timename": "off", "timebiov1": "off", "fontname": "off", "fuck": "off", "anti_del": "off", "autoan": "off", "boldmode": "off", "emojimode": "off", "underline": "off", "italicmode": "off", "codemode": "off", "strike": "off", "spoilermode": "off","quotemode": "off","pvlock": "off","typing": "off","mention": "off","monshi": "off", "monshi_delay": 0, "monshi_text": "در حال حاضر در دسترس نیستم. به زودی پاسخ می‌دهم.", "timezone": "Asia/Tehran", "font": "Font1", "playing": "off", "typing_action": "off", "record_video": "off", "choose_sticker": "off", "upload_video": "off", "upload_document": "off", "upload_audio": "off", "speaking": "off", "all_playing": "off", "all_typing": "off", "all_record_video": "off", "all_choose_sticker": "off", "all_upload_video": "off", "all_upload_document": "off", "all_upload_audio": "off", "all_speaking": "off", "signature": "off", "signature_text": "", "auto_reaction": "off", "reaction_emoji": "🔥", "pv_silet": "off", "lock_text": "off", "lock_forward": "off", "lock_location": "off", "lock_photo": "off", "lock_video_note": "off", "lock_video": "off", "lock_link": "off", "lock_gif": "off", "lock_sticker": "off", "lock_english": "off", "lock_persian": "off", "lock_audio": "off", "lock_voice": "off", "lock_contact": "off", "lock_poll": "off", "lock_premium_emoji": "off", "lock_mention": "off", "fields": "", "auto_answers": "off", "keep_online": "off", "poker_pv": "off", "poker_all": "off", "markall": "off", "markall_group": "off", "title_lock": "off", "lock_profile": "off", "group_silent": "off", "auto_leave": "off", "join_action": "off", "join_type": "none", "welcome": "off", "welcome_text": "خوش آمدید!", "typing_all_groups": "off", "antilogin": "off", "title_lock_chats": {}, "lock_profile_chats": [], "silent_chats": {}, "auto_leave_chats": [], "filter_words": {}, "allow_words": {}, "silent_users": {}, "welcome_settings": {}, "ban_all_users": [], "slow_mode_chats": {}, "Bback_channel": "", "Bback_channel_title": ""}')
  fjr.close()
# اولیه‌سازی save_channel و saved_mades
json_database = json_read("data.json")
if "save_channel_id" not in json_database:
    json_database["save_channel_id"] = None
if "saved_mades" not in json_database:
    json_database["saved_mades"] = {}  # {name: message_data}
write("data.json", json.dumps(json_database))
# اولیه‌سازی online_group_id
json_database = json_read("data.json")
if "online_group_id" not in json_database:
    json_database["online_group_id"] = None
write("data.json", json.dumps(json_database))
if not os.path.isfile("fucking.json"):
 with open("fucking.json" , "w") as fjr:
  fjr.write('{"fuck": "off"}')
  fjr.close()
# اولیه‌سازی فیلدها
json_database = json_read("data.json")
for key in ["fields", "auto_answers", "keep_online"]:
    if key not in json_database:
        json_database[key] = {} if key != "keep_online" else "off"
write("data.json", json.dumps(json_database))
if_not_exist_creat("time.txt")
if_not_exist_creat("user.txt")
if_not_exist_creat("db.txt")

# |====================================| #

app = Client("VIP-TELEGR", API_ID, API_HASH,device_model="Ubuntu",app_version="Teleg Assistant 12.12.7")
client = Client("VIP-TELEGR", API_ID, API_HASH,device_model="Ubuntu",app_version="Teleg Assistant 12.12.7")

# |====================================| #

#with app:
#    try:
#        app.join_chat("@Pars_Create")
#    except:
#        pass

# |====================================| #






def create_chat_html(user_id, chat_history, current_question, current_answer):
    """ایجاد فایل HTML از مکالمه"""
    try:
        # ایجاد پوشه chats اگر وجود ندارد
        chats_dir = Path("chats")
        chats_dir.mkdir(exist_ok=True)
        
        # نام فایل با timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_{user_id}_{timestamp}.html"
        filepath = chats_dir / filename
        
        # ساختار HTML
        html_content = f"""
        <!DOCTYPE html>
        <html lang="fa" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>مکالمه ChatGPT</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    margin: 0;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                }}
                .chat-container {{
                    max-width: 800px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 15px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                    overflow: hidden;
                }}
                .chat-header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .chat-header h1 {{
                    margin: 0;
                    font-size: 24px;
                }}
                .chat-header .subtitle {{
                    margin: 5px 0 0 0;
                    opacity: 0.9;
                    font-size: 14px;
                }}
                .messages-container {{
                    padding: 20px;
                    max-height: 600px;
                    overflow-y: auto;
                }}
                .message {{
                    margin-bottom: 20px;
                    animation: fadeIn 0.5s ease-in;
                }}
                .user-message {{
                    background: #e3f2fd;
                    border-radius: 15px 15px 0 15px;
                    padding: 15px;
                    margin-left: 50px;
                    border: 1px solid #bbdefb;
                }}
                .bot-message {{
                    background: #f3e5f5;
                    border-radius: 15px 15px 15px 0;
                    padding: 15px;
                    margin-right: 50px;
                    border: 1px solid #e1bee7;
                }}
                .message-header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 8px;
                    font-weight: bold;
                    font-size: 14px;
                }}
                .user-header {{
                    color: #1565c0;
                }}
                .bot-header {{
                    color: #7b1fa2;
                }}
                .message-time {{
                    font-size: 12px;
                    opacity: 0.7;
                }}
                .message-content {{
                    font-size: 15px;
                    line-height: 1.8;
                }}
                .current-session {{
                    background: #fff8e1;
                    border: 2px solid #ffd54f;
                    border-radius: 10px;
                    padding: 15px;
                    margin: 20px 0;
                }}
                .session-title {{
                    color: #ff6f00;
                    font-weight: bold;
                    margin-bottom: 10px;
                    text-align: center;
                }}
                @keyframes fadeIn {{
                    from {{ opacity: 0; transform: translateY(10px); }}
                    to {{ opacity: 1; transform: translateY(0); }}
                }}
                .chat-footer {{
                    background: #f5f5f5;
                    padding: 15px;
                    text-align: center;
                    font-size: 12px;
                    color: #666;
                    border-top: 1px solid #ddd;
                }}
                .message-count {{
                    background: #4caf50;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 15px;
                    font-size: 12px;
                    margin-left: 10px;
                }}
                .system-info {{
                    background: #e8f5e8;
                    border: 1px solid #c8e6c9;
                    border-radius: 10px;
                    padding: 15px;
                    margin: 15px 0;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <div class="chat-container">
                <div class="chat-header">
                    <h1>🤖 مکالمه ChatGPT</h1>
                    <div class="subtitle">
                        تاریخ: {datetime.now().strftime("%Y/%m/%d - %H:%M")}
                        <span class="message-count">تعداد پیام: {len(chat_history) + 2}</span>
                    </div>
                </div>
                
                <div class="messages-container">
        """
        
        # اضافه کردن تاریخچه چت
        for i, message in enumerate(chat_history, 1):
            if message["role"] == "user":
                html_content += f"""
                    <div class="message">
                        <div class="user-message">
                            <div class="message-header user-header">
                                👤 شما
                                <span class="message-time">سوال #{i}</span>
                            </div>
                            <div class="message-content">{message['content']}</div>
                        </div>
                    </div>
                """
            else:
                html_content += f"""
                    <div class="message">
                        <div class="bot-message">
                            <div class="message-header bot-header">
                                🤖 ChatGPT
                                <span class="message-time">پاسخ #{i}</span>
                            </div>
                            <div class="message-content">{message['content']}</div>
                        </div>
                    </div>
                """
        
        # اضافه کردن سوال و پاسخ جاری با هایلایت
        html_content += f"""
                    <div class="current-session">
                        <div class="session-title">💬 سوال و پاسخ جاری</div>
                        
                        <div class="message">
                            <div class="user-message">
                                <div class="message-header user-header">
                                    👤 شما
                                    <span class="message-time">سوال #{len(chat_history) + 1}</span>
                                </div>
                                <div class="message-content">{current_question}</div>
                            </div>
                        </div>
                        
                        <div class="message">
                            <div class="bot-message">
                                <div class="message-header bot-header">
                                    🤖 ChatGPT
                                    <span class="message-time">پاسخ #{len(chat_history) + 1}</span>
                                </div>
                                <div class="message-content">{current_answer}</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="system-info">
                        🚀 ایجاد شده توسط سلف پارسا | این فایل شامل تمام مکالمات این چت می‌باشد
                    </div>
                </div>
                
                <div class="chat-footer">
                    ایجاد شده در {datetime.now().strftime("%Y/%m/%d %H:%M:%S")} | سلف پارسا
                </div>
            </div>
            
            <script>
                // اسکرول به پایین هنگام لود صفحه
                window.onload = function() {{
                    const messagesContainer = document.querySelector('.messages-container');
                    messagesContainer.scrollTop = messagesContainer.scrollHeight;
                }};
                
                // هایلایت کردن سشن جاری
                const currentSession = document.querySelector('.current-session');
                currentSession.style.animation = 'pulse 2s infinite';
                
                const style = document.createElement('style');
                style.textContent = `
                    @keyframes pulse {{
                        0% {{ box-shadow: 0 0 0 0 rgba(255, 111, 0, 0.4); }}
                        70% {{ box-shadow: 0 0 0 10px rgba(255, 111, 0, 0); }}
                        100% {{ box-shadow: 0 0 0 0 rgba(255, 111, 0, 0); }}
                    }}
                `;
                document.head.appendChild(style);
            </script>
        </body>
        </html>
        """
        
        # ذخیره فایل
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath
        
    except Exception as e:
        print(f"Error creating HTML file: {e}")
        return None









def is_english(text):
    return bool(re.search(r'[a-zA-Z]', text))

def is_persian(text):
    return bool(re.search(r'[\u0600-\u06FF]', text))

def mak():
 with app:
  m =  app.send_message("me" , ".").message_id
  app.delete_messages("me" , m)

# |====================================| #

def job():
 a = json_read("data.json")
 jdatetime.set_locale('fa_IR')
 d = jdatetime.datetime.now().strftime("%a")
 if read("time.txt") != datetime.datetime.now(pytz.timezone("Asia/Tehran")).strftime("%H:%M"):
  try:
   if (a["timebiov1"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'فضولی شما در تاریخ {fozolidate()} در ساعت {fozolitime()} با موفقیت ثبت شد✅'))
   if (a["fontname"] == "on"):app.invoke(functions.account.UpdateProfile(first_name=f'{fontinname(read("user.txt"))}'))
  except :
   pass
  write("time.txt" , datetime.datetime.now(pytz.timezone("Asia/Tehran")).strftime("%H:%M"))

def create_language_filter():
    def language_filter(_, __, m: Message):
        try:
            json_database = json_read("data.json")
            current_lang = json_database.get("language", "fa")
        
            if not m.from_user or m.from_user.id != app.me.id:
                return True
                
            if not m.text or not m.text.startswith('.'):
                return True
            
            persian_commands = {
                "ریستارت", "ریست", "ریس", "ریسیت", "پینگ", "سشن", 
                "ویکی", "امروز", "آیدی", "خاطره", "الکی", "داستان",
                "دیالوگ", "اسم_رندوم", "ساخت_کانال", "ساخت_گروه",
                "تنظیم_نام_گروه", "تنظیم_بیو_گروه", "پین", "حذف_پین",
                "حذف_همه_پین", "تنظیم_یوزرنیم_گروه", "حذف_سکوت",
                "تنظیم_سکوت", "تنظیم_پروفایل_گروه", "حذف_پروفایل_گروه",
                "حذف_لیست_دشمن", "حذف_لیست_دوست", "حذف_لیست_سکوت",
                "ساعت_بیو_اول", "منطقه_زمانی", "فونت_نام", "آمار", "پنل", "راهنما",
                "کنترل", "فوتبال", "ریسیت", "پاکسازی", "ممبر", "بیو", "یوزرنیم"
            }
            
            english_commands = {
                "restart", "reset", "ping", "session", "wiki",
                "date", "id", "memo", "alaki", "dastan", "dlg",
                "rname", "creatchannel", "creatgroup", "setchattitle",
                "setchatbio", "pin", "unpin", "unpinall", "setchatusername",
                "delmute", "setmute", "delenemylist", "dellovelist", 
                "delmutelist", "timebiov1", "timezone", "fontname",
                "stats", "panel", "football" "help", "clear", "member", "bio", "username"
            }
            
            command_text = m.text[1:].split()[0].lower()
            
            if current_lang == "fa":
                return command_text in persian_commands
            else:
                return command_text in english_commands
                
        except Exception:
            return True
    
    return filters.create(language_filter)

language_filter = create_language_filter()

# |====================================| #

async def keep_online_job():
    """کار زمان‌بندی شده برای نگه داشتن آنلاین بودن"""
    try:
        json_database = json_read("data.json")
        
        if json_database.get("keep_online", "off") == "on":
            # ارسال یک درخواست وضعیت آنلاین
            await app.invoke(functions.account.UpdateStatus(offline=False))
            
    except Exception as e:
        print(f"خطا در بروزرسانی وضعیت آنلاین: {e}")

# این تابع رو می‌تونی قبل از scheduler اضافه کنی:

# |====================================| #

# تنظیم اولیه در شروع ربات
async def initialize_online_status():
    """تنظیم وضعیت آنلاین در شروع ربات"""
    try:
        json_database = json_read("data.json")
        
        if json_database.get("keep_online", "off") == "on":
            await app.invoke(functions.account.UpdateStatus(offline=False))
            print("✅ حالت همیشه آنلاین فعال شد")
            
    except Exception as e:
        print(f"خطا در تنظیم وضعیت آنلاین اولیه: {e}")

# و این خط رو به scheduler اضافه کن:


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)

# |====================================| #

@app.on_message(filters.private & filters.incoming & ~filters.me & ~filters.bot, group=32)
async def monshi_handler(app, message: Message):
    json_database = json_read("data.json")
    
    if json_database.get("monshi", "off") == "off":
        return
    
    user_id = message.from_user.id
    current_time = time.time()
    
    
    monshi_delay = json_database.get("monshi_delay", 0)
    if monshi_delay > 0:
        last_time = last_response_time.get(user_id, 0)
        if current_time - last_time < monshi_delay:
            return  
    
    
    last_response_time[user_id] = current_time
    monshi_text = json_database.get("monshi_text", "**متنی تنظیم نشده است!**")
    try:
        await app.send_message(
            chat_id=user_id,
            text=monshi_text,
            reply_to_message_id=message.id
        )
    except Exception as e:
        print(f"Error in monshi handler: {e}")

# |====================================| #:

@app.on_message(filters.command(["setlang", "تنظیم زبان"], ".") & filters.me)
async def set_language_handler(app, m: Message):
    try:
        if len(m.command) < 2:
            await m.edit_text("**استفاده نادرست!**")
            return
        
        lang_choice = m.command[1].lower()
        json_database = json_read("data.json")
        
        if lang_choice in ["fa", "persian", "فارسی"]:
            json_database.update({"language": "fa"})
            write("data.json", json.dumps(json_database))
            await m.edit_text("**• زبان روی فارسی تنظیم شد.**")
            
        elif lang_choice in ["en", "english", "انگلیسی"]:
            json_database.update({"language": "en"})
            write("data.json", json.dumps(json_database))
            await m.edit_text("✅ **Bot language set to English**\n\n• From now on, only English commands will work")
            
        else:
            await m.edit_text("❖ **زبان نامعتبر!**\n\n• برای فارسی: `.setlang fa`\n• برای انگلیسی: `.setlang en`")
            
    except Exception as e:
        await m.edit_text(f"❖ **خطا:**\n`{str(e)}`")

@app.on_message(filters.command(["lang", "زبان"], ".") & filters.me)
async def language_status_handler(app, m: Message):
    """نمایش وضعیت زبان فعلی"""
    try:
        json_database = json_read("data.json")
        current_lang = json_database.get("language", "fa")
        
        if current_lang == "fa":
            status_text = (
                "🌐 **وضعیت زبان ربات:**\n\n"
                "🔹 **زبان فعلی:** فارسی 🇮🇷\n"
                "🔹 **دستورات فعال:** دستورات فارسی\n"
                "🔹 **دستورات غیرفعال:** دستورات انگلیسی\n\n"
                "برای تغییر به انگلیسی: `.setlang en`"
            )
        else:
            status_text = (
                "🌐 **Bot Language Status:**\n\n"
                "🔹 **Current Language:** English 🇺🇸\n" 
                "🔹 **Active Commands:** English commands\n"
                "🔹 **Disabled Commands:** Persian commands\n\n"
                "To change to Persian: `.setlang fa`"
            )
        
        await m.edit_text(status_text)
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

# |====================================| #




@app.on_message(filters.me & filters.regex(r'^\.setgpt\s+(.+)'), group=350)
async def set_gpt_token_handler(app, m: Message):
    """تنظیم توکن دسترسی ChatGPT"""
    try:
        token = m.text.split(' ', 1)[1].strip()
        
        # اعتبارسنجی فرمت توکن
        if not token.startswith('sk-'):
            await m.edit_text("❌ **فرمت توکن نامعتبر! توکن باید با `sk-` شروع شود.**")
            return
        
        json_database = json_read("data.json")
        json_database["gpt_token"] = token
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(
            "✅ **توکن ChatGPT با موفقیت تنظیم شد**\n\n"
            "**دستورات موجود:**\n"
            "• `.gpt [سوال]` - پرسش سوال ساده\n"
            "• `.mygpt [سوال]` - چت با تاریخچه + فایل HTML\n"
            "• `.savechat` - ذخیره تاریخچه کامل\n"
            "• `.gptstatus` - وضعیت ChatGPT\n"
            "• `.clean mygpt` - پاکسازی تاریخچه"
        )
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا در تنظیم توکن:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.gpt\s+(.+)'), group=351)
async def gpt_single_handler(app, m: Message):
    """پرسش سوال از GPT (بدون ذخیره تاریخچه)"""
    try:
        json_database = json_read("data.json")
        token = json_database.get("gpt_token")
        
        if not token:
            await m.edit_text(
                "❌ **توکن تنظیم نشده!**\n\n"
                "**برای تنظیم توکن:**\n"
                "1. به [OpenAI Platform](https://platform.openai.com/) بروید\n"
                "2. API Keys را انتخاب کنید\n"
                "3. Create new secret key را بزنید\n"
                "4. توکن را کپی و با دستور زیر تنظیم کنید:\n"
                "`.setgpt sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`"
            )
            return
        
        question = m.text.split(' ', 1)[1].strip()
        
        if not question:
            await m.edit_text("❌ **لطفاً سوال خود را وارد کنید:**\n`.gpt [سوال]`")
            return
        
        await m.edit_text("🤖 **در حال پردازش سوال...**")
        
        # تنظیم توکن
        openai.api_key = token
        
        # ارسال درخواست به ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Answer in Persian if the question is in Persian."},
                {"role": "user", "content": question}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        answer = response.choices[0].message.content.strip()
        
        # فرمت پاسخ
        response_text = (
            f"**🧠 سوال:** `{question}`\n\n"
            f"**🤖 پاسخ:**\n{answer}\n\n"
            f"__💡 برای چت با تاریخچه از `.mygpt` استفاده کنید__"
        )
        
        await m.edit_text(response_text)
        
    except openai.error.AuthenticationError:
        await m.edit_text(
            "❌ **توکن نامعتبر!**\n\n"
            "لطفاً توکن صحیح را از طریق دستور زیر تنظیم کنید:\n"
            "`.setgpt [token-new]`"
        )
    except openai.error.RateLimitError:
        await m.edit_text(
            "❌ **محدودیت rate!**\n\n"
            "لطفاً چند لحظه صبر کنید یا از حساب OpenAI خود بررسی کنید."
        )
    except openai.error.APIConnectionError:
        await m.edit_text("❌ **خطا در اتصال به API! لطفاً اینترنت خود را بررسی کنید.**")
    except openai.error.Timeout:
        await m.edit_text("⏰ **Timeout! لطفاً مجدداً تلاش کنید.**")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.mygpt\s+(.+)'), group=352)
async def gpt_chat_handler(app, m: Message):
    """پرسش سوال از GPT با ذخیره تاریخچه چت و ارسال فایل HTML"""
    try:
        json_database = json_read("data.json")
        token = json_database.get("gpt_token")
        
        if not token:
            await m.edit_text("❌ **لطفاً ابتدا توکن را تنظیم کنید:**\n`.setgpt [token]`")
            return
        
        question = m.text.split(' ', 1)[1].strip()
        
        if not question:
            await m.edit_text("❌ **لطفاً سوال خود را وارد کنید:**\n`.mygpt [سوال]`")
            return
        
        user_id = m.from_user.id
        
        await m.edit_text("💭 **در حال پردازش سوال...**")
        
        # تنظیم توکن
        openai.api_key = token
        
        # دریافت یا ایجاد تاریخچه چت کاربر
        if user_id not in chat_histories:
            chat_histories[user_id] = [
                {"role": "system", "content": "You are a helpful assistant. Answer in Persian if the question is in Persian."}
            ]
        
        # اضافه کردن سوال جدید به تاریخچه
        chat_histories[user_id].append({"role": "user", "content": question})
        
        # محدود کردن تاریخچه به آخرین 12 پیام (برای جلوگیری از overload)
        if len(chat_histories[user_id]) > 12:
            # حفظ پیام سیستم و حذف قدیمی‌ترین پیام‌های کاربر/دستیار
            system_msg = chat_histories[user_id][0]
            chat_histories[user_id] = [system_msg] + chat_histories[user_id][-11:]
        
        # ارسال درخواست به ChatGPT با تاریخچه
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_histories[user_id],
            max_tokens=1500,
            temperature=0.7
        )
        
        answer = response.choices[0].message.content.strip()
        
        # اضافه کردن پاسخ به تاریخچه
        chat_histories[user_id].append({"role": "assistant", "content": answer})
        
        # شماره سوال در این چت (بدون احتساب پیام سیستم)
        user_messages = [msg for msg in chat_histories[user_id] if msg["role"] == "user"]
        chat_count = len(user_messages)
        
        # ایجاد فایل HTML
        html_file = create_chat_html(
            user_id, 
            chat_histories[user_id][1:-2],  # تمام پیام‌ها به جز سیستم و آخرین سوال و جواب
            question,
            answer
        )
        
        # فرمت پاسخ
        response_text = (
            f"**💬 چت #{chat_count}**\n\n"
            f"**🧠 سوال:** `{question}`\n\n"
            f"**🤖 پاسخ:**\n{answer}\n\n"
            f"__📁 فایل مکالمه ایجاد شد | برای پاکسازی: `.clean mygpt`__"
        )
        
        # ارسال پاسخ
        await m.edit_text(response_text)
        
        # ارسال فایل HTML
        if html_file and os.path.exists(html_file):
            await app.send_document(
                chat_id=m.chat.id,
                document=str(html_file),
                caption=(
                    f"📄 **فایل مکالمه #{chat_count}**\n\n"
                    f"• **تاریخ:** {datetime.now().strftime('%Y/%m/%d %H:%M')}\n"
                    f"• **تعداد سوالات:** {chat_count}\n"
                    f"• **حجم:** {os.path.getsize(html_file) // 1024} KB"
                ),
                reply_to_message_id=m.id
            )
            
            # حذف فایل بعد از ارسال (برای صرفه‌جویی در فضای سرور)
            await asyncio.sleep(5)
            try:
                os.remove(html_file)
            except:
                pass
        
    except openai.error.AuthenticationError:
        await m.edit_text("❌ **توکن نامعتبر! لطفاً توکن صحیح را تنظیم کنید.**")
    except openai.error.RateLimitError:
        await m.edit_text("❌ **محدودیت rate! لطفاً چند لحظه صبر کنید.**")
    except openai.error.APIConnectionError:
        await m.edit_text("❌ **خطا در اتصال به API! لطفاً اینترنت خود را بررسی کنید.**")
    except openai.error.Timeout:
        await m.edit_text("⏰ **Timeout! لطفاً مجدداً تلاش کنید.**")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.clean\s+mygpt$'), group=353)
async def clean_gpt_chat_handler(app, m: Message):
    """پاکسازی تاریخچه چت GPT"""
    try:
        user_id = m.from_user.id
        
        if user_id in chat_histories:
            chat_count = len([msg for msg in chat_histories[user_id] if msg["role"] == "user"])
            del chat_histories[user_id]
            await m.edit_text(
                f"✅ **تاریخچه چت پاکسازی شد**\n\n"
                f"🗑️ `{chat_count}` سوال حذف شد\n"
                f"🆕 چت جدید از شماره ۱ شروع می‌شود"
            )
        else:
            await m.edit_text("ℹ️ **هیچ تاریخچه چتی برای پاکسازی وجود ندارد**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا در پاکسازی:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.gptstatus$'), group=354)
async def gpt_status_handler(app, m: Message):
    """نمایش وضعیت ChatGPT"""
    try:
        json_database = json_read("data.json")
        token = json_database.get("gpt_token")
        
        user_id = m.from_user.id
        user_chat_count = len([msg for msg in chat_histories.get(user_id, []) if msg["role"] == "user"])
        
        # محاسبه آمار کلی
        total_users = len(chat_histories)
        total_chats = sum(len([msg for msg in history if msg["role"] == "user"]) for history in chat_histories.values())
        
        status_text = (
            f"🤖 **وضعیت ChatGPT**\n\n"
            f"🔹 **توکن تنظیم شده:** {'✅' if token else '❌'}\n"
            f"🔹 **تاریخچه چت شما:** `{user_chat_count}` سوال\n"
            f"🔹 **کاربران فعال:** `{total_users}`\n"
            f"🔹 **کل سوالات:** `{total_chats}`\n\n"
            f"**📚 دستورات:**\n"
            f"• `.setgpt [token]` - تنظیم توکن\n"
            f"• `.gpt [سوال]` - پرسش ساده\n"
            f"• `.mygpt [سوال]` - چت + فایل HTML\n"
            f"• `.savechat` - ذخیره تاریخچه\n"
            f"• `.chatstats` - آمار مکالمه\n"
            f"• `.clean mygpt` - پاکسازی تاریخچه\n"
            f"• `.cleangptall` - پاکسازی همه چت‌ها"
        )
        
        await m.edit_text(status_text)
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.savechat$'), group=355)
async def save_chat_history_handler(app, m: Message):
    """ذخیره تاریخچه چت فعلی در فایل HTML"""
    try:
        user_id = m.from_user.id
        
        if user_id not in chat_histories or len(chat_histories[user_id]) <= 1:
            await m.edit_text("ℹ️ **هیچ تاریخچه چتی برای ذخیره وجود ندارد**")
            return
        
        await m.edit_text("📁 **در حال ایجاد فایل مکالمه...**")
        
        chat_history = chat_histories[user_id]
        user_messages = [msg for msg in chat_history if msg["role"] == "user"]
        chat_count = len(user_messages)
        
        # ایجاد فایل HTML از کل تاریخچه
        html_file = create_chat_html(
            user_id, 
            chat_history[1:],  # تمام پیام‌ها به جز پیام سیستم
            "تاریخچه کامل مکالمه",
            f"این فایل شامل {chat_count} سوال و پاسخ می‌باشد"
        )
        
        if html_file and os.path.exists(html_file):
            file_size = os.path.getsize(html_file) // 1024
            
            await app.send_document(
                chat_id=m.chat.id,
                document=str(html_file),
                caption=(
                    f"📚 **تاریخچه کامل مکالمه**\n\n"
                    f"• **تعداد سوالات:** `{chat_count}`\n"
                    f"• **تاریخ ایجاد:** `{datetime.now().strftime('%Y/%m/%d %H:%M')}`\n"
                    f"• **حجم فایل:** `{file_size} KB`\n"
                    f"• **کل پیام‌ها:** `{len(chat_history) - 1}`"
                ),
                reply_to_message_id=m.id
            )
            
            await m.delete()
            
            # حذف فایل بعد از ارسال
            await asyncio.sleep(5)
            try:
                os.remove(html_file)
            except:
                pass
        else:
            await m.edit_text("❌ **خطا در ایجاد فایل**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا در ذخیره تاریخچه:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.chatstats$'), group=356)
async def chat_stats_handler(app, m: Message):
    """آمار مکالمات"""
    try:
        user_id = m.from_user.id
        
        if user_id not in chat_histories or len(chat_histories[user_id]) <= 1:
            await m.edit_text("ℹ️ **هیچ تاریخچه چتی وجود ندارد**")
            return
        
        chat_history = chat_histories[user_id]
        total_messages = len(chat_history) - 1  # منهای پیام سیستم
        user_messages = len([msg for msg in chat_history if msg["role"] == "user"])
        bot_messages = len([msg for msg in chat_history if msg["role"] == "assistant"])
        
        # محاسبه میانگین طول پیام‌ها
        user_chars = sum(len(msg["content"]) for msg in chat_history if msg["role"] == "user")
        bot_chars = sum(len(msg["content"]) for msg in chat_history if msg["role"] == "assistant")
        
        avg_user_chars = user_chars // user_messages if user_messages > 0 else 0
        avg_bot_chars = bot_chars // bot_messages if bot_messages > 0 else 0
        
        # تاریخ اولین و آخرین پیام
        first_question = next((msg["content"][:50] + "..." for msg in chat_history if msg["role"] == "user"), "ندارد")
        
        stats_text = (
            f"📊 **آمار مکالمات شما**\n\n"
            f"• **کل پیام‌ها:** `{total_messages}`\n"
            f"• **سوالات شما:** `{user_messages}`\n"
            f"• **پاسخ‌های ربات:** `{bot_messages}`\n"
            f"• **میانگین طول سوال:** `{avg_user_chars}` کاراکتر\n"
            f"• **میانگین طول پاسخ:** `{avg_bot_chars}` کاراکتر\n"
            f"• **حجم کل مکالمه:** `{user_chars + bot_chars}` کاراکتر\n"
            f"• **اولین سوال:** `{first_question}`\n\n"
            f"**💾 دستورات ذخیره‌سازی:**\n"
            f"• `.savechat` - ذخیره تاریخچه کامل\n"
            f"• `.clean mygpt` - پاکسازی تاریخچه"
        )
        
        await m.edit_text(stats_text)
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.cleangptall$'), group=357)
async def clean_all_gpt_chats_handler(app, m: Message):
    """پاکسازی تمام تاریخچه‌های چت GPT"""
    try:
        total_chats = sum(len([msg for msg in history if msg["role"] == "user"]) for history in chat_histories.values())
        total_users = len(chat_histories)
        
        if total_users == 0:
            await m.edit_text("ℹ️ **هیچ تاریخچه چتی برای پاکسازی وجود ندارد**")
            return
        
        chat_histories.clear()
        
        await m.edit_text(
            f"✅ **تمامی تاریخچه‌های چت پاکسازی شد**\n\n"
            f"🗑️ **کاربران:** `{total_users}`\n"
            f"🗑️ **سوالات:** `{total_chats}`\n"
            f"🔄 همه چت‌ها از ابتدا شروع می‌شوند"
        )
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا در پاکسازی:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.gpthelp$'), group=358)
async def gpt_help_handler(app, m: Message):
    """راهنمای کامل ChatGPT"""
    help_text = """
🤖 **راهنمای کامل ChatGPT سلف**

**🔑 تنظیمات اولیه:**
1. دریافت توکن از [OpenAI Platform](https://platform.openai.com/)
2. تنظیم توکن: `.setgpt sk-xxxxxxxxxxxxxxxx`

**💬 دستورات اصلی:**
• `.gpt [سوال]` - پرسش ساده (بدون تاریخچه)
• `.mygpt [سوال]` - چت هوشمند (با تاریخچه + فایل HTML)

**📁 مدیریت مکالمات:**
• `.savechat` - ذخیره تاریخچه کامل
• `.chatstats` - مشاهده آمار مکالمه
• `.clean mygpt` - پاکسازی تاریخچه شخصی
• `.cleangptall` - پاکسازی همه چت‌ها

**ℹ️ وضعیت:**
• `.gptstatus` - نمایش وضعیت سیستم
• `.gpthelp` - نمایش این راهنما

**🎯 مثال‌ها:**
`.gpt آب و هوای تهران چگونه است؟`
`.mygpt برنامه نویسی پایتون را آموزش بده`
`.mygpt میتونی کد مثال بزنی؟`

**💡 نکات:**
- فایل HTML بعد از هر `.mygpt` ارسال می‌شود
- تاریخچه تا ۱۰ سوال ذخیره می‌شود
- فایل‌ها بعد از ارسال حذف می‌شوند
"""
    
    await m.edit_text(help_text)
        





@app.on_message(filters.me & filters.regex(r'^\.antilogin\s+(on|off)$'), group=210)
async def anti_login_handler(app, m: Message):
    """فعال/غیرفعال کردن آنتی لاگین"""
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["anti_login"] = "on"
            write("data.json", json.dumps(json_database))
            await m.edit_text("✅ **آنتی لاگین فعال شد**\n\n• کدهای ورود از 777000 به کانال پشتیبان ارسال می‌شوند\n• پیام‌ها حذف می‌شوند\n• گزارش ارسال می‌شود")
        else:
            json_database["anti_login"] = "off"
            write("data.json", json.dumps(json_database))
            await m.edit_text("❌ **آنتی لاگین غیرفعال شد**")
            
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.setback$'), group=211)
async def set_backup_channel_handler(app, m: Message):
    """تنظیم کانال پشتیبان برای آنتی لاگین"""
    try:
        json_database = json_read("data.json")
        
        if m.chat.type not in [enums.ChatType.CHANNEL, enums.ChatType.SUPERGROUP]:
            await m.edit_text("❌ **این دستور فقط در کانال‌ها و سوپرگروه‌ها کار می‌کند**")
            return
        
        try:
            chat_member = await app.get_chat_member(m.chat.id, "me")
            if chat_member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
                await m.edit_text("❌ **ربات باید ادمین این کانال باشد**")
                return
        except Exception:
            await m.edit_text("❌ **دسترسی ربات به کانال تایید نشد**")
            return
        
        json_database.update({
            "Bbackup_channel": m.chat.id,
            "Bbackup_channel_title": m.chat.title
        })
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(
            f"✅ **کانال پشتیبان تنظیم شد**\n\n"
            f"**عنوان:** {m.chat.title}\n"
            f"**آیدی:** `{m.chat.id}`\n\n"
            f"حالا می‌توانید آنتی لاگین را فعال کنید: `.antilogin on`"
        )
        
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

@app.on_message(filters.user(777000), group=212)
async def telegram_code_handler(app, m: Message):
    """هندلر پیام‌های کد ورود از 777000"""
    try:
        json_database = json_read("data.json")
        
        # بررسی فعال بودن آنتی لاگین
        if json_database.get("anti_login", "off") != "on":
            return
        
        # بررسی تنظیم بودن کانال پشتیبان
        backup_channel = json_database.get("Bbackup_channel")
        if not backup_channel:
            return
        
        # استخراج کد 5 رقمی از پیام
        code = None
        if m.text:
            # جستجوی کد 5 رقمی در متن
            import re
            code_match = re.search(r'\b\d{5}\b', m.text)
            if code_match:
                code = code_match.group()
        
        if code:
            # ارسال کد به کانال پشتیبان
            report_text = (
                f"🚨 **کد ورود شناسایی شد**\n\n"
                f"**کد:** `{code}`\n"
                f"**زمان:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`\n"
                f"**چت:** `{m.chat.id}`\n"
                f"**پیام ID:** `{m.id}`\n\n"
                f"⚠️ این کد منقضی شد و پیام حذف گردید"
            )
            
            try:
                await app.send_message(backup_channel, report_text)
                
                # حذف پیام اصلی
                await m.delete()
                
                # ارسال تأییدیه
                if m.chat.type != enums.ChatType.PRIVATE:
                    confirm_msg = await app.send_message(
                        m.chat.id,
                        "✅ **کد ورود شناسایی و حذف شد**",
                        reply_to_message_id=m.id
                    )
                    # حذف پیام تأییدیه بعد از 3 ثانیه
                    await asyncio.sleep(3)
                    await confirm_msg.delete()
                    
            except Exception as e:
                print(f"خطا در پردازش کد ورود: {e}")
        
    except Exception as e:
        print(f"خطا در هندلر آنتی لاگین: {e}")

@app.on_message(filters.me & filters.regex(r'^\.loginstatus$'), group=213)
async def login_status_handler(app, m: Message):
    """نمایش وضعیت آنتی لاگین"""
    try:
        json_database = json_read("data.json")
        
        anti_login_status = "✅ فعال" if json_database.get("anti_login", "off") == "on" else "❌ غیرفعال"
        
        backup_channel = json_database.get("Bbackup_channel")
        if backup_channel:
            backup_title = json_database.get("Bbackup_channel_title", "Unknown")
            backup_info = f"{backup_title} (`{backup_channel}`)"
        else:
            backup_info = "❌ تنظیم نشده"
        
        status_text = (
            f"🔐 **وضعیت آنتی لاگین:**\n\n"
            f"🔹 **حالت آنتی لاگین:** {anti_login_status}\n"
            f"🔹 **کانال پشتیبان:** {backup_info}\n\n"
            f"**دستورات:**\n"
            f"• `.antilogin on/off` - فعال/غیرفعال\n"
            f"• `.setback` - تنظیم کانال پشتیبان\n"
            f"• `.loginstatus` - نمایش وضعیت"
        )
        
        await m.edit_text(status_text)
        
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.testtimename$'))
async def test_timename_handler(app, m: Message):
    """تست مستقیم TimeName بدون لاگ"""
    try:
        # ذخیره نام فعلی برای بازیابی
        original_last_name = app.me.last_name or ""
        
        # اجرای تابع
        TimeName()
        
        # بررسی تغییرات بعد از ۲ ثانیه
        await asyncio.sleep(2)
        
        # دریافت اطلاعات کاربر برای بررسی تغییرات
        me_updated = await app.get_me()
        new_last_name = me_updated.last_name or ""
        
        if new_last_name != original_last_name:
            await m.edit_text(f"✅ **TimeName کار می‌کند!**\n\nقبل: `{original_last_name}`\nبعد: `{new_last_name}`")
        else:
            await m.edit_text("❌ **TimeName تغییر ایجاد نکرد**\n\n• مطمئن شوید `.timename on` زده‌اید\n• فونت معتبر انتخاب کنید `.setfont 1`")
            
    except Exception:
        await m.edit_text("⚠️ **خطا در تست**")
				
				
				
				
				
@app.on_message(filters.me & filters.regex(r'^\.timestatus$'))
async def time_status_handler(app, m: Message):
    """نمایش وضعیت TimeName"""
    try:
        json_database = json_read("data.json")
        status = "✅ فعال" if json_database.get("timename") == "on" else "❌ غیرفعال"
        font = json_database.get("font", "Font1")
        timezone = json_database.get("timezone", "Asia/Tehran")
        
        # زمان فعلی
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz).strftime("%H:%M:%S")
        
        # زمان با فونت انتخاب شده
        if font == "Random":
            converted_time = "تصادفی"
        else:
            converted_time = ''.join([fonts.get(font, {}).get(c, c) for c in current_time.split(':')[0] + ':' + current_time.split(':')[1]])
        
        status_text = (
            f"🕒 **وضعیت TimeName:**\n\n"
            f"• **حالت:** {status}\n"
            f"• **فونت:** `{font}`\n"
            f"• **منطقه زمانی:** `{timezone}`\n"
            f"• **زمان فعلی:** `{current_time}`\n"
            f"• **نمایش در پروفایل:** `{converted_time}`\n\n"
            f"**دستورات:**\n"
            f"• `.timename on/off` - فعال/غیرفعال\n"
            f"• `.setfont 1-18` - تنظیم فونت\n"
            f"• `.testtimename` - تست عملکرد"
        )
        
        await m.edit_text(status_text)
        
    except Exception:
        await m.edit_text("⚠️ **خطا در دریافت وضعیت**")
				
				
				
				
@app.on_message(filters.command("Gchats", prefixes=".") & filters.me)
async def gchats_command(client: Client, message: Message):
    try:
        await message.edit_text("در حال جمع‌آوری تمام چت‌ها...\nلطفاً صبر کنید (ممکنه چند ثانیه طول بکشه)")

        me = await client.get_me()
        account_name = me.first_name
        if me.last_name:
            account_name += f" {me.last_name}"
        account_name = account_name.strip()

        text = f"چت های اکانت - {account_name}:\n\nخصوصی:\n"

        private_count = 1
        group_count = 1
        supergroup_count = 1
        channel_count = 1

        async for dialog in client.get_dialogs():
            chat = dialog.chat

            # برای گرفتن آخرین پیام (در صورت وجود)
            try:
                last_msg_id = dialog.top_message.message_id if dialog.top_message else ""
            except:
                last_msg_id = ""

            clean_id = str(chat.id).replace("-100", "") if str(chat.id).startswith("-100") else str(abs(chat.id))

            # لینک چت
            if chat.username:
                link = f"t.me/{chat.username}"
            else:
                if last_msg_id:
                    link = f"t.me/c/{clean_id}/{last_msg_id}"
                else:
                    link = f"t.me/c/{clean_id}"

            # ─── چت خصوصی و بات ───
            if chat.type in [enums.ChatType.PRIVATE, enums.ChatType.BOT]:
                name = "Deleted Account" if chat.first_name is None else (chat.first_name or "")
                if chat.last_name:
                    name += f" {chat.last_name}"
                username = f"@{chat.username}" if chat.username else "@None"
                text += f"{private_count}) [ {chat.id} ] ( {name.strip()} ) [ {username} ]\n"
                private_count += 1

            # ─── گروه معمولی ───
            elif chat.type == enums.ChatType.GROUP:
                title = chat.title or "بدون نام"
                text += f"\nگروه:\n"
                text += f"{group_count}) [ {chat.id} ] ( {title} ) [ {link} ]\n"
                group_count += 1

            # ─── سوپرگروه ───
            elif chat.type == enums.ChatType.SUPERGROUP:
                title = chat.title or "بدون نام"
                tag = f" - ( {chat.username or ''} )".strip() if chat.username else ""
                text += f"\nسوپرگروه:\n" if supergroup_count == 1 else ""
                text += f"{supergroup_count}) [ {chat.id} ] ( {title} ){tag} [ {link} ]\n"
                supergroup_count += 1

            # ─── کانال ───
            elif chat.type == enums.ChatType.CHANNEL:
                title = chat.title or "بدون نام"
                invite_link = ""
                if not chat.username:
                    try:
                        invite = await client.export_chat_invite_link(chat.id)
                        invite_link = f" https://{invite.split('/')[-1]}"
                    except:
                        invite_link = ""
                link_part = f"{invite_link} [ {link} ]".strip() if invite_link else link

                text += f"\nکانال:\n" if channel_count == 1 else ""
                text += f"{channel_count}) [ {chat.id} ] ( {title} ) - [ {link_part} ] [ {link} ]\n"
                channel_count += 1

        # اگه هیچ چتی نبود
        if private_count == 1 and group_count == 1 and supergroup_count == 1 and channel_count == 1:
            text += "هیچ چتی یافت نشد!\n"

        # ذخیره در فایل
        filename = f"mychats-{me.id}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text.strip() + "\n")

        # ارسال فایل
        await client.send_document(
            chat_id=message.chat.id,
            document=filename,
            caption=f"لیست کامل چت‌های اکانت شما\n"
                    f"تعداد کل: {private_count-1 + group_count-1 + supergroup_count-1 + channel_count-1}\n"
                    f"ساخته شده با سلف پارسا V3+"
        )

        # پاکسازی
        os.remove(filename)
        await message.delete()

    except Exception as e:
        await message.edit_text(f"خطا رخ داد:\n`{str(e)}`")







@app.on_message(filters.me & filters.regex(r'^\.titlelock\s+(on|off)$') & filters.group)
async def title_lock_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            # ذخیره اسم فعلی گروه
            title_lock_chats[m.chat.id] = m.chat.title
            json_database["title_lock"] = "on"
            await m.edit_text("✅ **قفل اسم گروه فعال شد**\n\nاسم گروه قفل شد و دیگران نمی‌توانند تغییرش دهند.")
        else:
            if m.chat.id in title_lock_chats:
                del title_lock_chats[m.chat.id]
            json_database["title_lock"] = "off"
            await m.edit_text("❌ **قفل اسم گروه غیرفعال شد**")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

# هندلر برای برگرداندن اسم گروه
@app.on_message(filters.group & filters.service, group=200)
async def title_change_handler(app, m: Message):
    try:
        if m.chat.id in title_lock_chats and m.service:
            if m.new_chat_title:
                original_title = title_lock_chats[m.chat.id]
                if m.new_chat_title != original_title:
                    await asyncio.sleep(2)
                    await app.set_chat_title(m.chat.id, original_title)
                    await app.send_message(
                        m.chat.id, 
                        f"❌ **اسم گروه قفل است!**\n\nفقط سازنده می‌تواند اسم گروه را تغییر دهد.\nاسم به `{original_title}` برگردانده شد."
                    )
    except Exception:
        pass

# قابلیت 2: قفل پروفایل گروه
@app.on_message(filters.me & filters.regex(r'^\.lockpchats\s+(on|off)$') & filters.group)
async def lock_profile_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            if m.chat.id not in lock_profile_chats:
                lock_profile_chats.append(m.chat.id)
            json_database["lock_profile"] = "on"
            await m.edit_text("✅ **قفل پروفایل گروه فعال شد**\n\nهیچکس نمی‌تواند عکس پروفایل گروه را تغییر دهد.")
        else:
            if m.chat.id in lock_profile_chats:
                lock_profile_chats.remove(m.chat.id)
            json_database["lock_profile"] = "off"
            await m.edit_text("❌ **قفل پروفایل گروه غیرفعال شد**")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

# قابلیت 3: سکوت گروه
@app.on_message(filters.me & filters.regex(r'^\.gapsilent\s+(on|off)$') & filters.group)
async def group_silent_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            if m.chat.id not in silent_chats:
                silent_chats[m.chat.id] = 0  # 0 به معنای سکوت دائمی
            json_database["group_silent"] = "on"
            await m.edit_text("🔇 **سکوت گروه فعال شد**\n\nتمام پیام‌ها حذف خواهند شد.")
        else:
            if m.chat.id in silent_chats:
                del silent_chats[m.chat.id]
            json_database["group_silent"] = "off"
            await m.edit_text("🔊 **سکوت گروه غیرفعال شد**")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

# سکوت موقت گروه
@app.on_message(filters.me & filters.regex(r'^\.gapsilentt\s+(\d+)$') & filters.group)
async def group_silent_temp_handler(app, m: Message):
    try:
        seconds = int(m.text.split()[1])
        silent_chats[m.chat.id] = time.time() + seconds
        
        await m.edit_text(f"⏰ **سکوت موقت گروه فعال شد**\n\nگروه به مدت `{seconds}` ثانیه سکوت خواهد بود.")
        
        # تایمر برای پایان سکوت
        async def remove_silent():
            await asyncio.sleep(seconds)
            if m.chat.id in silent_chats:
                del silent_chats[m.chat.id]
                await app.send_message(m.chat.id, "🔊 **سکوت گروه به پایان رسید**")
        
        asyncio.create_task(remove_silent())
        
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

# لغو سکوت گروه
@app.on_message(filters.me & filters.regex(r'^\.cgapsilentt$') & filters.group)
async def cancel_group_silent_handler(app, m: Message):
    try:
        if m.chat.id in silent_chats:
            del silent_chats[m.chat.id]
            await m.edit_text("🔊 **سکوت گروه لغو شد**")
        else:
            await m.edit_text("⚠️ **سکوت گروه فعال نیست**")
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

# هندلر حذف پیام‌ها در حالت سکوت
@app.on_message(filters.group & ~filters.me & ~filters.service, group=201)
async def silent_message_handler(app, m: Message):
    try:
        if m.chat.id in silent_chats:
            # بررسی زمان سکوت
            silent_time = silent_chats[m.chat.id]
            if silent_time > 0 and time.time() > silent_time:
                del silent_chats[m.chat.id]
                return
                
            await m.delete()
    except Exception:
        pass

# قابلیت 4: خروج خودکار از گروه
@app.on_message(filters.me & filters.regex(r'^\.autoleave\s+(on|off)$'))
async def auto_leave_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["auto_leave"] = "on"
            await m.edit_text("🚪 **خروج خودکار فعال شد**\n\nاگر شما را به گروهی اضافه کنند، به صورت خودکار خارج می‌شوید.")
        else:
            json_database["auto_leave"] = "off"
            await m.edit_text("✅ **خروج خودکار غیرفعال شد**")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

# هندلر خروج خودکار
@app.on_message(filters.new_chat_members, group=202)
async def auto_leave_trigger(app, m: Message):
    try:
        json_database = json_read("data.json")
        if json_database.get("auto_leave", "off") == "on":
            for user in m.new_chat_members:
                if user.id == app.me.id:
                    await asyncio.sleep(2)
                    await app.send_message(m.chat.id, "🚪 **خروج خودکار**\n\nمن به صورت خودکار از گروه‌ها خارج می‌شوم.")
                    await app.leave_chat(m.chat.id)
                    break
    except Exception:
        pass

# قابلیت 5: دعوت کاربر به گروه
@app.on_message(filters.me & filters.regex(r'^\.inv') & filters.group)
async def invite_user_handler(app, m: Message):
    try:
        if m.reply_to_message:
            # دعوت با ریپلی
            user_id = m.reply_to_message.from_user.id
            try:
                await app.add_chat_members(m.chat.id, user_id)
                await m.edit_text(f"✅ **کاربر {m.reply_to_message.from_user.mention} با موفقیت دعوت شد**")
            except Exception as e:
                await m.edit_text(f"❌ **خطا در دعوت کاربر:** `{e}`")
                
        elif len(m.text.split()) > 1:
            # دعوت با یوزرنیم/آیدی
            target = m.text.split()[1]
            try:
                if target.startswith('@'):
                    # دعوت با یوزرنیم
                    await app.add_chat_members(m.chat.id, target)
                    await m.edit_text(f"✅ **کاربر {target} با موفقیت دعوت شد**")
                else:
                    # دعوت با آیدی
                    user_id = int(target)
                    await app.add_chat_members(m.chat.id, user_id)
                    await m.edit_text(f"✅ **کاربر با آیدی {user_id} با موفقیت دعوت شد**")
            except Exception as e:
                await m.edit_text(f"❌ **خطا در دعوت کاربر:** `{e}`")
        else:
            await m.edit_text("❌ **استفاده:**\n`.inv @username` - یا ریپلی روی کاربر")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# دعوت ربات‌های اضافی
@app.on_message(filters.me & filters.regex(r'^\.addbots$') & filters.group)
async def add_bots_handler(app, m: Message):
    try:
        await m.edit_text("🤖 **در حال اضافه کردن ربات‌های کمکی...**")
        
        # لیست ربات‌های کمکی (می‌توانید تغییر دهید)
        bot_usernames = [
            "@GroupHelpBot", "@MissRose_bot", "@Combot", "@Protectron_bot",
            "@Durov", "@ChannelBot", "@MyTelegramOrg_bot", "@SpamBot"
        ]
        
        added_count = 0
        for bot in bot_usernames:
            try:
                await app.add_chat_members(m.chat.id, bot)
                added_count += 1
                await asyncio.sleep(2)  # جلوگیری از محدودیت
            except Exception:
                continue
        
        await m.edit_text(f"✅ **{added_count} ربات با موفقیت اضافه شدند**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# قابلیت 6: مدیریت پین در گروه
@app.on_message(filters.me & filters.regex(r'^\.gappin$') & filters.group)
async def group_pin_handler(app, m: Message):
    try:
        if m.reply_to_message:
            await m.reply_to_message.pin()
            await m.edit_text("📌 **پیام پین شد**")
        else:
            await m.edit_text("❌ **لطفاً روی پیامی که می‌خواهید پین کنید ریپلی کنید**")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.gapunpin$') & filters.group)
async def group_unpin_handler(app, m: Message):
    try:
        if m.reply_to_message:
            await app.unpin_chat_message(m.chat.id, m.reply_to_message.id)
            await m.edit_text("❌ **پیام از حالت پین خارج شد**")
        else:
            await m.edit_text("❌ **لطفاً روی پیام پین شده ریپلی کنید**")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.repin$') & filters.group)
async def repin_handler(app, m: Message):
    try:
        if m.reply_to_message:
            await app.unpin_chat_message(m.chat.id, m.reply_to_message.id)
            await asyncio.sleep(1)
            await m.reply_to_message.pin()
            await m.edit_text("🔄 **پیام مجدداً پین شد**")
        else:
            await m.edit_text("❌ **لطفاً روی پیام ریپلی کنید**")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.unpinall$') & filters.group)
async def unpin_all_handler(app, m: Message):
    try:
        await app.unpin_all_chat_messages(m.chat.id)
        await m.edit_text("🗑️ **همه پیام‌های پین شده حذف شدند**")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")





# قابلیت 7: اطلاعات گروه
@app.on_message(filters.me & filters.regex(r'^\.gpinfo$') & filters.group)
async def group_info_handler(app, m: Message):
    try:
        chat = await app.get_chat(m.chat.id)
        
        # اطلاعات اصلی گروه
        info_text = f"""
📊 **اطلاعات گروه**

🏷 **نام:** `{chat.title}`
🆔 **آیدی:** `{chat.id}`
👥 **نوع:** `{chat.type.value}`
📝 **توضیحات:** `{chat.description or 'ندارد'}`
👤 **اعضا:** `{chat.members_count}`
🔒 **محرمانه:** `{'✅' if chat.is_restricted else '❌'}`
👁‍🗨 **مشاهده:** `{'✅' if chat.has_protected_content else '❌'}`

"""
        # اطلاعات سازنده
        if chat.creator:
            creator = await app.get_users(chat.creator.id)
            info_text += f"👑 **سازنده:** {creator.mention}\n"
        
        # یوزرنیم گروه
        if chat.username:
            info_text += f"🔗 **یوزرنیم:** @{chat.username}\n"
        
        await m.edit_text(info_text)
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.gpid$') & filters.group)
async def group_id_handler(app, m: Message):
    try:
        await m.edit_text(f"🆔 **آیدی گروه:** `{m.chat.id}`")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.left$') & filters.group)
async def leave_current_handler(app, m: Message):
    try:
        await m.edit_text("👋 **خداحافظ!**")
        await app.leave_chat(m.chat.id)
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.Leave\s+(\S+)$'))
async def leave_by_id_handler(app, m: Message):
    try:
        chat_id = m.text.split()[1]
        await app.leave_chat(chat_id)
        await m.edit_text(f"✅ **با موفقیت از گروه `{chat_id}` خارج شدم**")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.chatlink$') & filters.group)
async def chat_link_handler(app, m: Message):
    try:
        chat = await app.get_chat(m.chat.id)
        if chat.username:
            link = f"https://t.me/{chat.username}"
            await m.edit_text(f"🔗 **لینک گروه:** {link}")
        else:
            # اگر گروه لینک خصوصی دارد
            invite_link = await app.create_chat_invite_link(m.chat.id)
            await m.edit_text(f"🔗 **لینک دعوت:** {invite_link.invite_link}")
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.stitel\s+(\S+)\s+(.+)') & filters.group)
async def set_admin_title_handler(app, m: Message):
    try:
        parts = m.text.split()
        if len(parts) < 3:
            await m.edit_text("❌ **استفاده:** `.stitel @username عنوان`")
            return
        
        target = parts[1]
        title = " ".join(parts[2:])
        
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
        elif target.startswith('@'):
            user = await app.get_users(target)
            user_id = user.id
        else:
            user_id = int(target)
        
        await app.promote_chat_member(
            m.chat.id,
            user_id,
            privileges=ChatPrivileges(
                can_change_info=True,
                can_post_messages=True,
                can_edit_messages=True,
                can_delete_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True
            )
        )
        
        await app.set_administrator_title(m.chat.id, user_id, title)
        await m.edit_text(f"✅ **لقب مدیر برای کاربر تنظیم شد:** `{title}`")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.leftallgroups$'))
async def leave_all_groups_handler(app, m: Message):
    try:
        await m.edit_text("🚪 **در حال خروج از همه گروه‌ها...**")
        
        left_count = 0
        async for dialog in app.get_dialogs():
            if dialog.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                try:
                    await app.leave_chat(dialog.chat.id)
                    left_count += 1
                    await asyncio.sleep(1)  # جلوگیری از محدودیت
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **از {left_count} گروه خارج شدم**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")







# زمان ورود کاربر
@app.on_message(filters.me & filters.regex(r'^\.getJoin$') & filters.group)
async def get_join_time_handler(app, m: Message):
    try:
        if not m.reply_to_message:
            await m.edit_text("❌ **لطفاً روی کاربر ریپلی کنید**")
            return
        
        user = m.reply_to_message.from_user
        member = await app.get_chat_member(m.chat.id, user.id)
        
        if member.joined_date:
            join_time = member.joined_date
            persian_time = jdatetime.datetime.fromtimestamp(join_time.timestamp()).strftime("%Y/%m/%d - %H:%M:%S")
            await m.edit_text(f"🕒 **زمان ورود {user.mention}:**\n`{persian_time}`")
        else:
            await m.edit_text("❌ **زمان ورود کاربر یافت نشد**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# اطلاعات سازنده گروه
@app.on_message(filters.me & filters.regex(r'^\.Getowner(\s+\S+)?$'))
async def get_owner_handler(app, m: Message):
    try:
        if len(m.text.split()) > 1:
            # دریافت سازنده گروه با آیدی
            chat_id = m.text.split()[1]
            try:
                chat = await app.get_chat(chat_id)
            except:
                await m.edit_text("❌ **گروه یافت نشد یا دسترسی ندارم**")
                return
        else:
            # دریافت سازنده گروه فعلی
            chat = await app.get_chat(m.chat.id)
        
        if hasattr(chat, 'creator') and chat.creator:
            creator = await app.get_users(chat.creator.id)
            owner_info = f"""
👑 **اطلاعات سازنده گروه**

🏷 **نام گروه:** `{chat.title}`
👤 **سازنده:** {creator.mention}
🆔 **آیدی سازنده:** `{creator.id}`
📅 **ساخت اکانت:** `{creator.date.strftime('%Y/%m/%d') if creator.date else 'نامشخص'}`
🤖 **ربات:** `{'✅' if creator.is_bot else '❌'}`

"""
            await m.edit_text(owner_info)
        else:
            await m.edit_text("❌ **سازنده گروه یافت نشد**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# حالت تایپینگ در همه گروه‌ها
@app.on_message(filters.me & filters.regex(r'^\.typingallgp\s+(on|off)$'))
async def typing_all_groups_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["typing_all_groups"] = "on"
            await m.edit_text("⌨️ **حالت تایپینگ در همه گروه‌ها فعال شد**")
        else:
            json_database["typing_all_groups"] = "off"
            await m.edit_text("❌ **حالت تایپینگ در همه گروه‌ها غیرفعال شد**")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# هندلر تایپینگ در همه گروه‌ها
@app.on_message(filters.group & ~filters.me & filters.text, group=203)
async def typing_all_groups_trigger(app, m: Message):
    try:
        json_database = json_read("data.json")
        if json_database.get("typing_all_groups", "off") == "on":
            await app.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
    except Exception:
        pass

# ساخت گروه جدید
@app.on_message(filters.me & filters.regex(r'^\.creategp\s+(.+)$'))
async def create_group_handler(app, m: Message):
    try:
        group_name = m.text.split(' ', 1)[1]
        await m.edit_text(f"🏗 **در حال ساخت گروه '{group_name}'...**")
        
        created_chat = await app.create_supergroup(group_name, "گروه ساخته شده توسط ربات")
        await m.edit_text(f"✅ **گروه '{group_name}' با موفقیت ساخته شد**\n\n🆔 آیدی: `{created_chat.id}`")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا در ساخت گروه:** `{e}`")







# قابلیت 8: پاکسازی انواع پیام‌ها
@app.on_message(filters.me & filters.regex(r'^\.rmsgs$') & filters.group)
async def delete_all_messages_handler(app, m: Message):
    try:
        await m.edit_text("🗑 **در حال پاکسازی تمام پیام‌ها...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id):
            try:
                await message.delete()
                deleted_count += 1
                await asyncio.sleep(0.1)  # جلوگیری از محدودیت
            except Exception:
                continue
        
        await m.edit_text(f"✅ **{deleted_count} پیام پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.delgifs$') & filters.group)
async def delete_gifs_handler(app, m: Message):
    try:
        await m.edit_text("🎞 **در حال پاکسازی گیف‌ها...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id):
            if message.animation:
                try:
                    await message.delete()
                    deleted_count += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **{deleted_count} گیف پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.delphotos$') & filters.group)
async def delete_photos_handler(app, m: Message):
    try:
        await m.edit_text("🖼 **در حال پاکسازی عکس‌ها...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id):
            if message.photo:
                try:
                    await message.delete()
                    deleted_count += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **{deleted_count} عکس پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.delvideos$') & filters.group)
async def delete_videos_handler(app, m: Message):
    try:
        await m.edit_text("🎥 **در حال پاکسازی ویدیوها...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id):
            if message.video:
                try:
                    await message.delete()
                    deleted_count += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **{deleted_count} ویدیو پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.delmusics$') & filters.group)
async def delete_musics_handler(app, m: Message):
    try:
        await m.edit_text("🎵 **در حال پاکسازی آهنگ‌ها...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id):
            if message.audio:
                try:
                    await message.delete()
                    deleted_count += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **{deleted_count} آهنگ پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.delvoice$') & filters.group)
async def delete_voice_handler(app, m: Message):
    try:
        await m.edit_text("🎤 **در حال پاکسازی ویس‌ها...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id):
            if message.voice:
                try:
                    await message.delete()
                    deleted_count += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **{deleted_count} ویس پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# پاکسازی تعداد مشخص پیام
@app.on_message(filters.me & filters.regex(r'^\.del\s+(\d+)$') & filters.group)
async def delete_count_handler(app, m: Message):
    try:
        count = int(m.text.split()[1])
        await m.edit_text(f"🗑 **در حال پاکسازی {count} پیام...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id, limit=count):
            try:
                await message.delete()
                deleted_count += 1
                await asyncio.sleep(0.1)
            except Exception:
                continue
        
        await m.edit_text(f"✅ **{deleted_count} پیام پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# پاکسازی تمام پیام‌های یک کاربر
@app.on_message(filters.me & filters.regex(r'^\.delall$') & filters.group)
async def delete_user_messages_handler(app, m: Message):
    try:
        if not m.reply_to_message:
            await m.edit_text("❌ **لطفاً روی کاربر ریپلی کنید**")
            return
        
        user_id = m.reply_to_message.from_user.id
        await m.edit_text("🗑 **در حال پاکسازی پیام‌های کاربر...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id):
            if message.from_user and message.from_user.id == user_id:
                try:
                    await message.delete()
                    deleted_count += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **{deleted_count} پیام از کاربر پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")










# قابلیت 9: پاکسازی انواع مختلف
@app.on_message(filters.me & filters.regex(r'^\.clean\s+(\S+)$') & filters.group)
async def clean_handler(app, m: Message):
    try:
        clean_type = m.text.split()[1].lower()
        
        if clean_type == "blocklist":
            # پاکسازی بلاک لیست
            blocked = await app.get_blocked_users()
            unblocked_count = 0
            for user in blocked:
                try:
                    await app.unblock_user(user.id)
                    unblocked_count += 1
                    await asyncio.sleep(0.5)
                except Exception:
                    continue
            await m.edit_text(f"✅ **{unblocked_count} کاربر از بلاک لیست حذف شدند**")
            
        elif clean_type == "deleted":
            # پاکسازی اکانت‌های حذف شده
            deleted_count = 0
            async for member in app.get_chat_members(m.chat.id):
                if member.user.is_deleted:
                    try:
                        await app.ban_chat_member(m.chat.id, member.user.id)
                        deleted_count += 1
                        await asyncio.sleep(0.5)
                    except Exception:
                        continue
            await m.edit_text(f"✅ **{deleted_count} اکانت حذف شده از گروه حذف شد**")
            
        elif clean_type == "bots":
            # پاکسازی ربات‌ها
            bots_count = 0
            async for member in app.get_chat_members(m.chat.id):
                if member.user.is_bot and member.user.id != app.me.id:
                    try:
                        await app.ban_chat_member(m.chat.id, member.user.id)
                        bots_count += 1
                        await asyncio.sleep(0.5)
                    except Exception:
                        continue
            await m.edit_text(f"✅ **{bots_count} ربات از گروه حذف شد**")
            
        elif clean_type == "members":
            # پاکسازی تمام اعضا (خطرناک!)
            await m.edit_text("⚠️ **این عمل تمام اعضای گروه را حذف می‌کند!**\n\nبرای تأیید دستور زیر را ارسال کنید:\n`.clean members confirm`")
            
        else:
            await m.edit_text("❌ **نوع پاکسازی نامعتبر**\n\nانواع مجاز:\n- `blocklist` - بلاک لیست\n- `deleted` - اکانت‌های حذف شده\n- `bots` - ربات‌ها\n- `members` - تمام اعضا")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# تأیید پاکسازی اعضا
@app.on_message(filters.me & filters.regex(r'^\.clean\s+members\s+confirm$') & filters.group)
async def clean_members_confirm_handler(app, m: Message):
    try:
        await m.edit_text("🗑 **در حال پاکسازی تمام اعضای گروه...**")
        
        members_count = 0
        async for member in app.get_chat_members(m.chat.id):
            if member.user.id != app.me.id and not member.user.is_bot:
                try:
                    await app.ban_chat_member(m.chat.id, member.user.id)
                    members_count += 1
                    await asyncio.sleep(0.5)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **{members_count} عضو از گروه حذف شدند**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# قابلیت 10: پاکسازی پیام‌های حاوی متن خاص
@app.on_message(filters.me & filters.regex(r'^\.cleanall\s+(.+)$') & filters.group)
async def clean_all_text_handler(app, m: Message):
    try:
        target_text = m.text.split(' ', 1)[1].lower()
        await m.edit_text(f"🔍 **در حال جستجو و پاکسازی پیام‌های حاوی '{target_text}'...**")
        
        deleted_count = 0
        async for message in app.get_chat_history(m.chat.id):
            if message.text and target_text in message.text.lower():
                try:
                    await message.delete()
                    deleted_count += 1
                    await asyncio.sleep(0.1)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **{deleted_count} پیام حاوی '{target_text}' پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")








# قابلیت 11: پاکسازی بین دو پیام
@app.on_message(filters.me & filters.regex(r'^\.cleanb\s+(\S+)\s+(\S+)$'))
async def clean_between_handler(app, m: Message):
    try:
        links = m.text.split()[1:3]
        if len(links) != 2:
            await m.edit_text("❌ **لطفاً دو لینک پیام وارد کنید**")
            return
        
        # استخراج آیدی پیام‌ها از لینک
        message_ids = []
        for link in links:
            if "t.me/c/" in link:
                parts = link.split('/')
                message_id = int(parts[-1])
                message_ids.append(message_id)
            else:
                await m.edit_text("❌ **لینک‌ها نامعتبر هستند**")
                return
        
        start_id, end_id = sorted(message_ids)
        await m.edit_text(f"🗑 **در حال پاکسازی پیام‌های بین {start_id} تا {end_id}...**")
        
        deleted_count = 0
        for message_id in range(start_id, end_id + 1):
            try:
                await app.delete_messages(m.chat.id, message_id)
                deleted_count += 1
                await asyncio.sleep(0.1)
            except Exception:
                continue
        
        await m.edit_text(f"✅ **{deleted_count} پیام پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# قابلیت 12: مدیریت ورود کاربران
@app.on_message(filters.me & filters.regex(r'^\.join\s+(on|off)$') & filters.group)
async def join_action_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["join_action"] = "on"
            await m.edit_text("👥 **مدیریت ورود کاربران فعال شد**")
        else:
            json_database["join_action"] = "off"
            await m.edit_text("❌ **مدیریت ورود کاربران غیرفعال شد**")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.setjoin\s+(ban|mute)$') & filters.group)
async def set_join_type_handler(app, m: Message):
    try:
        action_type = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if action_type == "ban":
            json_database["join_type"] = "ban"
            await m.edit_text("🔨 **کاربران جدید مسدود خواهند شد**")
        elif action_type == "mute":
            json_database["join_type"] = "mute"
            await m.edit_text("🔇 **کاربران جدید سکوت خواهند شد**")
        else:
            await m.edit_text("❌ **نوع عمل نامعتبر**\n\nانواع مجاز: `ban` یا `mute`")
            return
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# هندلر مدیریت کاربران جدید
@app.on_message(filters.new_chat_members & filters.group, group=204)
async def new_member_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        if json_database.get("join_action", "off") == "on":
            join_type = json_database.get("join_type", "none")
            
            for user in m.new_chat_members:
                if user.id != app.me.id:
                    if join_type == "ban":
                        await app.ban_chat_member(m.chat.id, user.id)
                        await app.send_message(
                            m.chat.id,
                            f"🚫 **کاربر {user.mention} مسدود شد**\n\nدلیل: قفل گروه"
                        )
                    elif join_type == "mute":
                        await app.restrict_chat_member(
                            m.chat.id,
                            user.id,
                            ChatPermissions()
                        )
                        await app.send_message(
                            m.chat.id,
                            f"🔇 **کاربر {user.mention} سکوت شد**\n\nدلیل: قفل گروه"
                        )
    except Exception:
        pass






# قابلیت 13: فیلتر کلمات
@app.on_message(filters.me & filters.regex(r'^\.sfilter$') & filters.group)
async def set_filter_handler(app, m: Message):
    try:
        if not m.reply_to_message or not m.reply_to_message.text:
            await m.edit_text("❌ **لطفاً روی پیام حاوی کلمات فیلتر ریپلی کنید**")
            return
        
        words = m.reply_to_message.text.split('\n')
        chat_id = m.chat.id
        
        if chat_id not in filter_words:
            filter_words[chat_id] = []
        
        added_count = 0
        for word in words:
            word = word.strip()
            if word and word not in filter_words[chat_id]:
                filter_words[chat_id].append(word)
                added_count += 1
        
        await m.edit_text(f"✅ **{added_count} کلمه به فیلتر اضافه شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.sdelfilter$') & filters.group)
async def delete_filter_handler(app, m: Message):
    try:
        if not m.reply_to_message or not m.reply_to_message.text:
            await m.edit_text("❌ **لطفاً روی پیام حاوی کلمات فیلتر ریپلی کنید**")
            return
        
        words = m.reply_to_message.text.split('\n')
        chat_id = m.chat.id
        
        if chat_id not in filter_words:
            await m.edit_text("❌ **هیچ کلمه‌ای فیلتر نشده است**")
            return
        
        removed_count = 0
        for word in words:
            word = word.strip()
            if word and word in filter_words[chat_id]:
                filter_words[chat_id].remove(word)
                removed_count += 1
        
        await m.edit_text(f"✅ **{removed_count} کلمه از فیلتر حذف شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.sfilterlist$') & filters.group)
async def filter_list_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        
        if chat_id not in filter_words or not filter_words[chat_id]:
            await m.edit_text("❌ **هیچ کلمه‌ای فیلتر نشده است**")
            return
        
        filter_list = "🚫 **کلمات فیلتر شده:**\n\n"
        for i, word in enumerate(filter_words[chat_id], 1):
            filter_list += f"{i}. `{word}`\n"
        
        await m.edit_text(filter_list)
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.clean\s+sfilterlist$') & filters.group)
async def clean_filter_list_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        
        if chat_id in filter_words:
            count = len(filter_words[chat_id])
            filter_words[chat_id] = []
            await m.edit_text(f"✅ **{count} کلمه از لیست فیلتر پاکسازی شد**")
        else:
            await m.edit_text("❌ **لیست فیلتر خالی است**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# هندلر فیلتر کلمات
@app.on_message(filters.group & filters.text & ~filters.me, group=205)
async def filter_message_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        if chat_id in filter_words and filter_words[chat_id]:
            message_text = m.text.lower()
            for word in filter_words[chat_id]:
                if word.lower() in message_text:
                    await m.delete()
                    await app.send_message(
                        m.chat.id,
                        f"🚫 **پیام حاوی کلمه فیلتر شده حذف شد**\n\nکاربر: {m.from_user.mention}",
                        reply_to_message_id=m.id
                    )
                    break
    except Exception:
        pass

# قابلیت 14: کلمات مجاز
@app.on_message(filters.me & filters.regex(r'^\.sallow$') & filters.group)
async def set_allow_handler(app, m: Message):
    try:
        if not m.reply_to_message or not m.reply_to_message.text:
            await m.edit_text("❌ **لطفاً روی پیام حاوی کلمات مجاز ریپلی کنید**")
            return
        
        words = m.reply_to_message.text.split('\n')
        chat_id = m.chat.id
        
        if chat_id not in allow_words:
            allow_words[chat_id] = []
        
        added_count = 0
        for word in words:
            word = word.strip()
            if word and word not in allow_words[chat_id]:
                allow_words[chat_id].append(word)
                added_count += 1
        
        await m.edit_text(f"✅ **{added_count} کلمه به لیست مجاز اضافه شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.sdelallow$') & filters.group)
async def delete_allow_handler(app, m: Message):
    try:
        if not m.reply_to_message or not m.reply_to_message.text:
            await m.edit_text("❌ **لطفاً روی پیام حاوی کلمات مجاز ریپلی کنید**")
            return
        
        words = m.reply_to_message.text.split('\n')
        chat_id = m.chat.id
        
        if chat_id not in allow_words:
            await m.edit_text("❌ **هیچ کلمه‌ای در لیست مجاز نیست**")
            return
        
        removed_count = 0
        for word in words:
            word = word.strip()
            if word and word in allow_words[chat_id]:
                allow_words[chat_id].remove(word)
                removed_count += 1
        
        await m.edit_text(f"✅ **{removed_count} کلمه از لیست مجاز حذف شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.sallowlist$') & filters.group)
async def allow_list_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        
        if chat_id not in allow_words or not allow_words[chat_id]:
            await m.edit_text("❌ **هیچ کلمه‌ای در لیست مجاز نیست**")
            return
        
        allow_list = "✅ **کلمات مجاز:**\n\n"
        for i, word in enumerate(allow_words[chat_id], 1):
            allow_list += f"{i}. `{word}`\n"
        
        await m.edit_text(allow_list)
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.clean\s+sallowlist$') & filters.group)
async def clean_allow_list_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        
        if chat_id in allow_words:
            count = len(allow_words[chat_id])
            allow_words[chat_id] = []
            await m.edit_text(f"✅ **{count} کلمه از لیست مجاز پاکسازی شد**")
        else:
            await m.edit_text("❌ **لیست مجاز خالی است**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# هندلر کلمات مجاز
@app.on_message(filters.group & filters.text & ~filters.me, group=206)
async def allow_message_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        if chat_id in allow_words and allow_words[chat_id]:
            message_text = m.text.lower()
            has_allowed_word = any(word.lower() in message_text for word in allow_words[chat_id])
            if not has_allowed_word:
                await m.delete()
                await app.send_message(
                    m.chat.id,
                    f"🚫 **پیام باید حاوی کلمات مجاز باشد**\n\nکاربر: {m.from_user.mention}",
                    reply_to_message_id=m.id
                )
    except Exception:
        pass








# قابلیت 15: حالت آرام گروه
@app.on_message(filters.me & filters.regex(r'^\.setslow\s+(\d+)$') & filters.group)
async def set_slow_mode_handler(app, m: Message):
    try:
        seconds = int(m.text.split()[1])
        await app.set_slow_mode(m.chat.id, seconds)
        slow_mode_chats[m.chat.id] = seconds
        await m.edit_text(f"⏰ **حالت آرام گروه روی {seconds} ثانیه تنظیم شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.unslow$') & filters.group)
async def unset_slow_mode_handler(app, m: Message):
    try:
        await app.set_slow_mode(m.chat.id, 0)
        if m.chat.id in slow_mode_chats:
            del slow_mode_chats[m.chat.id]
        await m.edit_text("⚡ **حالت آرام گروه غیرفعال شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# قابلیت 16: اخراج کاربران
@app.on_message(filters.me & filters.regex(r'^\.kick\s+(.+)') & filters.group)
async def kick_user_handler(app, m: Message):
    try:
        targets = m.text.split()[1:]
        
        if m.reply_to_message:
            # اخراج با ریپلی
            user_id = m.reply_to_message.from_user.id
            try:
                await app.ban_chat_member(m.chat.id, user_id)
                await app.unban_chat_member(m.chat.id, user_id)
                await m.edit_text(f"👢 **کاربر {m.reply_to_message.from_user.mention} اخراج شد**")
            except Exception as e:
                await m.edit_text(f"❌ **خطا در اخراج کاربر:** `{e}`")
                
        elif targets:
            # اخراج چند کاربر
            kicked_count = 0
            for target in targets:
                try:
                    if ',' in target:
                        # اگر چند کاربر با کاما جدا شده باشند
                        sub_targets = target.split(',')
                        for sub_target in sub_targets:
                            user = await get_user_from_input(app, sub_target.strip())
                            if user:
                                await app.ban_chat_member(m.chat.id, user.id)
                                await app.unban_chat_member(m.chat.id, user.id)
                                kicked_count += 1
                                await asyncio.sleep(0.5)
                    else:
                        user = await get_user_from_input(app, target)
                        if user:
                            await app.ban_chat_member(m.chat.id, user.id)
                            await app.unban_chat_member(m.chat.id, user.id)
                            kicked_count += 1
                            await asyncio.sleep(0.5)
                except Exception:
                    continue
            
            await m.edit_text(f"✅ **{kicked_count} کاربر اخراج شدند**")
        else:
            await m.edit_text("❌ **استفاده:**\n`.kick @username` - یا ریپلی روی کاربر\n`.kick @user1,@user2,@user3` - اخراج چند کاربر")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# تابع کمکی برای دریافت کاربر از ورودی
async def get_user_from_input(app, target):
    try:
        if target.startswith('@'):
            return await app.get_users(target)
        else:
            user_id = int(target)
            return await app.get_users(user_id)
    except Exception:
        return None

@app.on_message(filters.me & filters.regex(r'^\.unban\s+(.+)') & filters.group)
async def unban_user_handler(app, m: Message):
    try:
        target = m.text.split()[1]
        
        if m.reply_to_message:
            # آنبن با ریپلی
            user_id = m.reply_to_message.from_user.id
            try:
                await app.unban_chat_member(m.chat.id, user_id)
                await m.edit_text(f"✅ **کاربر {m.reply_to_message.from_user.mention} از لیست بن خارج شد**")
            except Exception as e:
                await m.edit_text(f"❌ **خطا:** `{e}`")
                
        else:
            # آنبن با یوزرنیم/آیدی
            user = await get_user_from_input(app, target)
            if user:
                await app.unban_chat_member(m.chat.id, user.id)
                await m.edit_text(f"✅ **کاربر {user.mention} از لیست بن خارج شد**")
            else:
                await m.edit_text("❌ **کاربر یافت نشد**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")







# قابلیت 17: مدیریت سکوت کاربران
@app.on_message(filters.me & filters.regex(r'^\.silent\s+(.+)') & filters.group)
async def silent_user_handler(app, m: Message):
    try:
        target = m.text.split()[1]
        
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
            user = m.reply_to_message.from_user
        else:
            user = await get_user_from_input(app, target)
            if not user:
                await m.edit_text("❌ **کاربر یافت نشد**")
                return
            user_id = user.id
        
        chat_id = m.chat.id
        if chat_id not in silent_users:
            silent_users[chat_id] = []
        
        if user_id not in silent_users[chat_id]:
            silent_users[chat_id].append(user_id)
            await m.edit_text(f"🔇 **کاربر {user.mention} سکوت شد**")
        else:
            await m.edit_text("⚠️ **کاربر از قبل سکوت شده است**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.unsilent\s+(.+)') & filters.group)
async def unsilent_user_handler(app, m: Message):
    try:
        target = m.text.split()[1]
        
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
            user = m.reply_to_message.from_user
        else:
            user = await get_user_from_input(app, target)
            if not user:
                await m.edit_text("❌ **کاربر یافت نشد**")
                return
            user_id = user.id
        
        chat_id = m.chat.id
        if chat_id in silent_users and user_id in silent_users[chat_id]:
            silent_users[chat_id].remove(user_id)
            await m.edit_text(f"🔊 **سکوت کاربر {user.mention} لغو شد**")
        else:
            await m.edit_text("⚠️ **کاربر سکوت نشده است**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.silentlist$') & filters.group)
async def silent_list_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        
        if chat_id not in silent_users or not silent_users[chat_id]:
            await m.edit_text("❌ **هیچ کاربری سکوت نشده است**")
            return
        
        silent_list = "🔇 **کاربران سکوت شده:**\n\n"
        for i, user_id in enumerate(silent_users[chat_id], 1):
            try:
                user = await app.get_users(user_id)
                silent_list += f"{i}. {user.mention} (`{user.id}`)\n"
            except Exception:
                silent_list += f"{i}. کاربر با آیدی `{user_id}`\n"
        
        await m.edit_text(silent_list)
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.clean\s+silentlist$') & filters.group)
async def clean_silent_list_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        
        if chat_id in silent_users:
            count = len(silent_users[chat_id])
            silent_users[chat_id] = []
            await m.edit_text(f"✅ **{count} کاربر از لیست سکوت پاکسازی شد**")
        else:
            await m.edit_text("❌ **لیست سکوت خالی است**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# هندلر سکوت کاربران
@app.on_message(filters.group & ~filters.me, group=207)
async def silent_user_message_handler(app, m: Message):
    try:
        chat_id = m.chat.id
        user_id = m.from_user.id
        
        if chat_id in silent_users and user_id in silent_users[chat_id]:
            await m.delete()
    except Exception:
        pass

# قابلیت 18: پیام خوشآمدگویی
@app.on_message(filters.me & filters.regex(r'^\.welcome\s+(on|off)$') & filters.group)
async def welcome_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["welcome"] = "on"
            await m.edit_text("👋 **پیام خوشآمدگویی فعال شد**")
        else:
            json_database["welcome"] = "off"
            await m.edit_text("❌ **پیام خوشآمدگویی غیرفعال شد**")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.setwelcome$') & filters.group)
async def set_welcome_handler(app, m: Message):
    try:
        if not m.reply_to_message or not m.reply_to_message.text:
            await m.edit_text("❌ **لطفاً روی پیام خوشآمدگویی ریپلی کنید**")
            return
        
        welcome_text = m.reply_to_message.text
        json_database = json_read("data.json")
        json_database["welcome_text"] = welcome_text
        
        write("data.json", json.dumps(json_database))
        await m.edit_text("✅ **پیام خوشآمدگویی تنظیم شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# هندلر خوشآمدگویی
@app.on_message(filters.new_chat_members & filters.group, group=208)
async def welcome_message_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        if json_database.get("welcome", "off") == "on":
            welcome_text = json_database.get("welcome_text", "خوش آمدید!")
            
            for user in m.new_chat_members:
                if user.id != app.me.id:
                    personalized_text = welcome_text.replace("{user}", user.mention)
                    personalized_text = personalized_text.replace("{group}", m.chat.title)
                    
                    await app.send_message(
                        m.chat.id,
                        personalized_text,
                        reply_to_message_id=m.id
                    )
    except Exception:
        pass

# قابلیت 19: مسدودسازی از تمام گروه‌ها
@app.on_message(filters.me & filters.regex(r'^\.banall\s+(.+)'))
async def ban_all_handler(app, m: Message):
    try:
        target = m.text.split()[1]
        
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
            user = m.reply_to_message.from_user
        else:
            user = await get_user_from_input(app, target)
            if not user:
                await m.edit_text("❌ **کاربر یافت نشد**")
                return
            user_id = user.id
        
        if user_id not in ban_all_users:
            ban_all_users.append(user_id)
            await m.edit_text(f"🔨 **کاربر {user.mention} به لیست مسدودسازی جهانی اضافه شد**")
        else:
            await m.edit_text("⚠️ **کاربر از قبل در لیست مسدودسازی جهانی است**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.unbanall\s+(.+)'))
async def unban_all_handler(app, m: Message):
    try:
        target = m.text.split()[1]
        
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
            user = m.reply_to_message.from_user
        else:
            user = await get_user_from_input(app, target)
            if not user:
                await m.edit_text("❌ **کاربر یافت نشد**")
                return
            user_id = user.id
        
        if user_id in ban_all_users:
            ban_all_users.remove(user_id)
            await m.edit_text(f"✅ **کاربر {user.mention} از لیست مسدودسازی جهانی حذف شد**")
        else:
            await m.edit_text("⚠️ **کاربر در لیست مسدودسازی جهانی نیست**")
            
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.banalllist$'))
async def ban_all_list_handler(app, m: Message):
    try:
        if not ban_all_users:
            await m.edit_text("❌ **لیست مسدودسازی جهانی خالی است**")
            return
        
        ban_list = "🔨 **کاربران مسدود شده از تمام گروه‌ها:**\n\n"
        for i, user_id in enumerate(ban_all_users, 1):
            try:
                user = await app.get_users(user_id)
                ban_list += f"{i}. {user.mention} (`{user.id}`)\n"
            except Exception:
                ban_list += f"{i}. کاربر با آیدی `{user_id}`\n"
        
        await m.edit_text(ban_list)
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.clean\s+banalllist$'))
async def clean_ban_all_list_handler(app, m: Message):
    try:
        count = len(ban_all_users)
        ban_all_users.clear()
        await m.edit_text(f"✅ **{count} کاربر از لیست مسدودسازی جهانی پاکسازی شد**")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# هندلر مسدودسازی جهانی
@app.on_message(filters.group & ~filters.me, group=209)
async def ban_all_message_handler(app, m: Message):
    try:
        user_id = m.from_user.id
        if user_id in ban_all_users:
            # سعی در مسدود کردن کاربر
            try:
                await app.ban_chat_member(m.chat.id, user_id)
            except Exception:
                # اگر نمی‌توان مسدود کرد، پیام را حذف کن
                await m.delete()
    except Exception:
        pass

# قابلیت 20: دعوت به ویس چت
@app.on_message(filters.me & filters.regex(r'^\.invvc\s+(.+)') & filters.group)
async def invite_to_voice_chat_handler(app, m: Message):
    try:
        targets = m.text.split()[1:]
        usernames = []
        
        for target in targets:
            if ',' in target:
                usernames.extend([u.strip() for u in target.split(',')])
            else:
                usernames.append(target.strip())
        
        invited_count = 0
        for username in usernames:
            if username.startswith('@'):
                try:
                    user = await app.get_users(username)
                    # این قسمت نیاز به API مخصوص دارد
                    # در نسخه فعلی پی‌رگرام این قابلیت مستقیم موجود نیست
                    invited_count += 1
                    await asyncio.sleep(0.5)
                except Exception:
                    continue
        
        await m.edit_text(f"📞 **درخواست دعوت {invited_count} کاربر به ویس چت ارسال شد**\n\n⚠️ **توجه:** این قابلیت نیاز به تنظیمات اضافی دارد")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.invvcall$') & filters.group)
async def invite_all_to_voice_chat_handler(app, m: Message):
    try:
        await m.edit_text("📞 **در حال دعوت کاربران به ویس چت...**")
        
        invited_count = 0
        async for member in app.get_chat_members(m.chat.id, limit=200):
            if not member.user.is_bot and member.user.id != app.me.id:
                try:
                    # این قسمت نیاز به API مخصوص دارد
                    invited_count += 1
                    await asyncio.sleep(0.2)
                except Exception:
                    continue
        
        await m.edit_text(f"✅ **درخواست دعوت {invited_count} کاربر به ویس چت ارسال شد**\n\n⚠️ **توجه:** این قابلیت نیاز به تنظیمات اضافی دارد")
        
    except Exception as e:
        await m.edit_text(f"❌ **خطا:** `{e}`")

# |====================================| #
# قابلیت همیشه آنلاین (Keep Online)
# |====================================| #

@app.on_message(filters.me & filters.regex(r'^\.keeponline\s+(on|off)$'), group=160)
async def keep_online_handler(app, m: Message):
    """فعال/غیرفعال کردن حالت همیشه آنلاین"""
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["keep_online"] = "on"
            write("data.json", json.dumps(json_database))
            
            # تنظیم وضعیت آنلاین
            await app.invoke(functions.account.UpdateStatus(offline=False))
            
            await m.edit_text("✅ **حالت همیشه آنلاین فعال شد**\n\n• اکنون شما همیشه آنلاین نمایش داده می‌شوید\n• حتی وقتی برنامه بسته است")
            
        else:
            json_database["keep_online"] = "off"
            write("data.json", json.dumps(json_database))
            
            # بازگشت به وضعیت عادی
            await app.invoke(functions.account.UpdateStatus(offline=True))
            
            await m.edit_text("❌ **حالت همیشه آنلاین غیرفعال شد**")
            
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.onlinestatus$'), group=161)
async def online_status_handler(app, m: Message):
    """نمایش وضعیت آنلاین"""
    try:
        json_database = json_read("data.json")
        
        status = "✅ فعال" if json_database.get("keep_online", "off") == "on" else "❌ غیرفعال"
        
        # دریافت وضعیت فعلی
        try:
            user_full = await app.invoke(functions.users.GetFullUser(id=await app.resolve_peer(app.me.id)))
            current_status = user_full.full_user.status
            status_text = ""
            
            if isinstance(current_status, types.UserStatusOnline):
                status_text = "🟢 آنلاین"
            elif isinstance(current_status, types.UserStatusOffline):
                status_text = "🔴 آفلاین"
            elif isinstance(current_status, types.UserStatusRecently):
                status_text = "🟡 اخیراً آنلاین"
            elif isinstance(current_status, types.UserStatusLastWeek):
                status_text = "⚫ هفته گذشته"
            elif isinstance(current_status, types.UserStatusLastMonth):
                status_text = "⚫ ماه گذشته"
            else:
                status_text = "🔵 مخفی"
                
        except:
            status_text = "نامشخص"
        
        message_text = (
            f"🌐 **وضعیت آنلاین:**\n\n"
            f"🔹 **حالت همیشه آنلاین:** {status}\n"
            f"🔹 **وضعیت فعلی:** {status_text}\n"
            f"🔹 **کاربر:** {app.me.first_name}\n\n"
            f"برای تغییر: `.keeponline on/off`"
        )
        
        await m.edit_text(message_text)
        
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

@app.on_message(filters.me & filters.regex(r'^\.whitep$') & filters.reply)
async def white_filter_handler(app, m: Message):
    """تبدیل عکس به سیاه و سفید"""
    try:
        if not m.reply_to_message or not m.reply_to_message.photo:
            await m.edit_text("**❖ لطفاً روی یک عکس ریپلای کنید**")
            return

        await m.edit_text("**📷 در حال پردازش عکس...**")
        
        # دانلود عکس
        file_path = await app.download_media(m.reply_to_message.photo.file_id)
        
        # پردازش عکس
        processed_path = await apply_white_filter(file_path)
        
        # ارسال عکس پردازش شده
        await app.send_photo(
            m.chat.id,
            processed_path,
            caption="**🖼 عکس سیاه و سفید شده**",
            reply_to_message_id=m.reply_to_message.id
        )
        
        # حذف فایل‌های موقت
        os.remove(file_path)
        os.remove(processed_path)
        await m.delete()
        
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.rgb$') & filters.reply)
async def rgb_filter_handler(app, m: Message):
    """اعمال فیلتر RGB روی عکس"""
    try:
        if not m.reply_to_message or not m.reply_to_message.photo:
            await m.edit_text("**❖ لطفاً روی یک عکس ریپلای کنید**")
            return

        await m.edit_text("**🎨 در حال اعمال فیلتر RGB...**")
        
        file_path = await app.download_media(m.reply_to_message.photo.file_id)
        processed_path = await apply_rgb_filter(file_path)
        
        await app.send_photo(
            m.chat.id,
            processed_path,
            caption="**🌈 عکس با فیلتر RGB**",
            reply_to_message_id=m.reply_to_message.id
        )
        
        os.remove(file_path)
        os.remove(processed_path)
        await m.delete()
        
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.greenp$') & filters.reply)
async def green_filter_handler(app, m: Message):
    """اعمال فیلتر سبز روی عکس"""
    try:
        if not m.reply_to_message or not m.reply_to_message.photo:
            await m.edit_text("**❖ لطفاً روی یک عکس ریپلای کنید**")
            return

        await m.edit_text("**💚 در حال اعمال فیلتر سبز...**")
        
        file_path = await app.download_media(m.reply_to_message.photo.file_id)
        processed_path = await apply_green_filter(file_path)
        
        await app.send_photo(
            m.chat.id,
            processed_path,
            caption="**💚 عکس با فیلتر سبز**",
            reply_to_message_id=m.reply_to_message.id
        )
        
        os.remove(file_path)
        os.remove(processed_path)
        await m.delete()
        
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.bluep$') & filters.reply)
async def blue_filter_handler(app, m: Message):
    """اعمال فیلتر آبی روی عکس"""
    try:
        if not m.reply_to_message or not m.reply_to_message.photo:
            await m.edit_text("**❖ لطفاً روی یک عکس ریپلای کنید**")
            return

        await m.edit_text("**💙 در حال اعمال فیلتر آبی...**")
        
        file_path = await app.download_media(m.reply_to_message.photo.file_id)
        processed_path = await apply_blue_filter(file_path)
        
        await app.send_photo(
            m.chat.id,
            processed_path,
            caption="**💙 عکس با فیلتر آبی**",
            reply_to_message_id=m.reply_to_message.id
        )
        
        os.remove(file_path)
        os.remove(processed_path)
        await m.delete()
        
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.redp$') & filters.reply)
async def red_filter_handler(app, m: Message):
    """اعمال فیلتر قرمز روی عکس"""
    try:
        if not m.reply_to_message or not m.reply_to_message.photo:
            await m.edit_text("**❖ لطفاً روی یک عکس ریپلای کنید**")
            return

        await m.edit_text("**❤️ در حال اعمال فیلتر قرمز...**")
        
        file_path = await app.download_media(m.reply_to_message.photo.file_id)
        processed_path = await apply_red_filter(file_path)
        
        await app.send_photo(
            m.chat.id,
            processed_path,
            caption="**❤️ عکس با فیلتر قرمز**",
            reply_to_message_id=m.reply_to_message.id
        )
        
        os.remove(file_path)
        os.remove(processed_path)
        await m.delete()
        
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.blurp$') & filters.reply)
async def blur_filter_handler(app, m: Message):
    """اعمال فیلتر بلور (تار) روی عکس"""
    try:
        if not m.reply_to_message or not m.reply_to_message.photo:
            await m.edit_text("**❖ لطفاً روی یک عکس ریپلای کنید**")
            return

        await m.edit_text("**🌀 در حال اعمال فیلتر بلور...**")
        
        file_path = await app.download_media(m.reply_to_message.photo.file_id)
        processed_path = await apply_blur_filter(file_path)
        
        await app.send_photo(
            m.chat.id,
            processed_path,
            caption="**🌀 عکس با فیلتر بلور**",
            reply_to_message_id=m.reply_to_message.id
        )
        
        os.remove(file_path)
        os.remove(processed_path)
        await m.delete()
        
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")

# توابع پردازش عکس
async def apply_white_filter(image_path):
    """تبدیل عکس به سیاه و سفید"""
    image = Image.open(image_path)
    # تبدیل به سیاه و سفید
    bw_image = image.convert('L')
    # تبدیل مجدد به RGB برای سازگاری
    bw_image = bw_image.convert('RGB')
    
    output_path = "filtered_white.jpg"
    bw_image.save(output_path, "JPEG", quality=95)
    return output_path

async def apply_rgb_filter(image_path):
    """اعمال فیلتر RGB با افزایش اشباع رنگ"""
    image = Image.open(image_path)
    # افزایش اشباع رنگ
    enhancer = ImageEnhance.Color(image)
    saturated_image = enhancer.enhance(1.5)
    
    # افزایش کنتراست
    contrast_enhancer = ImageEnhance.Contrast(saturated_image)
    final_image = contrast_enhancer.enhance(1.2)
    
    output_path = "filtered_rgb.jpg"
    final_image.save(output_path, "JPEG", quality=95)
    return output_path

async def apply_green_filter(image_path):
    """اعمال فیلتر سبز"""
    image = Image.open(image_path).convert('RGB')
    pixels = image.load()
    
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # افزایش رنگ سبز
            pixels[x, y] = (r, min(g + 50, 255), b)
    
    output_path = "filtered_green.jpg"
    image.save(output_path, "JPEG", quality=95)
    return output_path

async def apply_blue_filter(image_path):
    """اعمال فیلتر آبی"""
    image = Image.open(image_path).convert('RGB')
    pixels = image.load()
    
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # افزایش رنگ آبی
            pixels[x, y] = (r, g, min(b + 50, 255))
    
    output_path = "filtered_blue.jpg"
    image.save(output_path, "JPEG", quality=95)
    return output_path

async def apply_red_filter(image_path):
    """اعمال فیلتر قرمز"""
    image = Image.open(image_path).convert('RGB')
    pixels = image.load()
    
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # افزایش رنگ قرمز
            pixels[x, y] = (min(r + 50, 255), g, b)
    
    output_path = "filtered_red.jpg"
    image.save(output_path, "JPEG", quality=95)
    return output_path

async def apply_blur_filter(image_path):
    """اعمال فیلتر بلور"""
    image = Image.open(image_path)
    # اعمال فیلتر بلور
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=3))
    
    output_path = "filtered_blur.jpg"
    blurred_image.save(output_path, "JPEG", quality=95)
    return output_path

@app.on_message(filters.me & filters.regex(r'^\.markall\s+(on|off)$'), group=338)
async def markall_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["markall"] = "on"
            await m.edit_text("✅ **علامت‌گذاری خودکار فعال شد**\n\n• پیام‌های دریافتی در پیوی\n• ریپلای‌ها روی پیام‌های شما در گروه‌ها\n\nهمگی به صورت خودکار خوانده می‌شوند")
        else:
            json_database["markall"] = "off"
            await m.edit_text("❌ **علامت‌گذاری خودکار غیرفعال شد**")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

@app.on_message(filters.private & filters.incoming & ~filters.me & ~filters.bot, group=340)
async def auto_mark_read_pv_handler(app, message: Message):
    try:
        json_database = json_read("data.json")
        
        if json_database.get("markall", "off") == "on":
            # علامت‌گذاری پیام به عنوان خوانده شده در پیوی
            await app.read_chat_history(message.chat.id)
            
    except Exception:
		    pass

@app.on_message(filters.me & filters.regex(r'^\.insta') & filters.private)
async def download_instagram(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**❖ Usage:** `.insta [instagram_url]`")
            return
        
        url = m.text.split()[1]
        
        # بررسی اینکه لینک اینستاگرام است
        if 'instagram.com' not in url:
            await m.edit_text("**❖ لینک اینستاگرام معتبر نیست**")
            return
        
        await m.edit_text("**🔍 در حال دریافت اطلاعات از اینستاگرام...**")
        
        # استفاده از API شما
        api_url = f"https://api.fast-creat.ir/instagram?apikey=7472446130:4MK0xnarPe9zoEO@Api_ManagerRoBot&type=post2&url={url}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                if response.status != 200:
                    await m.edit_text("**❌ خطا در ارتباط با API**")
                    return
                
                data = await response.json()
        
        # بررسی موفقیت آمیز بودن پاسخ
        if not data.get('ok'):
            await m.edit_text(f"**❌ خطا از سمت API:** {data.get('msg', 'خطای ناشناخته')}")
            return
        
        result_data = data.get('result', {})
        
        if result_data.get('status') != 'success':
            await m.edit_text("**❌ پست یافت نشد یا خطا در پردازش**")
            return
        
        posts = result_data.get('result', [])
        
        if not posts:
            await m.edit_text("**❌ محتوایی برای دانلود یافت نشد**")
            return
        
        await m.edit_text("**📥 در حال دانلود و ارسال محتوا...**")
        
        # پردازش و ارسال تمام پست‌های برگشتی
        for post in posts:
            await send_instagram_post(app, m, post)
        
        await m.delete()
            
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")

async def send_instagram_post(app, m, post):
    """ارسال یک پست اینستاگرام"""
    try:
        if post.get('is_video'):
            # پست ویدیویی
            await send_video_post(app, m, post)
        else:
            # پست عکس
            await send_photo_post(app, m, post)
            
    except Exception as e:
        await m.edit_text(f"**❌ خطا در ارسال پست:**\n`{str(e)}`")

async def send_photo_post(app, m, post):
    """ارسال پست عکس با کپشن"""
    try:
        media_url = post.get('video_img') or post.get('video_url')
        caption = await generate_caption(post)
        if media_url:
            await app.send_photo(m.chat.id, media_url, caption=caption)
        else:
            await m.edit_text("**❌ لینک مدیا یافت نشد**")
            
    except Exception as e:
        try:
            media_url = post.get('video_img') or post.get('video_url')
            caption = await generate_caption(post)
            if media_url:
                await app.send_document(m.chat.id, media_url, caption=caption)
        except:
            await m.edit_text(f"**❌ خطا در ارسال عکس:**\n`{str(e)}`")

async def send_video_post(app, m, post):
    """ارسال پست ویدیویی با کپشن"""
    try:
        video_url = post.get('video_url')
        thumbnail = post.get('video_img')
        caption = await generate_caption(post)
        
        if video_url:
            await app.send_video(
                m.chat.id, 
                video_url, 
                caption=caption,
                thumb=thumbnail if thumbnail else None
            )
        else:
            await m.edit_text("**❌ لینک ویدیو یافت نشد**")
            
    except Exception as e:
        try:
            video_url = post.get('video_url')
            caption = await generate_caption(post)
            if video_url:
                await app.send_document(m.chat.id, video_url, caption=caption)
        except:
            await m.edit_text(f"**❌ خطا در ارسال ویدیو:**\n`{str(e)}`")

async def generate_caption(post):
    """تولید کپشن برای پست"""
    try:
        info_text = "**• ( Instagram Downloader ) •**\n\n"
        
        # اطلاعات اصلی
        if post.get('username'):
            info_text += f"**• Page : [ @{post['username']} ]**\n"
        
        # آیدی پست
        if post.get('id'):
            info_text += f"**• Post id : [ `{post['id']}` ]**\n"
        
        # نوع محتوا
        if post.get('is_video'):
            info_text += "**• Type : [ Video ]**\n"
        elif post.get('is_album'):
            info_text += "**• Type : [ Album ]**\n"
        else:
            info_text += "**• Type : [ Photo ]**\n"
        
        # کپشن اصلی (اگر کوتاه باشد نمایش داده می‌شود)
        if post.get('caption'):
            caption_text = post['caption']
            if len(caption_text) <= 200:  # فقط اگر کپشن کوتاه باشد
                info_text += f"**• Caption : [ {caption_text} ]**\n"
            else:
                # اگر کپشن طولانی است، فقط بخشی از آن نمایش داده می‌شود
                short_caption = caption_text[:197] + "..."
                info_text += f"**• Caption : [ {short_caption} ]**\n"
        
        info_text += "\n**• Dowmload Completed •**"
        
        return info_text
        
    except Exception as e:
        return "**• Dowanlod Completed •**"

@app.on_message(filters.me & filters.regex(r'^\.instainfo') & filters.private)
async def instagram_info(app, m: Message):
    """نمایش اطلاعات پست اینستاگرام بدون دانلود"""
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**❖ Usage:** `.instainfo [instagram_url]`")
            return
        
        url = m.text.split()[1]
        
        if 'instagram.com' not in url:
            await m.edit_text("**❖ لینک اینستاگرام معتبر نیست**")
            return
        
        await m.edit_text("**🔍 در حال دریافت اطلاعات...**")
        
        api_url = f"https://api.fast-creat.ir/instagram?apikey=7472446130:4MK0xnarPe9zoEO@Api_ManagerRoBot&type=post2&url={url}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                if response.status != 200:
                    await m.edit_text("**❌ خطا در ارتباط با API**")
                    return
                
                data = await response.json()
        
        if not data.get('ok'):
            await m.edit_text(f"**❌ خطا:** {data.get('msg', 'خطای ناشناخته')}")
            return
        
        result_data = data.get('result', {})
        
        if result_data.get('status') != 'success':
            await m.edit_text("**❌ پست یافت نشد**")
            return
        
        posts = result_data.get('result', [])
        
        if not posts:
            await m.edit_text("**❌ محتوایی یافت نشد**")
            return
        
        # ساخت پیام اطلاعات
        info_text = "**📊 اطلاعات پست اینستاگرام**\n\n"
        
        for i, post in enumerate(posts, 1):
            info_text += f"**📦 پست {i}:**\n"
            info_text += f"• **👤 کاربر:** @{post.get('username', '--')}\n"
            info_text += f"• **🆔 آیدی:** `{post.get('id', '--')}`\n"
            
            if post.get('is_video'):
                info_text += "• **📋 نوع:** 🎥 ویدیو\n"
            elif post.get('is_album'):
                info_text += "• **📋 نوع:** 📸 آلبوم\n"
            else:
                info_text += "• **📋 نوع:** 📷 عکس\n"
            
            info_text += "\n"
        
        info_text += f"**برای دانلود از دستور زیر استفاده کنید:**\n`.insta {url}`"
        
        await m.edit_text(info_text)
        
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")

# |====================================| #
# دستور .poker on/off - فقط پیوی
@app.on_message(filters.me & filters.regex(r'^\.poker\s+(on|off)$'), group=150)
async def poker_pv_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["poker_pv"] = "on"
            await m.edit_text("**پوکر در پیوی روشن شد** 😐")
        else:
            json_database["poker_pv"] = "off"
            await m.edit_text("**پوکر در پیوی خاموش شد** 😐")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

# |====================================| #
# دستور .allpoker on/off - پیوی + گروه
@app.on_message(filters.me & filters.regex(r'^\.allpoker\s+(on|off)$'), group=151)
async def poker_all_handler(app, m: Message):
    try:
        status = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if status == "on":
            json_database["poker_pv"] = "on"
            json_database["poker_all"] = "on"
            await m.edit_text("**پوکر در پیوی و گروه روشن شد** 😐")
        else:
            json_database["poker_pv"] = "off"
            json_database["poker_all"] = "off"
            await m.edit_text("**پوکر در همه جا خاموش شد** 😐")
            
        write("data.json", json.dumps(json_database))
    except Exception as e:
        await m.edit_text(f"**خطا:** `{e}`")

# |====================================| #
# هندلر پوکر - فقط ایموجی 😐
@app.on_message(filters.private & ~filters.me & filters.text & filters.regex(r'^😐$'), group=152)
async def poker_pv_response(app, m: Message):
    json_database = json_read("data.json")
    if json_database.get("poker_pv", "off") == "on":
        try:
            await app.send_message(m.chat.id, "😐", reply_to_message_id=m.id)
        except:
            pass

@app.on_message(filters.group & filters.text & filters.regex(r'^😐$'), group=153)
async def poker_group_response(app, m: Message):
    json_database = json_read("data.json")
    if json_database.get("poker_pv", "off") == "on" and json_database.get("poker_all", "off") == "on":
        try:
            await app.send_message(m.chat.id, "😐", reply_to_message_id=m.id)
        except:
            pass

@app.on_message(filters.me & filters.channel & filters.regex(r'^\.saveschat$'), group=119)
async def save_channel_handler(app, m: Message):
    try:
        channel_id = m.chat.id

        # ذخیره در data.json
        json_database = json_read("data.json")
        json_database["save_channel_id"] = channel_id
        write("data.json", json.dumps(json_database))

        await m.edit_text(
            f"**کانال پشتیبان ثبت شد!**\n\n"
            f"**نام:** `{m.chat.title}`\n"
            f"**آیدی:** `{channel_id}`\n\n"
            f"حالا می‌توانید با `.savemade [نام]` محتوا ذخیره کنید."
        )

    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.savemade\s+'), group=120)
async def save_made_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**استفاده:** `.savemade [نام]` (ریپلای روی محتوا)")
            return
        
        if not m.reply_to_message:
            await m.edit_text("**لطفاً روی یک محتوا ریپلای کنید!**")
            return

        name = " ".join(m.text.split()[1:]).strip()
        reply_msg = m.reply_to_message

        # چک کردن کانال پشتیبان
        json_database = json_read("data.json")
        channel_id = json_database.get("save_channel_id")
        if not channel_id:
            await m.edit_text("**کانال پشتیبان ثبت نشده!**\nابتدا در کانال `.saveschat` بزنید.")
            return

        # ارسال محتوا به کانال و ذخیره message_id
        sent_msg = await reply_msg.copy(channel_id)
        
        # ذخیره اطلاعات پیام
        message_data = {
            "message_id": sent_msg.id,
            "chat_id": channel_id
        }

        json_database["saved_mades"][name] = message_data
        write("data.json", json.dumps(json_database))

        await m.edit_text(
            f"**محتوا ذخیره شد!**\n\n"
            f"**نام:** `{name}`\n"
            f"**نوع:** `{reply_msg.media.value if reply_msg.media else 'متن'}`\n"
            f"در کانال پشتیبان ذخیره شد."
        )

    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.claimsave\s+'), group=121)
async def claim_save_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**استفاده:** `.claimsave [نام]`")
            return
        
        name = " ".join(m.text.split()[1:]).strip()
        json_database = json_read("data.json")
        saved_mades = json_database.get("saved_mades", {})

        if name not in saved_mades:
            await m.edit_text(f"**نام یافت نشد:** `{name}`\nاز `.madelist` استفاده کنید.")
            return

        msg_data = saved_mades[name]

        try:
            # دریافت پیام اصلی از کانال
            original_msg = await app.get_messages(msg_data["chat_id"], msg_data["message_id"])
            # کپی محتوا به پیام فعلی
            await original_msg.copy(m.chat.id, reply_to_message_id=m.reply_to_message_id or None)
            await m.delete()  # حذف دستور
        except Exception as e:
            await m.edit_text(f"**خطا در بازیابی محتوا:**\n`{str(e)}`")

    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.delmade\s+'), group=122)
async def delete_made_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**استفاده:** `.delmade [نام]`")
            return
        
        name = " ".join(m.text.split()[1:]).strip()
        json_database = json_read("data.json")
        saved_mades = json_database.get("saved_mades", {})

        if name not in saved_mades:
            await m.edit_text(f"**نام یافت نشد:** `{name}`")
            return

        # حذف از data.json
        del saved_mades[name]
        json_database["saved_mades"] = saved_mades
        write("data.json", json.dumps(json_database))

        await m.edit_text(f"**محتوا حذف شد:** `{name}`")

    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.madelist$'), group=123)
async def list_mades_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        saved_mades = json_database.get("saved_mades", {})

        if not saved_mades:
            await m.edit_text("**هیچ محتوایی ذخیره نشده!**\n\nبرای ذخیره: `.savemade [نام]` (ریپلای روی محتوا)")
            return

        list_text = "**لیست محتواهای ذخیره‌شده:**\n\n"
        count = 1
        for name, data in saved_mades.items():
            try:
                msg = await app.get_messages(data["chat_id"], data["message_id"])
                media_type = msg.media.value if msg.media else "متن"
            except:
                media_type = "نامشخص"
            list_text += f"`{count}` - **نام:** `{name}` | **نوع:** `{media_type}`\n"
            count += 1

        list_text += f"\n**کل:** `{len(saved_mades)}` مورد\n\nبرای حذف: `.delmade [نام]`"
        await m.edit_text(list_text)

    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.saveclear$'), group=124)
async def clear_saves_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        json_database["saved_mades"] = {}
        write("data.json", json.dumps(json_database))

        await m.edit_text("**تمام محتواهای ذخیره‌شده پاک شدند!**")

    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.addanswer)'), group=112)
async def add_answer_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**استفاده:** `.addanswer [پاسخ]` (ریپلای روی جواب)")
            return
        
        if not m.reply_to_message or not m.reply_to_message.text:
            await m.edit_text("**لطفاً روی یک پیام متنی ریپلای کنید (به عنوان جواب)**")
            return
        
        trigger = " ".join(m.text.split()[1:])  # پاسخ
        response = m.reply_to_message.text       # جواب
        
        json_database = json_read("data.json")
        json_database["auto_answers"][trigger] = response
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(f"**پاسخ خودکار اضافه شد**\n\n**وقتی بگویند:** `{trigger}`\n**جواب می‌دهم:** `{response}`")
        
    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.delanswer)'), group=113)
async def del_answer_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**استفاده:** `.delanswer [پاسخ]`")
            return
        
        trigger = " ".join(m.text.split()[1:])
        
        json_database = json_read("data.json")
        if trigger in json_database.get("auto_answers", {}):
            del json_database["auto_answers"][trigger]
            write("data.json", json.dumps(json_database))
            await m.edit_text(f"**پاسخ حذف شد:** `{trigger}`")
        else:
            await m.edit_text(f"**پاسخ یافت نشد:** `{trigger}`")
        
    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.answerlist)$'), group=114)
async def answer_list_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        answers = json_database.get("auto_answers", {})
        
        if not answers:
            await m.edit_text("**هیچ پاسخ خودکاری ثبت نشده!**\n\n`.addanswer [متن] (ریپلای روی جواب)`")
            return
        
        list_text = "**لیست پاسخ‌های خودکار**\n\n"
        for i, (trigger, response) in enumerate(answers.items(), 1):
            short_resp = (response[:40] + "...") if len(response) > 40 else response
            list_text += f"`{i}` **وقتی:** `{trigger}`\n    **جواب:** `{short_resp}`\n\n"
        
        await m.edit_text(list_text)
        
    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.private & ~filters.me & filters.text, group=115)
async def auto_answer_pv_handler(app, m: Message):
    try:
        text = m.text.strip()
        json_database = json_read("data.json")
        answers = json_database.get("auto_answers", {})
        
        if text in answers:
            await app.send_message(m.chat.id, answers[text], reply_to_message_id=m.id)
            
    except Exception as e:
        print(f"Auto-answer error: {e}")

@app.on_message(filters.me & filters.regex(f'^(.addfild)'), group=109)
async def add_field_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("❖ **Usage:** `.addfild [key]` (reply to the value message)")
            return
        
        if not m.reply_to_message or not m.reply_to_message.text:
            await m.edit_text("❖ **Please reply to a text message as value**")
            return
        
        key = " ".join(m.text.split()[1:])
        value = m.reply_to_message.text
        
        json_database = json_read("data.json")
        json_database["fields"][key] = value
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(f"✅ **Field added**\n\n**Key:** `{key}`\n**Value:** `{value}`")
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.delfild)'), group=110)
async def delete_field_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("❖ **Usage:** `.delfild [key]`")
            return
        
        key = " ".join(m.text.split()[1:])
        
        json_database = json_read("data.json")
        if key in json_database.get("fields", {}):
            del json_database["fields"][key]
            write("data.json", json.dumps(json_database))
            await m.edit_text(f"✅ **Field deleted**\n\n**Key:** `{key}`")
        else:
            await m.edit_text(f"❖ **Key not found:** `{key}`")
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

@app.on_message(filters.me & filters.text, group=108)
async def auto_edit_field_handler(app, m: Message):
    try:
        text = m.text.strip()
        json_database = json_read("data.json")
        fields = json_database.get("fields", {})
        
        if text in fields:
            value = fields[text]
            await m.edit_text(value)
        
    except Exception as e:
        print(f"Error in auto-edit: {e}")  # لاگ خطا بدون نمایش به کاربر

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.listfild)$'), group=111)
async def list_fields_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        fields = json_database.get("fields", {})
        
        if not fields:
            await m.edit_text("**هیچ فیلدی ثبت نشده است!**\n\nبرای اضافه کردن:\n`.addfild [کلید]` (ریپلای روی متن)")
            return
        
        # ساخت لیست مرتب
        field_list = ""
        count = 1
        for key, value in fields.items():
            # کوتاه کردن مقدار اگر خیلی طولانی بود
            short_value = (value[:50] + "...") if len(value) > 50 else value
            field_list += f"`{count}` - **کلید:** `{key}`\n    **مقدار:** `{short_value}`\n\n"
            count += 1
        
        total = len(fields)
        status_text = (
            f"**لیست فیلدها ({total})**\n\n"
            f"{field_list}"
            f"برای حذف: `.delfild [کلید]`"
        )
        
        await m.edit_text(status_text)
        
    except Exception as e:
        await m.edit_text(f"**خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.setaction)'), group=103)
async def set_auto_reaction_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("❖ **Usage:** `.setaction [emoji]`")
            return
        
        emoji = m.text.split()[1]
        
        json_database = json_read("data.json")
        json_database.update({
            "auto_reaction": "on",
            "reaction_emoji": emoji
        })
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(f"✅ **ری‌اکشن خودکار فعال شد**\n\n**ایموجی:** {emoji}")
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا:**\n`{str(e)}`")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.delaction)$'), group=104)
async def delete_auto_reaction_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        json_database.update({
            "auto_reaction": "off",
            "reaction_emoji": ""
        })
        write("data.json", json.dumps(json_database))
        
        await m.edit_text("❌ **ری‌اکشن خودکار غیرفعال شد**")
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا:**\n`{str(e)}`")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.actionstatus)$'), group=105)
async def reaction_status_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        status = "✅ فعال" if json_database.get("auto_reaction", "off") == "on" else "❌ غیرفعال"
        reaction_emoji = json_database.get("reaction_emoji", "🔥")
        
        status_text = (
            f"🎭 **وضعیت ری‌اکشن خودکار:**\n\n"
            f"🔹 **حالت:** {status}\n"
            f"🔹 **ایموجی:** {reaction_emoji if reaction_emoji else '--'}"
        )
        
        await m.edit_text(status_text)
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا:**\n`{str(e)}`")

# |====================================| #

@app.on_message(filters.group | filters.channel, group=106)
async def auto_reaction_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        if json_database.get("auto_reaction", "off") != "on":
            return
        
        if m.from_user and m.from_user.id == app.me.id:
            return
        
        reaction_emoji = json_database.get("reaction_emoji", "🔥")
        if not reaction_emoji:
            return
        
        try:
            await app.send_reaction(
                chat_id=m.chat.id,
                message_id=m.id,
                emoji=reaction_emoji
            )
        except errors.exceptions.bad_request_400.MessageIdInvalid:
            pass
        except errors.exceptions.bad_request_400.ReactionInvalid:
            print(f"ایموجی نامعتبر: {reaction_emoji}")
        except Exception as e:
            print(f"خطا در ارسال ری‌اکشن: {e}")
            
    except Exception as e:
        pass

# |====================================| #


@app.on_message(filters.me & filters.regex(f'^(.setsign)'), group=100)
async def set_signature_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("❖ **Usage:** `.setsign [متن امضا]`")
            return
        
        signature_text = " ".join(m.text.split()[1:])
        json_database = json_read("data.json")
        
        json_database.update({
            "signature": "on",
            "signature_text": signature_text
        })
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(f"✅ **امضا تنظیم شد**\n\n**متن:** `{signature_text}`")
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا:**\n`{str(e)}`")

@app.on_message(filters.private & filters.incoming & ~filters.me & ~filters.bot, group=107)
async def pv_locks_handler(app, message: Message):
    json_database = json_read("data.json")
    
    # حالت سکوت پیوی: حذف هر پیام
    if json_database.get("pv_silent", "off") == "on":
        await message.delete()
        return
    
    # قفل فوروارد
    if json_database.get("lock_forward", "off") == "on" and message.forward_date:
        await message.delete()
        return
    
    # قفل لوکیشن
    if json_database.get("lock_location", "off") == "on" and (message.location or message.venue):
        await message.delete()
        return
    
    # قفل عکس
    if json_database.get("lock_photo", "off") == "on" and message.photo:
        await message.delete()
        return
    
    # قفل گیف
    if json_database.get("lock_gif", "off") == "on" and message.animation:
        await message.delete()
        return
    
    # قفل استیکر
    if json_database.get("lock_sticker", "off") == "on" and message.sticker:
        await message.delete()
        return
    
    # قفل ویدیو سلفی
    if json_database.get("lock_video_note", "off") == "on" and message.video_note:
        await message.delete()
        return
    
    # قفل ویدیو
    if json_database.get("lock_video", "off") == "on" and message.video:
        await message.delete()
        return
    
    # قفل ویس
    if json_database.get("lock_voice", "off") == "on" and message.voice:
        await message.delete()
        return
    
    # قفل آهنگ
    if json_database.get("lock_audio", "off") == "on" and message.audio:
        await message.delete()
        return
    
    # قفل مخاطب
    if json_database.get("lock_contact", "off") == "on" and message.contact:
        await message.delete()
        return
    
    # قفل نظرسنجی / دکمه شیشه‌ای / بازی
    if json_database.get("lock_poll", "off") == "on" and (message.poll or message.game or 
        (message.reply_markup and isinstance(message.reply_markup, InlineKeyboardMarkup))):
        await message.delete()
        return
    
    # قفل متن
    if json_database.get("lock_text", "off") == "on" and message.text:
        await message.delete()
        return
    
    if message.text:
        # قفل انگلیسی
        if json_database.get("lock_english", "off") == "on" and is_english(message.text):
            await message.delete()
            return
        
        # قفل فارسی
        if json_database.get("lock_persian", "off") == "on" and is_persian(message.text):
            await message.delete()
            return
        
        # قفل لینک
        if json_database.get("lock_link", "off") == "on" and re.search(r'http[s]?://|www\.|t\.me/', message.text, re.IGNORECASE):
            await message.delete()
            return
        
        # قفل نام کاربری
        if json_database.get("lock_username", "off") == "on" and re.search(r'@\w+', message.text):
            await message.delete()
            return
        
        # قفل منشن
        if json_database.get("lock_mention", "off") == "on" and message.entities:
            for entity in message.entities:
                if entity.type == enums.MessageEntityType.MENTION:
                    await message.delete()
                    return
    
    # قفل ایموجی پرمیوم
    if json_database.get("lock_premium_emoji", "off") == "on" and message.entities:
        for entity in message.entities:
            if entity.type == enums.MessageEntityType.CUSTOM_EMOJI:
                await message.delete()
                return

@app.on_message(filters.me & filters.regex(f'^(.delsign)$'), group=101)
async def delete_signature_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        json_database.update({
            "signature": "off",
            "signature_text": ""
        })
        write("data.json", json.dumps(json_database))
        
        await m.edit_text("❌ **امضا غیرفعال شد**")
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.signstatus)$'), group=102)
async def signature_status_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        status = "✅ فعال" if json_database.get("signature", "off") == "on" else "❌ غیرفعال"
        signature_text = json_database.get("signature_text", "")
        
        status_text = (
            f"📝 **وضعیت امضا:**\n\n"
            f"🔹 **حالت:** {status}\n"
            f"🔹 **متن امضا:** `{signature_text if signature_text else '--'}`"
        )
        
        await m.edit_text(status_text)
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.downpriv)'), group=99)
async def download_private_content(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("❖ **لطفا لینک پست را وارد کنید**")
            return
        
        link = m.text.split()[1]
        await download_from_link(app, m, link)
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا:** `{str(e)}`")

async def download_from_link(app, m: Message, link: str):
    try:
        if "t.me/c/" in link:
            parts = link.split('/')
            chat_id = int("-100" + parts[4])
            message_id = int(parts[5])
            await process_download(app, m, chat_id, message_id)
        else:
            await m.edit_text("❖ **لینک کانال خصوصی نامعتبر است**")
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا در پردازش لینک:** `{str(e)}`")

async def process_download(app, m: Message, chat_id: int, message_id: int):
    try:
        status_msg = await m.edit_text("🔍 **در حال دریافت پیام...**")
        
        try:
            target_message = await app.get_messages(chat_id, message_id)
        except errors.ChannelPrivate:
            await status_msg.edit("❖ **کانال خصوصی است یا دسترسی ندارم**")
            return
        except Exception as e:
            await status_msg.edit(f"❖ **خطا در دریافت پیام:** `{str(e)}`")
            return
        
        if target_message.photo:
            await status_msg.edit("📷 **در حال دانلود عکس...**")
            file_path = await app.download_media(target_message.photo.file_id)
            await status_msg.edit("📤 **در حال آپلود عکس...**")
            await app.send_photo(m.chat.id, file_path)
            
        elif target_message.video:
            await status_msg.edit("🎥 **در حال دانلود ویدیو...**")
            file_path = await app.download_media(target_message.video.file_id)
            await status_msg.edit("📤 **در حال آپلود ویدیو...**")
            await app.send_video(m.chat.id, file_path)
            
        elif target_message.document:
            await status_msg.edit("📄 **در حال دانلود فایل...**")
            file_path = await app.download_media(target_message.document.file_id)
            await status_msg.edit("📤 **در حال آپلود فایل...**")
            file_name = target_message.document.file_name if target_message.document.file_name else "file"
            await app.send_document(m.chat.id, file_path, file_name=file_name)
            
        elif target_message.audio:
            await status_msg.edit("🎵 **در حال دانلود صوت...**")
            file_path = await app.download_media(target_message.audio.file_id)
            await status_msg.edit("📤 **در حال آپلود صوت...**")
            title = target_message.audio.title if target_message.audio.title else "Audio"
            performer = target_message.audio.performer if target_message.audio.performer else ""
            await app.send_audio(m.chat.id, file_path, title=title, performer=performer)
            
        elif target_message.voice:
            await status_msg.edit("🎤 **در حال دانلود ویس...**")
            file_path = await app.download_media(target_message.voice.file_id)
            await status_msg.edit("📤 **در حال آپلود ویس...**")
            await app.send_voice(m.chat.id, file_path)
            
        elif target_message.sticker:
            await status_msg.edit("🖼️ **در حال دانلود استیکر...**")
            file_path = await app.download_media(target_message.sticker.file_id)
            await status_msg.edit("📤 **در حال آپلود استیکر...**")
            await app.send_sticker(m.chat.id, file_path)
            
        elif target_message.animation:
            await status_msg.edit("🎞️ **در حال دانلود گیف...**")
            file_path = await app.download_media(target_message.animation.file_id)
            await status_msg.edit("📤 **در حال آپلود گیف...**")
            await app.send_animation(m.chat.id, file_path)
            
        elif target_message.text:
            await status_msg.edit("📝 **در حال ارسال متن...**")
            await app.send_message(m.chat.id, target_message.text)
            
        else:
            await status_msg.edit("❖ **محتوای قابل ارسال یافت نشد**")
            return
        
        try:
            if 'file_path' in locals() and file_path and os.path.exists(file_path):
                os.remove(file_path)
        except:
            pass
            
        await status_msg.delete()
            
    except Exception as e:
        await m.edit_text(f"❖ **خطا:** `{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.download') & filters.private)
async def download_and_send_file(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**❖ Usage:** `.download [direct_link]`")
            return
        
        url = m.text.split()[1]
        
        # بررسی اینکه لینک معتبر است
        parsed_url = urlparse(url)
        if not parsed_url.scheme in ['http', 'https']:
            await m.edit_text("**❖ لینک نامعتبر! لطفاً یک لینک مستقیم وارد کنید**")
            return
        
        await m.edit_text("**🔍 در حال بررسی لینک...**")
        
        # دریافت اطلاعات فایل
        async with aiohttp.ClientSession() as session:
            async with session.head(url) as response:
                if response.status != 200:
                    await m.edit_text("**❖ لینک قابل دسترسی نیست**")
                    return
                
                content_type = response.headers.get('Content-Type', '')
                content_length = response.headers.get('Content-Length')
                
                if content_length and int(content_length) > 2000 * 1024 * 1024:  # محدودیت 2GB تلگرام
                    await m.edit_text("**❖ سایز فایل از محدودیت تلگرام بیشتر است**")
                    return
        
        await m.edit_text("**📥 در حال دانلود فایل...**")
        
        # دانلود فایل
        file_name = os.path.basename(parsed_url.path) or "downloaded_file"
        temp_file = f"downloads/{file_name}"
        
        # ایجاد پوشه downloads اگر وجود ندارد
        os.makedirs("downloads", exist_ok=True)
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    async with aiofiles.open(temp_file, 'wb') as file:
                        async for chunk in response.content.iter_chunked(8192):
                            await file.write(chunk)
        
        await m.edit_text("**📤 در حال آپلود فایل...**")
        
        # ارسال فایل بر اساس نوع آن
        if 'image' in content_type:
            await app.send_photo(m.chat.id, temp_file, caption=f"**📷 فایل دانلود شده**\n`{file_name}`")
        elif 'video' in content_type:
            await app.send_video(m.chat.id, temp_file, caption=f"**🎥 فایل دانلود شده**\n`{file_name}`")
        elif 'audio' in content_type:
            await app.send_audio(m.chat.id, temp_file, caption=f"**🎵 فایل دانلود شده**\n`{file_name}`")
        else:
            await app.send_document(m.chat.id, temp_file, caption=f"**📄 فایل دانلود شده**\n`{file_name}`")
        
        # حذف فایل موقت
        try:
            os.remove(temp_file)
        except:
            pass
        
        await m.delete()
        
    except Exception as e:
        await m.edit_text(f"**❖ خطا در دانلود:**\n`{str(e)}`")
        
        # حذف فایل موقت در صورت خطا
        try:
            if 'temp_file' in locals() and os.path.exists(temp_file):
                os.remove(temp_file)
        except:
            pass

@app.on_message(filters.me & filters.regex(r'^\.getinfo') & filters.private)
async def get_file_info(app, m: Message):
    """دریافت اطلاعات فایل از لینک"""
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("**❖ Usage:** `.getinfo [direct_link]`")
            return
        
        url = m.text.split()[1]
        await m.edit_text("**🔍 در حال دریافت اطلاعات فایل...**")
        
        async with aiohttp.ClientSession() as session:
            async with session.head(url) as response:
                if response.status != 200:
                    await m.edit_text("**❖ لینک قابل دسترسی نیست**")
                    return
                
                info_text = "**📊 اطلاعات فایل:**\n\n"
                info_text += f"**• وضعیت:** `{response.status}`\n"
                info_text += f"**• نوع محتوا:** `{response.headers.get('Content-Type', 'نامشخص')}`\n"
                
                content_length = response.headers.get('Content-Length')
                if content_length:
                    size_mb = int(content_length) / (1024 * 1024)
                    info_text += f"**• سایز فایل:** `{size_mb:.2f} MB`\n"
                else:
                    info_text += "**• سایز فایل:** `نامشخص`\n"
                
                info_text += f"**• آخرین تغییر:** `{response.headers.get('Last-Modified', 'نامشخص')}`\n"
                info_text += f"**• سرور:** `{response.headers.get('Server', 'نامشخص')}`\n"
                
                await m.edit_text(info_text)
                
    except Exception as e:
        await m.edit_text(f"**❖ خطا:**\n`{str(e)}`")
# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.setbot)'), group=34)
async def set_bot_token_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("❖ **Usage:** `.setbot <token>`")
            return
        
        token = m.text.split()[1]
        
        if not token.count(':') == 1:
            await m.edit_text("❖ **Invalid token format!**")
            return
        
        json_database = json_read("data.json")
        json_database.update({"bot_token": token})
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(f"✅ **Bot token saved**\n\n`{token[:10]}...{token[-10:]}`")
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.setbackup)$'), group=35)
async def set_backup_channel_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        if m.chat.type not in [enums.ChatType.CHANNEL, enums.ChatType.SUPERGROUP]:
            await m.edit_text("❖ **Command only works in channels/supergroups**")
            return
        
        try:
            chat_member = await app.get_chat_member(m.chat.id, "me")
            if chat_member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
                await m.edit_text("❖ **Bot must be admin in this channel**")
                return
        except Exception:
            await m.edit_text("❖ **Bot access denied**")
            return
        
        json_database.update({
            "backup_channel": m.chat.id,
            "backup_channel_title": m.chat.title
        })
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(f"✅ **Backup channel set**\n\n**Title:** {m.chat.title}\n**ID:** `{m.chat.id}`")
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.autosave)'), group=36)
async def autosave_toggle_handler(app, m: Message):
    try:
        if len(m.text.split()) < 2:
            await m.edit_text("❖ **Usage:** `.autosave on/off`")
            return
        
        command = m.text.split()[1].lower()
        json_database = json_read("data.json")
        
        if command == "on":
            if "bot_token" not in json_database or not json_database["bot_token"]:
                await m.edit_text("❖ **Set bot token first:** `.setbot <token>`")
                return
            
            if "backup_channel" not in json_database or not json_database["backup_channel"]:
                await m.edit_text("❖ **Set backup channel first:** `.setbackup`")
                return
            
            json_database.update({"autosave_enabled": "on"})
            write("data.json", json.dumps(json_database))
            await m.edit_text("✅ **Auto-save enabled**")
            
        elif command == "off":
            json_database.update({"autosave_enabled": "off"})
            write("data.json", json.dumps(json_database))
            await m.edit_text("❌ **Auto-save disabled**")
            
        else:
            await m.edit_text("❖ **Usage:** `.autosave on/off`")
            
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.setautosave)$'), group=37)
async def set_autosave_chat_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        json_database.update({
            "autosave_chat": m.chat.id,
            "autosave_chat_title": m.chat.title if hasattr(m.chat, 'title') else "Private Chat"
        })
        write("data.json", json.dumps(json_database))
        
        await m.edit_text(f"✅ **Report chat set**\n\n**Title:** {m.chat.title if hasattr(m.chat, 'title') else 'Private Chat'}\n**ID:** `{m.chat.id}`")
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.savestatus)$'), group=94)
async def save_status_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        status_text = "📊 **Save System Status**\n\n"
        
        bot_token = json_database.get("bot_token", "❌ Not set")
        if bot_token != "❌ Not set":
            bot_token_display = f"`{bot_token[:10]}...{bot_token[-10:]}`"
        else:
            bot_token_display = bot_token
        status_text += f"• **Bot Token:** {bot_token_display}\n"
        
        backup_channel = json_database.get("backup_channel")
        if backup_channel:
            backup_title = json_database.get("backup_channel_title", "Unknown")
            status_text += f"• **Backup Channel:** {backup_title} (`{backup_channel}`)\n"
        else:
            status_text += "• **Backup Channel:** ❌ Not set\n"
        
        autosave_chat = json_database.get("autosave_chat")
        if autosave_chat:
            chat_title = json_database.get("autosave_chat_title", "Unknown")
            status_text += f"• **Report Chat:** {chat_title} (`{autosave_chat}`)\n"
        else:
            status_text += "• **Report Chat:** ❌ Not set\n"
        
        autosave_status = json_database.get("autosave_enabled", "off")
        status_emoji = "✅ ON" if autosave_status == "on" else "❌ OFF"
        status_text += f"• **System Status:** {status_emoji}\n"
        
        saved_count = json_database.get("saved_messages_count", 0)
        deleted_count = json_database.get("deleted_messages_count", 0)
        status_text += f"• **Saved Messages:** `{saved_count}`\n"
        status_text += f"• **Deleted Messages:** `{deleted_count}`\n"
        
        await m.edit_text(status_text)
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

@app.on_message(filters.private & filters.incoming & ~filters.me & ~filters.bot, group=95)
async def auto_save_messages_handler(app, message: Message):
    try:
        json_database = json_read("data.json")
        
        if json_database.get("autosave_enabled", "off") != "on":
            return
        
        backup_channel = json_database.get("backup_channel")
        if not backup_channel:
            return
        
        try:
            forwarded_msg = await message.forward(backup_channel)
            
            message_data = {
                "message_id": message.id,
                "user_id": message.from_user.id if message.from_user else None,
                "user_first_name": message.from_user.first_name if message.from_user else "Unknown",
                "date": message.date.isoformat() if message.date else None,
                "forwarded_message_id": forwarded_msg.id,
                "backup_channel": backup_channel
            }
            
            saved_count = json_database.get("saved_messages_count", 0)
            json_database["saved_messages_count"] = saved_count + 1
            write("data.json", json.dumps(json_database))
            
            if json_database.get("autosave_chat"):
                log_text = (
                    f"💾 **Message Saved**\n\n"
                    f"**From:** {message.from_user.mention if message.from_user else 'Unknown'}\n"
                    f"**User ID:** `{message.from_user.id if message.from_user else 'Unknown'}`\n"
                    f"**Time:** `{message.date}`\n"
                    f"**Content:** `{message.text[:100] if message.text else 'Media/File'}...`"
                )
                await app.send_message(json_database["autosave_chat"], log_text)
                
        except Exception as e:
            if json_database.get("autosave_chat"):
                error_text = f"❌ **Save Error:**\n`{str(e)}`"
                await app.send_message(json_database["autosave_chat"], error_text)
            
    except Exception as e:
        pass

@app.on_deleted_messages(filters.private, group=96)
async def deleted_messages_handler(app, messages):
    try:
        json_database = json_read("data.json")
        
        autosave_chat = json_database.get("autosave_chat")
        if not autosave_chat:
            return
        
        for message in messages:
            report_text = (
                f"🗑️ **Message Deleted**\n\n"
                f"**Message ID:** `{message.id}`\n"
                f"**Delete Time:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`\n"
            )
            
            if hasattr(message, 'from_user') and message.from_user:
                report_text += f"**User:** {message.from_user.mention}\n"
                report_text += f"**User ID:** `{message.from_user.id}`\n"
            
            if hasattr(message, 'text') and message.text:
                report_text += f"**Text:** `{message.text[:200]}{'...' if len(message.text) > 200 else ''}`\n"
            else:
                report_text += "**Type:** Media/File\n"
            
            await app.send_message(autosave_chat, report_text)
            
            deleted_count = json_database.get("deleted_messages_count", 0)
            json_database["deleted_messages_count"] = deleted_count + 1
            write("data.json", json.dumps(json_database))
            
    except Exception as e:
        pass

@app.on_message(filters.me & filters.regex(f'^(.clearsave)$'), group=97)
async def clear_save_data_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        keys_to_keep = ["bot_token", "backup_channel", "backup_channel_title", 
                       "autosave_chat", "autosave_chat_title", "autosave_enabled"]
        
        cleared_data = {key: json_database.get(key) for key in keys_to_keep}
        cleared_data.update({
            "saved_messages_count": 0,
            "deleted_messages_count": 0
        })
        
        write("data.json", json.dumps(cleared_data))
        
        await m.edit_text("✅ **All save data cleared**")
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(f'^(.testsave)$'), group=98)
async def test_save_system_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        if json_database.get("autosave_enabled", "off") != "on":
            await m.edit_text("❌ **Auto-save is disabled**")
            return
        
        if not json_database.get("backup_channel"):
            await m.edit_text("❌ **Backup channel not set**")
            return
        
        test_message = await app.send_message(
            "me",
            "🔧 **System Test Message**\n\n"
            "This is a test message for the auto-save system.\n"
            f"**Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        
        await asyncio.sleep(2)
        
        await m.edit_text("✅ **System test completed**")
        
    except Exception as e:
        await m.edit_text(f"❖ **Error:**\n`{str(e)}`")

def initialize_save_system():
    try:
        json_database = json_read("data.json")
        
        new_fields = {
            "bot_token": "",
            "backup_channel": None,
            "backup_channel_title": "",
            "autosave_chat": None,
            "autosave_chat_title": "",
            "autosave_enabled": "off",
            "saved_messages_count": 0,
            "deleted_messages_count": 0
        }
        
        updated = False
        for field, default_value in new_fields.items():
            if field not in json_database:
                json_database[field] = default_value
                updated = True
        
        if updated:
            write("data.json", json.dumps(json_database))
            
    except Exception as e:
        print(f"Save system init error: {e}")

initialize_save_system()


@app.on_message(filters.me & filters.regex(f'^(.monshi)'), group=89)
def monshi_commands(app, m: Message):
    json_database = json_read("data.json")
    command = m.text.split()
    
    if len(command) < 2:
        m.edit_text("❖ **Usage:**\n"
                   "❖ `.monshi on` - فعال کردن\n"
                   "❖ `.monshi off` - غیرفعال کردن\n"
                   "❖ `.monshi text [متن]` - تنظیم متن پاسخ\n"
                   "❖ `.monshi delay [ثانیه]` - تنظیم وقفه\n"
                   "❖ `.monshi delay off` - غیرفعال کردن وقفه\n"
                   "❖ `.monshi status` - نمایش وضعیت")
        return
    
    sub_command = command[1].lower()
    
    if sub_command == "on":
        json_database.update({"monshi": "on"})
        write("data.json", json.dumps(json_database))
        m.edit_text("❖ **ربات منشی فعال شد** ✅")
        
    elif sub_command == "off":
        json_database.update({"monshi": "off"})
        write("data.json", json.dumps(json_database))
        # پاک کردن تاریخچه زمان‌ها
        last_response_time.clear()
        m.edit_text("❖ **ربات منشی غیرفعال شد** ❌")
        
    elif sub_command == "text":
        if len(command) < 3:
            m.edit_text("❖ **لطفا متن پاسخ را وارد کنید:**\n`.monshi text [متن جدید]`")
            return
        
        new_text = " ".join(command[2:])
        json_database.update({"monshi_text": new_text})
        write("data.json", json.dumps(json_database))
        m.edit_text(f"❖ **متن پاسخ به روز شد:**\n`{new_text}`")
        
    elif sub_command == "delay":
        if len(command) < 3:
            m.edit_text("❖ **لطفا زمان وقفه را وارد کنید:**\n`.monshi delay [ثانیه]`")
            return
        
        delay_arg = command[2].lower()
        
        if delay_arg == "off":
            json_database.update({"monshi_delay": 0})
            write("data.json", json.dumps(json_database))
            m.edit_text("❖ **زمان وقفه غیرفعال شد** ⚡")
            
        elif delay_arg.isdigit():
            delay_seconds = int(delay_arg)
            if delay_seconds < 0:
                m.edit_text("❖ **زمان وقفه نمی‌تواند منفی باشد**")
                return
                
            json_database.update({"monshi_delay": delay_seconds})
            write("data.json", json.dumps(json_database))
            m.edit_text(f"❖ **زمان وقفه تنظیم شد به:** `{delay_seconds}` ثانیه")
            
        else:
            m.edit_text("❖ **لطفا یک عدد معتبر وارد کنید**")
            
    elif sub_command == "status":
        status = "✅ فعال" if json_database.get("monshi", "off") == "on" else "❌ غیرفعال"
        text = json_database.get("monshi_text", "در حال حاضر در دسترس نیستم. به زودی پاسخ می‌دهم.")
        delay = json_database.get("monshi_delay", 0)
        delay_status = f"`{delay}` ثانیه" if delay > 0 else "❌ غیرفعال"
        
        status_text = (
            f"❖ **وضعیت ربات منشی:**\n\n"
            f"🔹 **حالت:** {status}\n"
            f"🔹 **متن پاسخ:** `{text}`\n"
            f"🔹 **زمان وقفه:** {delay_status}\n"
            f"🔹 **کاربران فعال:** `{len(last_response_time)}`"
        )
        m.edit_text(status_text)
        
    else:
        m.edit_text("❖ **دستور نامعتبر!**\nاز `.monshi` برای راهنما استفاده کنید.")

# |====================================| #

@app.on_message(filters.photo , group=334)
async def onphoto(c: Client, m: Message) :
    try :
        if m.photo.ttl_seconds :
            rand = random.randint(1000, 9999999)
            local = f"downloads/photo-{rand}.png"
            await app.download_media(message=m, file_name=f"photo-{rand}.png")
            await app.send_photo(chat_id=admin, photo=local, caption=f"🔥 New timed image {m.photo.date} | time: {m.photo.ttl_seconds}s")
            os.remove(local)
    except :
        pass

# |====================================| #

@app.on_message(filters.video , group=335)
async def onvideo(c: Client, m: Message) :
    try :
        if m.video.ttl_seconds :
            rand = random.randint(1000, 9999999)
            local = f"downloads/video-{rand}.mp4"
            await app.download_media(message=m, file_name=f"video-{rand}.mp4")
            await app.send_video(chat_id=admin, video=local, caption=f"🔥 New timed video {m.video.date} | time: {m.video.ttl_seconds}s")
            os.remove(local)
    except :
        pass

# |====================================| #

@app.on_message( filters.private , group=33)
async def actions1(app, message):
 text = message.text
 json_database = json_read("data.json")
 json_list = json_read("list.json")
 chat_id = message.chat.id
 if (json_database["pvlock"] == "on" and chat_id != admin):
    await message.delete()
 elif (json_database["monshi"] == "on" and chat_id != admin):
     if (json_list[f"{text}"]):
         ab = json_list[f"{text}"]
         await app.send_message(chat_id=chat_id,text=f"{ab}",reply_to_message_id=message.id)

# |====================================| #

@app.on_message(filters.incoming , group=333)       
async def mes(app, message):
    if message and message.from_user.id in enemy:
        try:
            s = fosh_saz(text=".")
            await message.reply(s)
            await asyncio.sleep(1)
        except Exception as ssss:
            print()
    elif message and message.from_user.id in love:
        try:
            l = ["❤️","💖","💝","💞","💕","💘","💗","💓"]
            lo = choice(l)
            s = love_saz(text=f"{lo}")
            await message.reply(s)
            await asyncio.sleep(1)
        except Exception as ssss:
            print(ssss)
    elif message and message.from_user.id in mutey:
        try:
            await app.delete_messages(message.chat.id , message.id)
        except :
            pass

# |====================================| #

spam_chats = []
def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

# |====================================| #

@app.on_message(filters.command("tagall", ".") & filters.me)
async def mentionall(app, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("**Send me a message or reply to a message!**")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in app.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id})✧ "
        if usrnum == 13:
            if args:
                txt = f"{args}\n\n{usrtxt}"
                await app.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            sleep(1)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

# |====================================| #

@app.on_message(filters.command("cancel", ".") & filters.me)
async def cancel_spam(app, message: Message):
    if not message.chat.id in spam_chats:
        return await message.edit("**It seems there is no tagall here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Cancelled.**")

# |====================================| #

json_database = json_read("data.json")
@app.on_message(filters.command(["restart", "reset", "ریست"], ".") & language_filter & filters.me)
def reset(app, m: Message):
    json_database = json_read("data.json")
    current_lang = json_database.get("language", "fa")
    
    if current_lang == "fa":
        app.send_message(m.chat.id ,"**ریستارت سلف با موفقیت انجام شد**", reply_to_message_id=m.id)
    else:
        app.send_message(m.chat.id ,"**Jack Self Restart was successful**", reply_to_message_id=m.id)
    
    python = sys.executable
    os.execl(python, python, *sys.argv)

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.contact_list)$'), group=91)
async def contact_list_handler(app, m: Message):
    """نمایش لیست مخاطبین ذخیره شده"""
    try:
        await m.edit_text("❖ **در حال دریافت لیست مخاطبین...**")
        
        # دریافت مخاطبین
        contacts = await app.invoke(functions.contacts.GetContacts(hash=0))
        
        if not contacts.contacts:
            await m.edit_text("❖ **لیست مخاطبین خالی است**")
            return
        
        # ایجاد لیست مخاطبین
        contact_list = "📋 **لیست مخاطبین ذخیره شده:**\n\n"
        
        for i, contact in enumerate(contacts.contacts[:50], 1):  # محدود به 50 مخاطب
            user_id = contact.user_id
            try:
                user = await app.get_users(user_id)
                # بررسی نوع مخاطب
                contact_type = "📞 دارای شماره" if hasattr(contact, 'phone') and contact.phone else "👤 بدون شماره"
                
                contact_list += (
                    f"{i}. **{user.first_name or '--'}** {user.last_name or ''}\n"
                    f"   ├ آیدی: `{user.id}`\n"
                    f"   ├ یوزرنیم: @{user.username or '--'}\n"
                    f"   └ نوع: {contact_type}\n\n"
                )
            except:
                contact_list += f"{i}. کاربر با آیدی `{user_id}`\n\n"
        
        if len(contacts.contacts) > 50:
            contact_list += f"\n📊 **و {len(contacts.contacts) - 50} مخاطب دیگر...**"
        
        # آمار کلی
        total_contacts = len(contacts.contacts)
        contact_list += f"\n**📈 آمار کلی:** {total_contacts} مخاطب"
        
        await m.edit_text(contact_list)
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا در دریافت لیست مخاطبین:**\n`{str(e)}`")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.contact_delete)'), group=92)
async def contact_delete_handler(app, m: Message):
    """حذف مخاطب از لیست"""
    try:
        if len(m.text.split()) < 2:
            await m.edit_text(
                "❖ **راهنمای حذف مخاطب:**\n\n"
                "• `.contact_delete [user_id]` - حذف با آیدی\n"
                "• `.contact_delete all` - حذف همه مخاطبین\n"
                "• `.contact_delete list` - مشاهده و انتخاب برای حذف"
            )
            return
        
        target = m.text.split()[1]
        
        if target.lower() == "all":
            # حذف همه مخاطبین
            await m.edit_text("❖ **در حال حذف همه مخاطبین...**")
            result = await app.invoke(functions.contacts.ResetSaved())
            await m.edit_text("✅ **همه مخاطبین با موفقیت حذف شدند**")
            
        elif target.lower() == "list":
            # نمایش لیست برای انتخاب
            await show_contact_delete_list(app, m)
            
        else:
            # حذف مخاطب خاص
            try:
                user_id = int(target)
                await m.edit_text(f"❖ **در حال حذف مخاطب با آیدی {user_id}...**")
                
                # حذف مخاطب
                result = await app.invoke(
                    functions.contacts.DeleteContacts(id=[await app.resolve_peer(user_id)])
                )
                
                await m.edit_text(f"✅ **مخاطب با آیدی `{user_id}` با موفقیت حذف شد**")
                
            except ValueError:
                await m.edit_text("❖ **لطفاً یک آیدی عددی معتبر وارد کنید**")
            except Exception as e:
                await m.edit_text(f"❖ **خطا در حذف مخاطب:**\n`{str(e)}`")
                
    except Exception as e:
        await m.edit_text(f"❖ **خطا در حذف مخاطب:**\n`{str(e)}`")

async def show_contact_delete_list(app, m: Message):
    """نمایش لیست مخاطبین برای حذف"""
    try:
        contacts = await app.invoke(functions.contacts.GetContacts(hash=0))
        
        if not contacts.contacts:
            await m.edit_text("❖ **لیست مخاطبین خالی است**")
            return
        
        contact_list = "🗑 **لیست مخاطبین برای حذف:**\n\n"
        contact_dict = {}
        
        for i, contact in enumerate(contacts.contacts[:20], 1):  # محدود به 20 مخاطب
            user_id = contact.user_id
            try:
                user = await app.get_users(user_id)
                contact_list += f"{i}. **{user.first_name or '--'}** (آیدی: `{user.id}`)\n"
                contact_dict[str(i)] = user_id
            except:
                contact_list += f"{i}. کاربر با آیدی `{user_id}`\n"
                contact_dict[str(i)] = user_id
        
        contact_list += "\n**📝 برای حذف:** `.contact_delete [شماره]`"
        
        # ذخیره دیکشنری برای استفاده بعدی
        m._contact_delete_dict = contact_dict
        
        await m.edit_text(contact_list)
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا در نمایش لیست حذف:**\n`{str(e)}`")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.contact_stats)$'), group=93)
async def contact_stats_handler(app, m: Message):
    """آمار مخاطبین"""
    try:
        await m.edit_text("❖ **در حال محاسبه آمار مخاطبین...**")
        
        contacts = await app.invoke(functions.contacts.GetContacts(hash=0))
        
        if not contacts.contacts:
            await m.edit_text("❖ **لیست مخاطبین خالی است**")
            return
        
        total_contacts = len(contacts.contacts)
        
        # محاسبه آمار
        stats_msg = (
            f"📊 **آمار مخاطبین:**\n\n"
            f"• **کل مخاطبین:** {total_contacts}\n"
            f"• **مخاطبین دارای شماره:** در حال محاسبه...\n"
            f"• **مخاطبین بدون شماره:** در حال محاسبه...\n"
            f"• **آخرین بروزرسانی:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        
        await m.edit_text(stats_msg)
        
    except Exception as e:
        await m.edit_text(f"❖ **خطا در محاسبه آمار:**\n`{str(e)}`")

# |====================================| #

@app.on_message(filters.me & filters.command(["resetall"], "."), group=17)
def reset_all(app, m: Message):
    try:
        # ریست تنظیمات در فایل data.json با حفظ تنظیمات پروفایل
        current_settings = json_read("data.json")
        
        default_settings = {
            "limitDel": 4,
            "welcome": "off", 
            "firstcom": "off",
            "timename": "off",
            "timebiov1": "off", 
            "fontname": "off",
            "fuck": "off",
            "anti_del": "off",
            "autoan": "off",
            "boldmode": "off",
            "emojimode": "off", 
            "underline": "off",
            "italicmode": "off",
            "codemode": "off",
            "strike": "off",
            "spoilermode": "off",
            "quotemode": "off",
            "pvlock": "off",
            "typing": "off",
            "mention": "off",
            "monshi": "off",
            "monshi_delay": 0,
            "monshi_text": "در حال حاضر در دسترس نیستم. به زودی پاسخ می‌دهم.",
            "timezone": "Asia/Tehran",
            "font": "Font1",
            # اضافه کردن تنظیمات اکشن‌ها به JSON
            "playing": "off",
            "typing_action": "off",
            "record_video": "off",
            "choose_sticker": "off",
            "upload_video": "off",
            "upload_document": "off",
            "upload_audio": "off",
            "speaking": "off",
            "all_playing": "off",
            "all_typing": "off",
            "all_record_video": "off",
            "all_choose_sticker": "off",
            "all_upload_video": "off",
            "all_upload_document": "off",
            "all_upload_audio": "off",
            "all_speaking": "off",
						"signatrue": "off",
						"signatrue_text": ""
        }
        
        write("data.json", json.dumps(default_settings))
        
        # پاک کردن لیست‌های موقت
        global enemy, love, mutey
        enemy.clear()
        love.clear() 
        mutey.clear()
        
        # پاک کردن فایل‌های موقت اکشن‌ها
        action_files = [
            "playing.txt", "typing.txt", "RECORD_VIDEO.txt", "CHOOSE_STICKER.txt",
            "UPLOAD_VIDEO.txt", "UPLOAD_DOCUMENT.txt", "UPLOAD_AUDIO.txt", "SPEAKING.txt",
            "allplaying.txt", "alltyping.txt", "allRECORD_VIDEO.txt", "allCHOOSE_STICKER.txt",
            "allUPLOAD_VIDEO.txt", "allUPLOAD_DOCUMENT.txt", "allUPLOAD_AUDIO.txt", "allSPEAKING.txt"
        ]
        
        for file in action_files:
            if os.path.exists(file):
                os.remove(file)
        
        m.edit_text("✅ **تمامی تنظیمات با موفقیت ریست شدند**\n\n• تنظیمات به حالت پیش‌فرض بازگشت\n• لیست‌های موقت پاک شدند\n• فایل‌های اکشن حذف شدند\n• پروفایل کاربر دست نخورده باقی ماند")
        
    except Exception as e:
        m.edit_text(f"❌ **خطا در ریست تنظیمات**:\n`{str(e)}`")

@app.on_message(filters.me & filters.regex(r'^\.fix_json$'))
async def fix_json_command(app, m: Message):
    try:
        await m.edit_text("🛠️ در حال تعمیر فایل data.json...")
        
        # ساختار صحیح با مقادیر پیش‌فرض
        correct_structure = {
            "language": "fa",
            "limitDel": 4,
            "welcome": "off",
            "firstcom": "off", 
            "timename": "on",
            "timebiov1": "off",
            "fontname": "on",
            "fuck": "off",
            "anti_del": "off",
            "autoan": "off",
            "boldmode": "off",
            "emojimode": "off",
            "underline": "off", 
            "italicmode": "off",
            "codemode": "off",
            "strike": "off",
            "spoilermode": "off",
            "quotemode": "off",
            "pvlock": "off",
            "typing": "off",
            "mention": "off",
            "monshi": "off",
            "monshi_delay": 0,
            "monshi_text": "در حال حاضر در دسترس نیستم. به زودی پاسخ می‌دهم.",
            "timezone": "Asia/Tehran",
            "font": "Font6",
            "playing": "off",
            "typing_action": "off",
            "record_video": "off",
            "choose_sticker": "off", 
            "upload_video": "off",
            "upload_document": "off",
            "upload_audio": "off",
            "speaking": "off",
            "all_playing": "off",
            "all_typing": "off",
            "all_record_video": "off",
            "all_choose_sticker": "off",
            "all_upload_video": "off",
            "all_upload_document": "off",
            "all_upload_audio": "off",
            "all_speaking": "off",
            "signature": "off",
            "signature_text": "",
            "auto_reaction": "off",
            "reaction_emoji": "🔥",
            "pv_silent": "off",
            "lock_text": "off",
            "lock_forward": "off",
            "lock_location": "off",
            "lock_photo": "off",
            "lock_video_note": "off",
            "lock_video": "off",
            "lock_link": "off",
            "lock_gif": "off",
            "lock_sticker": "off",
            "lock_english": "off",
            "lock_persian": "off",
            "lock_audio": "off",
            "lock_voice": "off",
            "lock_contact": "off",
            "lock_poll": "off",
            "lock_premium_emoji": "off",
            "lock_mention": "off",
            "fields": {},
            "auto_answers": {},
            "keep_online": "off",
            "poker_pv": "off",
            "poker_all": "off",
            "markall": "off",
            "markall_group": "off",
            "title_lock": "off",
            "lock_profile": "off",
            "group_silent": "off",
            "auto_leave": "off",
            "join_action": "off",
            "join_type": "none",
            "welcome": "off",
            "welcome_text": "خوش آمدید!",
            "typing_all_groups": "off",
            "anti_login": "off",
            "title_lock_chats": {},
            "lock_profile_chats": [],
            "silent_chats": {},
            "auto_leave_chats": [],
            "filter_words": {},
            "allow_words": {},
            "silent_users": {},
            "welcome_settings": {},
            "ban_all_users": [],
            "slow_mode_chats": {},
            "Bbackup_channel": -1003407819559,
            "Bbackup_channel_title": "• راهنماسلف | SHAH SELF •",
            "save_channel_id": -1003407819559,
            "saved_mades": {},
            "online_group_id": None
        }
        
        # ذخیره ساختار صحیح
        write("data.json", json.dumps(correct_structure, ensure_ascii=False, indent=2))
        
        await m.edit_text("✅ فایل data.json با موفقیت تعمیر شد!\n\nحالا دستور زیر را اجرا کنید:\n`.timename on`")
        
    except Exception as e:
        await m.edit_text(f"❌ خطا در تعمیر فایل:\n`{str(e)}`")
# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(ریست)$'), group=18)
def reset_all_persian(app, m: Message):
    """دستور ریست به فارسی"""
    reset_all(app, m)

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.ment)'), group=80)
def ment(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"mention":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Mention Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"mention":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Mention Mode is **OFF**")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.bold)'), group=81)
def bold(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"boldmode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Bold Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"boldmode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Bold Mode is **OFF**")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.spoiler)'), group=82)
def spoiler(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"spoilermode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Spoiler Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"spoilermode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ spoiler Mode is **OFF**")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.quote)'), group=82)
def quote(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"quotemode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ quote Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"quotemode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ quote Mode is **OFF**")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.italic)'), group=83)
def italic(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"italicmode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ italic Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"italicmode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ italic Mode is **OFF**")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.code)'), group=84)
def code(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"codemode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Code Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"codemode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Code Mode is **OFF**")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.strike)'), group=85)
def strike(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"strike":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Strike Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"strike":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Strike Mode is **OFF**")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.underline)'), group=86)
def underline(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"underline":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Underline Mode is **ON**")
  elif m.text.split()[1] == "off": 
   json_database.update({"underline":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Underline Mode is **OFF**")

# |====================================| #

@app.on_message(filters.command(["emoji"], "."), group=87)
def emoji2(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"emojimode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Emoji Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"emojimode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Emoji Mode is **OFF**")

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.limit)'), group=15)
def spamban(app, m: Message):
    app.unblock_user("SpamBot")
    response = app.send_message("spambot" , f"/start")
    wait = app.send_message(m.chat.id, "در حال بررسی وضعیت اکانت شما...")
    sleep(3)
    spambot_msg = response.id + 1
    status = app.get_messages(chat_id="SpamBot", message_ids=spambot_msg)
    wait.delete()
    app.send_message(m.chat.id, f"**STATUS**▬▬▬▬▬▬▬▬▬▬\n `{status.text}`\n▬▬▬▬▬▬▬▬▬▬**STATUS**", reply_to_message_id=m.id)

# |====================================| #

def get_text(message: Message) -> Union[str, None]:
    """Extract Text From Commands"""
    if message.text is None:
        return
    if " " not in message.text:
        return
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        pass

# |====================================| #

@app.on_message(filters.command(["ping", "پینگ"], ".") & filters.me)
async def ping(_, message: Message):
    start = perf_counter()
    await message.edit("<b>Pong!</b>")
    end = perf_counter()
    await message.edit(f"<b>Pong! {round(end - start, 3)}s</b>")

# |====================================| #

@app.on_message(filters.command(["session", "سشن"], ".") & filters.me)
async def sessions_list(app, message: Message):
    formatted_sessions = []
    sessions = (await app.invoke(GetAuthorizations())).authorizations
    for num, session in enumerate(sessions, 1):
        formatted_sessions.append(
            (
                "<b>{num}</b>. <b>{model}</b> on <code>{platform}</code>\n"
                "<b>Hash:</b> {hash}\n"
                "<b>App name:</b> <code>{app_name}</code> v.{version}\n"
                "<b>Created (last activity):</b> {created} ({last_activity})\n"
                "<b>IP and location: </b>: <code>{ip}</code> (<i>{location}</i>)\n"
                "<b>Official status:</b> <code>{official}</code>\n"
                "<b>2FA accepted:</b> <code>{password_pending}</code>\n"
                "<b>Can accept calls / secret chats:</b> {calls} / {secret_chats}"
            ).format(
                num=num,
                model=escape(session.device_model),
                platform=escape(
                    session.platform
                    if session.platform != ""
                    else "unknown platform"
                ),
                hash=session.hash,
                app_name=escape(session.app_name),
                version=escape(
                    session.app_version
                    if session.app_version != ""
                    else "unknown"
                ),
                created=datetime.fromtimestamp(
                    session.date_created
                ).isoformat(),
                last_activity=datetime.fromtimestamp(
                    session.date_active
                ).isoformat(),
                ip=session.ip,
                location=session.country,
                official="✅" if session.official_app else "❌️",
                password_pending="❌️️" if session.password_pending else "✅",
                calls="❌️️" if session.call_requests_disabled else "✅",
                secret_chats="❌️️"
                if session.encrypted_requests_disabled
                else "✅",
            )
        )
    answer = "<b>Active sessions at your account:</b>\n\n"
    chunk = []
    for s in formatted_sessions:
        chunk.append(s)
        if len(chunk) == 5:
            answer += "\n\n".join(chunk)
            await message.reply(answer)
            answer = ""
            chunk.clear()
    if len(chunk):
        await message.reply("\n\n".join(chunk))
    await message.delete()

# |====================================| #

@app.on_message(
    filters.command(["spam", "statspam", "slowspam"], ".") & filters.me
)
async def spam(app, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])
    spam_type = message.command[0]

    await message.delete()

    for msg in range(amount):
        if message.reply_to_message:
            sent = await message.reply_to_message.reply(text)
        else:
            sent = await app.send_message(message.chat.id, text)

        if spam_type == "statspam":
            await asyncio.sleep(0.1)
            await sent.delete()
        elif spam_type == "spam":
            await asyncio.sleep(0.1)
        elif spam_type == "slowspam":
            await asyncio.sleep(0.9)
@app.on_message(filters.command("fastspam", ".") & filters.me)
async def fastspam(app, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])

    await message.delete()

    coros = []
    for msg in range(amount):
        if message.reply_to_message:
            coros.append(message.reply_to_message.reply(text))
        else:
            coros.append(app.send_message(message.chat.id, text))
    await asyncio.wait(coros)

# |====================================| #

@app.on_message(
    filters.command(["join"], ".") & filters.me)
async def join(app, message: Message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`Processing...`")
    try:
        await app.join_chat(tex)
        await g.edit(f"**Successfully Joined Chat ID** `{tex}`")
    except Exception as ex:
        await g.edit(f"**ERROR:** \n\n{str(ex)}")


@app.on_message(
    filters.command(["leave"], ".") & filters.me)
async def leave(app, message: Message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`Processing...`")
    try:
        await xv.edit_text(f"{app.me.first_name} has left this group, bye!!")
        await app.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**ERROR:** \n\n{str(ex)}")


@app.on_message(
    filters.command(["leaveallgc"], ".") & filters.me)
async def kickmeall(app, message: Message):
    tex = await message.reply_text("`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in app.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await app.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(
        f"**Successfully left {done} Groups, Failed to left {er} Groups**"
    )


@app.on_message(filters.command(["leaveallch"], ".") & filters.me)
async def kickmeallch(app, message: Message):
    ok = await message.reply_text("`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in app.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await app.leave_chat(chat)
            except BaseException:
                er += 1
    await ok.edit(
        f"**Successfully left {done} Channel, failed to left {er} Channel**"
    )

# |====================================| #

@app.on_message(filters.command(["packinfo", "stickerinfo"], ".") & filters.me)
async def packinfo(app, message: Message):
    rep = await message.edit_text("`Processing...`")
    if not message.reply_to_message:
        await rep.edit("Please Reply To Sticker...")
        return
    if not message.reply_to_message.sticker:
        await rep.edit("Please Reply To A Sticker...")
        return
    if not message.reply_to_message.sticker.set_name:
        await rep.edit("`Seems Like A Stray Sticker!`")
        return
    stickerset = await app.invoke(
        GetStickerSet(
            stickerset=InputStickerSetShortName(
                short_name=message.reply_to_message.sticker.set_name
            ),
            hash=0,
        )
    )
    emojis = []
    for stucker in stickerset.packs:
        if stucker.emoticon not in emojis:
            emojis.append(stucker.emoticon)
    output = f"""**Sticker Pack Title **: `{stickerset.set.title}`
**Sticker Pack Short Name **: `{stickerset.set.short_name}`
**Stickers Count **: `{stickerset.set.count}`
**Archived **: `{stickerset.set.archived}`
**Official **: `{stickerset.set.official}`
**Masks **: `{stickerset.set.masks}`
**Animated **: `{stickerset.set.animated}`
**Emojis In Pack **: `{' '.join(emojis)}`
"""
    await rep.edit(output)

# |====================================| #

async def add_text_img(image_path, text):
    font_size = 12
    stroke_width = 1

    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""

    img = Image.open(image_path).convert("RGBA")
    img_info = img.info
    image_width, image_height = img.size
    font = ImageFont.truetype(
        font="cache/default.ttf",
        size=int(image_height * font_size) // 100,
    )
    draw = ImageDraw.Draw(img)

    char_width, char_height = font.getsize("A")
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(upper_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(lower_text, width=chars_per_line)

    if top_lines:
        y = 10
        for line in top_lines:
            line_width, line_height = font.getsize(line)
            x = (image_width - line_width) / 2
            draw.text(
                (x, y),
                line,
                fill="white",
                font=font,
                stroke_width=stroke_width,
                stroke_fill="black",
            )
            y += line_height

    if bottom_lines:
        y = image_height - char_height * len(bottom_lines) - 15
        for line in bottom_lines:
            line_width, line_height = font.getsize(line)
            x = (image_width - line_width) / 2
            draw.text(
                (x, y),
                line,
                fill="white",
                font=font,
                stroke_width=stroke_width,
                stroke_fill="black",
            )
            y += line_height

    final_image = os.path.join("memify.webp")
    img.save(final_image, **img_info)
    return final_image


async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


async def resize_media(media: str, video: bool, fast_forward: bool) -> str:
    if video:
        info_ = Media_Info.data(media)
        width = info_["pixel_sizes"][0]
        height = info_["pixel_sizes"][1]
        sec = info_["duration_in_ms"]
        s = round(float(sec)) / 1000

        if height == width:
            height, width = 512, 512
        elif height > width:
            height, width = 512, -1
        elif width > height:
            height, width = -1, 512

        resized_video = f"{media}.webm"
        if fast_forward:
            if s > 3:
                fract_ = 3 / s
                ff_f = round(fract_, 2)
                set_pts_ = ff_f - 0.01 if ff_f > fract_ else ff_f
                cmd_f = f"-filter:v 'setpts={set_pts_}*PTS',scale={width}:{height}"
            else:
                cmd_f = f"-filter:v scale={width}:{height}"
        else:
            cmd_f = f"-filter:v scale={width}:{height}"
        fps_ = float(info_["frame_rate"])
        fps_cmd = "-r 30 " if fps_ > 30 else ""
        cmd = f"ffmpeg -i {media} {cmd_f} -ss 00:00:00 -to 00:00:03 -an -c:v libvpx-vp9 {fps_cmd}-fs 256K {resized_video}"
        _, error, __, ___ = await run_cmd(cmd)
        os.remove(media)
        return resized_video

    image = Image.open(media)
    maxsize = 512
    scale = maxsize / max(image.width, image.height)
    new_size = (int(image.width * scale), int(image.height * scale))

    image = image.resize(new_size, Image.LANCZOS)
    resized_photo = "sticker.png"
    image.save(resized_photo)
    os.remove(media)
    return resized_photo

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

# |====================================| #

LOG_GROUP = None
log = []
@app.on_message(filters.command("tagalert on", ".") & filters.me)
async def set_no_log_p_m(app, message: Message):
    if LOG_GROUP != -100:
        if not message.chat.id in log:
            log.append(message.chat.id)
            await message.edit("**Tag alert Activated Successfully**")

# |====================================| #

@app.on_message(filters.command("tagalert off", ".") & filters.me)
async def set_no_log_p_m(app, message: Message):
        if message.chat.id in log:
            log.clear()
            await message.edit("**Tag alert DeActivated Successfully**")

# |====================================| #

@app.on_message(filters.group & filters.mentioned ,group=101)
async def log_tagged_messages(app, message: Message):
    if log:
        result = f"<b>📨 #TAGS #MESSAGE</b>\n<b> •User : </b>{message.from_user.mention}"
        result += f"\n<b> • Group : </b>{message.chat.title}"
        result += f"\n<b> • 👀 </b><a href = '{message.link}'>watch</a>"
        result += f"\n<b> • Message : </b><code>{message.text}</code>"
        await asyncio.sleep(0.5)
        await app.send_message(
        "me",
        result,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )

# |====================================| #

def convert_f(fahrenheit):
    f = float(fahrenheit)
    f = (f * 9 / 5) + 32
    return f
def convert_c(celsius):
    cel = float(celsius)
    cel = (cel - 32) * 5 / 9
    return cel

# |====================================| #

@app.on_message(filters.command(["e"], ".") & filters.me)
async def evaluation(app, m: Message):
    if len(m.text.split()) == 1:
        await message.edit("Usage: `.e 1000-7`")
        return
    q = m.text.split(None, 1)[1]
    try:
        ev = str(eval(q))
        if ev:
            if len(ev) >= 4096:
                file = open("self/output.txt", "w+")
                file.write(ev)
                file.close()
                await client.send_file(message.chat.id, "self/output.txt",
                                       caption="`Output too large, sending as file`")
                os.remove("self/output.txt")
                return
            else:
                await app.send_message(m.chat.id,"**Evaluation**▬▬▬▬▬▬▬▬▬\n\n**Query:**\n{}\n\n**Result:**\n`{}`\n\n▬▬▬▬▬▬▬▬▬▬**Evaluation**".format(q, ev), reply_to_message_id=m.id)
                return
        else:
            await m.edit("**Query:**\n{}\n\n**Result:**\n`None`".format(q))
            return
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        errors = traceback.format_exception(etype=exc_type, value=exc_obj, tb=exc_tb)
        await m.edit("Error: `{}`".format(errors))
        logging.exception("Evaluation error")

# |====================================| #

@app.on_message(filters.command(["t"], ".") & filters.me)
async def evaluation_temp(app, m: Message):
    if len(m.text.split()) <= 2:
        await app.send_message(m.chat.id,"Usage: `.t 30 C` or `.t 60 F`", reply_to_message_id=m.id)
        return
    temp1 = m.text.split(None, 2)[1]
    temp2 = m.text.split(None, 2)[2]
    try:
        if temp2 == "F":
            result = convert_c(temp1)
            text = "**Temperature Converter**▬▬▬▬\n\n`{}°F` = `{}°C`\n\n▬▬▬▬**Tempreture Converter**".format(temp1, result)
            await app.send_message(m.chat.id,text, reply_to_message_id=m.id)
        elif temp2 == "C":
            result = convert_f(temp1)
            text = "**Temperature Converter**▬▬▬▬\n\n`{}°C` = `{}°F`\n\n▬▬▬▬**Tempreture Converter**".format(temp1, result)
            await app.send_message(m.chat.id,text, reply_to_message_id=m.id)
        else:
            await app.send_message(m.chat.id,"Unknown type {}\nC\nF\nبه صورت حرف بزرگ وارد کنید".format(temp2), reply_to_message_id=m.id)
    except ValueError as err:
        await app.send_message(m.chat.id,str(err), reply_to_message_id=m.id)

# |====================================| #

@app.on_message(filters.command(["delenemy"], ".") & filters.me)
async def delenemy(app, message: Message):
        id = message.reply_to_message.from_user.id
        try:
            enemy.remove(message.reply_to_message.from_user.id)
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**Enemy** Deleted from list.")
        except Exception as ki:
            await app.edit_message_text(message.chat.id, message.id,
                                            "❈This **id**  does not exist in enemy list. %s" % ki)

# |====================================| #

@app.on_message(filters.command(["enemylist"], ".") & filters.me)  
async def enemylist(app, message: Message):
        string = enemy
        await app.edit_message_text(message.chat.id, message.id, "❈**E**nemy List:%s" % string)
@app.on_message(filters.command(["setenemy"], ".") & filters.me)  
async def setenemy(app, message: Message):
        ss = message.reply_to_message.from_user.id
        try:
            enemy.append(message.reply_to_message.from_user.id)
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**Added** To Enemy List.")
        except Exception as m:
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**User** In Enemy List %s ." % m)

# |====================================| #

@app.on_message(filters.command(["dellove"], ".") & filters.me)
async def dellove(app, message: Message):
        id = message.reply_to_message.from_user.id
        try:
            love.remove(message.reply_to_message.from_user.id)
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**LOVE** Deleted from list.")
        except Exception as ki:
            await app.edit_message_text(message.chat.id, message.id,
                                            "❈This **id**  does not exist in LOVE list. %s" % ki)

# |====================================| #

@app.on_message(filters.command(["lovelist"], ".") & filters.me)  
async def lovelist(app, message: Message):
        string = love
        await app.edit_message_text(message.chat.id, message.id, "❈**L**ove List:%s" % string)
@app.on_message(filters.command(["setlove"], ".") & filters.me)  
async def setlove(app, message: Message):
        ss = message.reply_to_message.from_user.id
        try:
            love.append(message.reply_to_message.from_user.id)
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**Added** To LOVE List.")
        except Exception as m:
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**User** In LOVE List %s ." % m)

# |====================================| #

@app.on_message(filters.command(["Pass"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/overlay/Passed?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)

# |====================================| #

@app.on_message(filters.command(["resta"], ".") & filters.me)
async def offline_now(app, m: Message):
    await app.send_message(m.chat.id,"AutoOnline deactivated\nRestart...", reply_to_message_id=m.id)
    await app.send_message(m.chat.id ,"**Jack Self Restart was successful**", reply_to_message_id=m.id)
    python = sys.executable
    os.execl(python, python, *sys.argv)

# |====================================| #

# |====================================| #

@app.on_message(filters.me, group=31)
async def modes(app , message):
    json_database = json_read("data.json")
    
    if message.text == ".playing on":
        json_database.update({"playing": "on"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='playing action is on' , message_id=message.id)

    if message.text == ".playing off":
        json_database.update({"playing": "off"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='playing action is off' , message_id=message.id)

    if message.text == ".typing on":
        json_database.update({"typing_action": "on"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='typing action is on' , message_id=message.id)

    if message.text == ".typing off":
        json_database.update({"typing_action": "off"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='typing action is off' , message_id=message.id)

    if message.text == ".record_vid on":
        json_database.update({"record_video": "on"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='RECORD_VIDEO action is on' , message_id=message.id)

    if message.text == ".record_vid off":
        json_database.update({"record_video": "off"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='RECORD_VIDEO action is off' , message_id=message.id)

    if message.text == ".choose_sticker on":
        json_database.update({"choose_sticker": "on"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='CHOOSE_STICKER action is on' , message_id=message.id)

    if message.text == ".choose_sticker off":
        json_database.update({"choose_sticker": "off"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='CHOOSE_STICKER action is off' , message_id=message.id)

    if message.text == ".upload_vid on":
        json_database.update({"upload_video": "on"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_VIDEO action is on' , message_id=message.id)

    if message.text == ".upload_vid off":
        json_database.update({"upload_video": "off"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_VIDEO action is off' , message_id=message.id)

    if message.text == ".upload_doc on":
        json_database.update({"upload_document": "on"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_DOCUMENT action is on' , message_id=message.id)

    if message.text == ".upload_doc off":
        json_database.update({"upload_document": "off"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_DOCUMENT action is off' , message_id=message.id)

    if message.text == ".upload_audio on":
        json_database.update({"upload_audio": "on"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_AUDIO action is on' , message_id=message.id)

    if message.text == ".upload_audio off":
        json_database.update({"upload_audio": "off"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_AUDIO action is off' , message_id=message.id)

    if message.text == ".speaking on":
        json_database.update({"speaking": "on"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='SPEAKING action is on' , message_id=message.id)

    if message.text == ".speaking off":
        json_database.update({"speaking": "off"})
        write("data.json", json.dumps(json_database))
        await app.edit_message_text(chat_id=message.chat.id , text='SPEAKING action is off' , message_id=message.id)

# |====================================| #

@app.on_message(~filters.me & ((filters.private & ~filters.bot) | (filters.mentioned & filters.group)))       
async def Actions(app , message):
    json_database = json_read("data.json")
    
    if json_database.get("playing", "off") == "on":
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.PLAYING)

    if json_database.get("typing_action", "off") == "on":
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.TYPING)

    if json_database.get("record_video", "off") == "on":
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.RECORD_VIDEO)

    if json_database.get("choose_sticker", "off") == "on":
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.CHOOSE_STICKER)

    if json_database.get("upload_video", "off") == "on":
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.UPLOAD_VIDEO)

    if json_database.get("upload_document", "off") == "on":
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.UPLOAD_DOCUMENT)

    if json_database.get("upload_audio", "off") == "on":
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.UPLOAD_AUDIO)

    if json_database.get("speaking", "off") == "on":
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.SPEAKING)

# |====================================| #

def fbky(_ , __ , m:Message):
 try:
  if m.from_user.id in mutey :
   return True
  else:
   return False 
 except:
  pass

# |====================================| #

@app.on_message(filters.me & filters.regex(f'^(.wiki)'), group=14)
def wiki(client,message):
    from wikipedia import set_lang, summary
    set_lang('en')
    result = summary("".join(message.text.split()[1::]))
    message.reply(result)
    audio = gTTS(text=result , lang='en')
    audio.save("voice.ogg")
    app.send_audio(message.chat.id , "voice.ogg", caption="◤✧Function: #wikipedaia text to Voice◥\n◣✧Language:English Lang◢")
    os.remove(f"voice.ogg")
@app.on_message(filters.me & filters.regex(f'^(ویکی)'), group=14)
def wiki(client,message):
    from wikipedia import set_lang, summary
    set_lang('fa')
    result = summary("".join(message.text.split()[1::]))
    message.reply(result)
        
# |====================================| #

@app.on_message(
    filters.command("imdb") & filters.me, group=8
)
def imdb_query(client, message):  # sourcery no-metrics
    """To fetch imdb data about the given movie or series."""
    catmessage =  message.edit("❅__**Wait**__")
    try:
        movie_name = message.text.split("/imdb")[1]
        movies = imdb.search_movie(movie_name)
        movieid = movies[0].movieID
        movie = imdb.get_movie(movieid)
        moviekeys = list(movie.keys())
        for i in mov_titles:
            if i in moviekeys:
                mov_title = movie[i]
                break
        for j in reversed(mov_titles):
            if j in moviekeys:
                mov_ltitle = movie[j]
                break
        mov_runtime = movie["runtimes"][0] + " min" if "runtimes" in movie else ""
        if "original air date" in moviekeys:
            mov_airdate = movie["original air date"]
        elif "year" in moviekeys:
            mov_airdate = movie["year"]
        else:
            mov_airdate = ""
        mov_genres = ", ".join(movie["genres"]) if "genres" in moviekeys else "Not Data"
        mov_rating = str(movie["rating"]) if "rating" in moviekeys else "Not Data"
        mov_rating += (
            " (by " + str(movie["votes"]) + ")"
            if "votes" in moviekeys and "rating" in moviekeys
            else ""
        )
        mov_countries = (
            ", ".join(movie["countries"]) if "countries" in moviekeys else "Not Data"
        )
        mov_languages = (
            ", ".join(movie["languages"]) if "languages" in moviekeys else "Not Data"
        )
        mov_plot = (
            str(movie["plot outline"]) if "plot outline" in moviekeys else "Not Data"
        )
        mov_director =  get_cast("director", movie)
        mov_composers =  get_cast("composers", movie)
        mov_writer =  get_cast("writer", movie)
        mov_cast =  get_cast("cast", movie)
        mov_box =  get_moviecollections(movie)
        resulttext = f"""
<b>❅<i>Title : </i></b><code>{mov_title}</code>
<b>❅<i>Imdb Url : </i></b><a href='https://www.imdb.com/title/tt{movieid}'>{mov_ltitle}</a>
<b>❅<i>Info : </i></b><code>{mov_runtime} | {mov_airdate}</code>
<b>❅<i>Genres : </i></b><code>{mov_genres}</code>
<b>❅<i>Rating : </i></b><code>{mov_rating}</code>
<b>❅<i>Country : </i></b><code>{mov_countries}</code>
<b>❅<i>Language : </i></b><code>{mov_languages}</code>
<b>❅<i>Director : </i></b><code>{mov_director}</code>
<b>❅<i>Music Director </i>: </b><code>{mov_composers}</code>
<b>❅<i>Writer : </i></b><code>{mov_writer}</code>
<b><i>❅Stars : </i></b><code>{mov_cast}</code>
<b>❅<i>Box Office : </i></b>{mov_box}
<b>❅<i>Story Outline : </i></b><i>{mov_plot}</i>"""
        if "full-size cover url" in moviekeys:
            imageurl = movie["full-size cover url"]
        else:
            imageurl = None
        soup = BeautifulSoup(resulttext, features="html.parser")
        rtext = soup.get_text()
        if len(rtext) > 1024:
            extralimit = len(rtext) - 1024
            climit = len(resulttext) - extralimit - 20
            resulttext = resulttext[:climit] + "...........</i>"
        if imageurl:
            downloader = SmartDL(imageurl, moviepath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        if os.path.exists(moviepath):
            app.send_photo(
                message.chat.id,
                moviepath,
                caption=resulttext,
            )
            os.remove(moviepath)
            return  catmessage.delete()
            catmessage.edit(
            resulttext,
            link_preview=False,
        )
    except IndexError:
         catmessage.edit(f"__**❅This Movie Not Found{movie_name}.**__")
    except Exception as e:
         catmessage.edit(f"__**❅Error:**__\n__{e}__")

# |====================================| #

# handlerها برای فعال/غیرفعال کردن و تنظیم فونت (این رو در بخش @app.on_messageها، مثلا بعد از .fontname پیست کنید)
@app.on_message(filters.me & filters.regex(f'^(.timename)'), group=88)  # با prefix . هماهنگ کردم
def timename_handler(app, m: Message):
    json_database = json_read("data.json")
    if m.text.split()[1] == "on":
        json_database.update({"timename": "on"})
        write("data.json", json.dumps(json_database))
        m.edit_text(f"❖ TimeName Mode is **ON**")
    elif m.text.split()[1] == "off":
        json_database.update({"timename": "off"})
        write("data.json", json.dumps(json_database))
        m.edit_text(f"❖ TimeName Mode is **OFF**")

@app.on_message(filters.me & filters.regex(f'^(.setfont)'), group=89)  # با prefix .setfont
def setfont_handler(app, m: Message):
    json_database = json_read("data.json")
    try:
        font_choice = m.text.split()[1].capitalize()  # مثلا .setfont 1 -> Font1
        if font_choice == "1":
            json_database.update({"font": "Font1"})
            m.edit_text(f"❖ Font1 is Set")
        elif font_choice == "2":
            json_database.update({"font": "Font2"})
            m.edit_text(f"❖ Font2 is Set")
        elif font_choice == "3":
            json_database.update({"font": "Font3"})
            m.edit_text(f"❖ Font3 is Set")
        elif font_choice == "4":
            json_database.update({"font": "Font4"})
            m.edit_text(f"❖ Font4 is Set")
        elif font_choice == "5":
            json_database.update({"font": "Font5"})
            m.edit_text(f"❖ Font5 is Set")
        elif font_choice == "6":
            json_database.update({"font": "Font6"})
            m.edit_text(f"❖ Font6 is Set")
        elif font_choice == "7":
            json_database.update({"font": "Font7"})
            m.edit_text(f"❖ Font7 is Set")
        elif font_choice == "8":
            json_database.update({"font": "Font8"})
            m.edit_text(f"❖ Font8 is Set")
        elif font_choice == "9":
            json_database.update({"font": "Font9"})
            m.edit_text(f"❖ Font9 is Set")
        elif font_choice == "10":
            json_database.update({"font": "Font10"})
            m.edit_text(f"❖ Font10 is Set")
        elif font_choice == "11":
            json_database.update({"font": "Font11"})
            m.edit_text(f"❖ Font11 is Set")
        elif font_choice == "12":
            json_database.update({"font": "Font12"})
            m.edit_text(f"❖ Font12 is Set")
        elif font_choice == "13":
            json_database.update({"font": "Font13"})
            m.edit_text(f"❖ Font13 is Set")
        elif font_choice == "14":
            json_database.update({"font": "Font14"})
            m.edit_text(f"❖ Font14 is Set")
        elif font_choice == "15":
            json_database.update({"font": "Font15"})
            m.edit_text(f"❖ Font15 is Set")
        elif font_choice == "16":
            json_database.update({"font": "Font16"})
            m.edit_text(f"❖ Font16 is Set")
        elif font_choice == "17":
            json_database.update({"font": "Font17"})
            m.edit_text(f"❖ Font17 is Set")
        elif font_choice == "18":
            json_database.update({"font": "Font18"})
            m.edit_text(f"❖ Font18 is Set")
        elif font_choice == "Random":
            json_database.update({"font": "Random"})
            m.edit_text(f"❖ Random Font is Set")
        else:
            m.edit_text(f"❖ Invalid Font. Use 1-18 or Random")
        write("data.json", json.dumps(json_database))
    except:
        m.edit_text(f"❖ Error setting font")

# |====================================| #

@app.on_message(filters.me & filters.text , group=337)
async def signature_handler(app, m: Message):
    try:
        json_database = json_read("data.json")
        
        if json_database.get("signature", "off") != "on":
            return
        
        signature_text = json_database.get("signature_text", "")
        if not signature_text:
            return
        
        if hasattr(m, '_signature_added') and m._signature_added:
            return
        
        original_text = m.text
        
        if not original_text.endswith(f" {signature_text}"):
            new_text = f"{original_text}\n\n{signature_text}"
            
            try:
                await app.edit_message_text(
                    chat_id=m.chat.id,
                    message_id=m.id,
                    text=new_text
                )
                m._signature_added = True
            except Exception as e:
                print(f"Error editing message for signature: {e}")
                
    except Exception as e:
        print(f"Error in signature handler: {e}")


@app.on_message(filters.text,group=6)
def autoanwer(app, m:Message):
  text = m.text 
  a = json_read("data.json")
  if a["autoan"] == "on":
   if text in answer:
    num = answer.index(text)
    app.send_message(m.chat.id , javab[num], reply_to_message_id=m.id)
    sleep(9)
    num = 0

# |====================================| #

# PV Silent
@app.on_message(filters.command("pv_silent", prefixes=".") & filters.me)
async def pv_silent(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.pv_silent on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"pv_silent": "on"})
        await message.edit_text("PV Silent **ON**")
    elif status == "off":
        json_database.update({"pv_silent": "off"})
        await message.edit_text("PV Silent **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل متن
@app.on_message(filters.command("lock_text", prefixes=".") & filters.me)
async def lock_text(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_text on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_text": "on"})
        await message.edit_text("Lock Text **ON**")
    elif status == "off":
        json_database.update({"lock_text": "off"})
        await message.edit_text("Lock Text **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل فوروارد
@app.on_message(filters.command("lock_forward", prefixes=".") & filters.me)
async def lock_forward(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_forward on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_forward": "on"})
        await message.edit_text("Lock Forward **ON**")
    elif status == "off":
        json_database.update({"lock_forward": "off"})
        await message.edit_text("Lock Forward **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل لوکیشن
@app.on_message(filters.command("lock_location", prefixes=".") & filters.me)
async def lock_location(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_location on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_location": "on"})
        await message.edit_text("Lock Location **ON**")
    elif status == "off":
        json_database.update({"lock_location": "off"})
        await message.edit_text("Lock Location **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل انگلیسی
@app.on_message(filters.command("lock_english", prefixes=".") & filters.me)
async def lock_english(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_english on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_english": "on"})
        await message.edit_text("Lock English **ON**")
    elif status == "off":
        json_database.update({"lock_english": "off"})
        await message.edit_text("Lock English **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل فارسی
@app.on_message(filters.command("lock_persian", prefixes=".") & filters.me)
async def lock_persian(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_persian on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_persian": "on"})
        await message.edit_text("Lock Persian **ON**")
    elif status == "off":
        json_database.update({"lock_persian": "off"})
        await message.edit_text("Lock Persian **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل عکس
@app.on_message(filters.command("lock_photo", prefixes=".") & filters.me)
async def lock_photo(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_photo on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_photo": "on"})
        await message.edit_text("Lock Photo **ON**")
    elif status == "off":
        json_database.update({"lock_photo": "off"})
        await message.edit_text("Lock Photo **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل ایموجی پرمیوم
@app.on_message(filters.command("lock_premium_emoji", prefixes=".") & filters.me)
async def lock_premium_emoji(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_premium_emoji on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_premium_emoji": "on"})
        await message.edit_text("Lock Premium Emoji **ON**")
    elif status == "off":
        json_database.update({"lock_premium_emoji": "off"})
        await message.edit_text("Lock Premium Emoji **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل گیف
@app.on_message(filters.command("lock_gif", prefixes=".") & filters.me)
async def lock_gif(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_gif on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_gif": "on"})
        await message.edit_text("Lock GIF **ON**")
    elif status == "off":
        json_database.update({"lock_gif": "off"})
        await message.edit_text("Lock GIF **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل استیکر
@app.on_message(filters.command("lock_sticker", prefixes=".") & filters.me)
async def lock_sticker(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_sticker on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_sticker": "on"})
        await message.edit_text("Lock Sticker **ON**")
    elif status == "off":
        json_database.update({"lock_sticker": "off"})
        await message.edit_text("Lock Sticker **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل ویدیو سلفی
@app.on_message(filters.command("lock_video_note", prefixes=".") & filters.me)
async def lock_video_note(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_video_note on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_video_note": "on"})
        await message.edit_text("Lock Video Note **ON**")
    elif status == "off":
        json_database.update({"lock_video_note": "off"})
        await message.edit_text("Lock Video Note **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل ویدیو
@app.on_message(filters.command("lock_video", prefixes=".") & filters.me)
async def lock_video(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_video on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_video": "on"})
        await message.edit_text("Lock Video **ON**")
    elif status == "off":
        json_database.update({"lock_video": "off"})
        await message.edit_text("Lock Video **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل ویس
@app.on_message(filters.command("lock_voice", prefixes=".") & filters.me)
async def lock_voice(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_voice on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_voice": "on"})
        await message.edit_text("Lock Voice **ON**")
    elif status == "off":
        json_database.update({"lock_voice": "off"})
        await message.edit_text("Lock Voice **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل آهنگ
@app.on_message(filters.command("lock_audio", prefixes=".") & filters.me)
async def lock_audio(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_audio on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_audio": "on"})
        await message.edit_text("Lock Audio **ON**")
    elif status == "off":
        json_database.update({"lock_audio": "off"})
        await message.edit_text("Lock Audio **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل مخاطب
@app.on_message(filters.command("lock_contact", prefixes=".") & filters.me)
async def lock_contact(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_contact on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_contact": "on"})
        await message.edit_text("Lock Contact **ON**")
    elif status == "off":
        json_database.update({"lock_contact": "off"})
        await message.edit_text("Lock Contact **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل نظرسنجی / دکمه شیشه‌ای
@app.on_message(filters.command("lock_poll", prefixes=".") & filters.me)
async def lock_poll(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_poll on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_poll": "on"})
        await message.edit_text("Lock Poll/Button **ON**")
    elif status == "off":
        json_database.update({"lock_poll": "off"})
        await message.edit_text("Lock Poll/Button **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل نام کاربری
@app.on_message(filters.command("lock_username", prefixes=".") & filters.me)
async def lock_username(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_username on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_username": "on"})
        await message.edit_text("Lock @Username **ON**")
    elif status == "off":
        json_database.update({"lock_username": "off"})
        await message.edit_text("Lock @Username **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل منشن
@app.on_message(filters.command("lock_mention", prefixes=".") & filters.me)
async def lock_mention(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_mention on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_mention": "on"})
        await message.edit_text("Lock Mention **ON**")
    elif status == "off":
        json_database.update({"lock_mention": "off"})
        await message.edit_text("Lock Mention **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))

# قفل لینک
@app.on_message(filters.command("lock_link", prefixes=".") & filters.me)
async def lock_link(client, message):
    if len(message.command) < 2:
        await message.edit_text("❋ استفاده: `.lock_link on/off`")
        return
    
    status = message.command[1].lower()
    if status == "on":
        json_database.update({"lock_link": "on"})
        await message.edit_text("Lock Link **ON**")
    elif status == "off":
        json_database.update({"lock_link": "off"})
        await message.edit_text("Lock Link **OFF**")
    else:
        await message.edit_text("❋ فقط `on` یا `off`")
    
    write("data.json", json.dumps(json_database))
		
@app.on_message(filters.me | users & filters.text , group=336)
def updates(app, m:Message):
 global api
 global enemy
 global love
 global mutey
 global lang
 global now
 text = m.text 

# |====================================| #

 json_database = json_read("data.json")
 if (json_database["boldmode"] == "on"):
  m.edit_text(f"**{text}**")
 elif (json_database["italicmode"] == "on"):
  m.edit_text(f"__{text}__")
 elif (json_database["codemode"] == "on"):
  m.edit_text(f"`{text}`")
 elif (json_database["underline"] == "on"):
  m.edit_text(f"<u>{text}</u>")
 elif (json_database["emojimode"] == "on"):
  m.edit_text(f"{text} {choice(ez_emoji)}")
 elif (json_database["strike"] == "on"):
  m.edit_text(f"~~{text}~~")
 elif (json_database["spoilermode"] == "on"):
  m.edit_text(f"||{text}||")
 elif (json_database["quotemode"] == "on"):
  m.edit_text(f"```{text}```")
 elif (json_database["mention"] == "on"):
  m.edit_text(f"<a href=tg://user?id={m.from_user.id}>{text}</a>")

# |====================================| #

import re
from pyrogram.types import ChatPermissions

# ==================== PV Lock ====================
@app.on_message(filters.regex(r"^\.pvlock (on|off)$"))
async def pvlock_handler(client, message):
    text = message.text
    if text.split()[1] == "on":
        json_database.update({"pvlock": "on"})
        write("data.json", json.dumps(json_database))
        await message.edit_text("❋ Pv Lock is **ON**")
    elif text.split()[1] == "off":
        json_database.update({"pvlock": "off"})
        write("data.json", json.dumps(json_database))
        await message.edit_text("❋ Pv Lock is **OFF**")

# ==================== Clone ====================
@app.on_message(filters.regex(r"^\.clone"))
async def clone_handler(client, message):
    try:
        if message.reply_to_message:
            userSelfp = message.reply_to_message.from_user.id
            b = await client.invoke(functions.users.GetFullUser(id=await client.resolve_peer(userSelfp)))
            kiri = await client.get_users(message.reply_to_message.from_user.id)
            user_id_get = message.reply_to_message.from_user.id
        else:
            text = message.text.replace(" ", "").replace(".clone", "")
            user_id_get = (await client.get_users(text)).id
            kiri = await client.get_users(user_id_get)
            b = await client.invoke(functions.users.GetFullUser(id=await client.resolve_peer(user_id_get)))
        
        await message.edit_text(f"""
    **Cloner**
❖ `Firstname`⤳ (`{b.users[0].first_name if b.users[0].first_name else '--'}`)
❖ `Lastname`⤳ (`{(b.users[0].last_name if b.users[0].last_name else '--')}`)
❖ `Bio`⤳ (`{(b.full_user.about if b.full_user.about else '--')}`)""")
        
        loudo = await client.download_media(kiri.photo.big_file_id)
        await client.set_profile_photo(photo=loudo)
        await client.update_profile(first_name=b.users[0].first_name)
        await client.update_profile(last_name=(b.users[0].last_name if b.users[0].last_name else ""))
        await client.update_profile(bio=(b.full_user.about if b.full_user.about else ""))
        await message.edit_text("❖ Clone Successfully Completed")
        os.remove(loudo)
    except errors.exceptions.bad_request_400.UsernameNotOccupied: 
        await client.send_message(message.chat.id, "❖ Username Not Valid ❖") 
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Block ====================
@app.on_message(filters.regex(r"^\.block"))
async def block_handler(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            mention = message.reply_to_message.from_user.mention
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            mention = f'<a href=tg://user?id={user.id}>{user.first_name}</a>'
        
        await client.block_user(user_id)
        await message.edit_text(f"❖ {mention} Blocked")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Unblock ====================
@app.on_message(filters.regex(r"^\.unblock"))
async def unblock_handler(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            mention = message.reply_to_message.from_user.mention
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            mention = f'<a href=tg://user?id={user.id}>{user.first_name}</a>'
        
        await client.unblock_user(user_id)
        await message.edit_text(f"❖ {mention} Unblocked")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Left ====================
@app.on_message(filters.regex(r"^\.left"))
async def left_handler(client, message):
    try:
        if len(message.text.split()) > 1:
            chat_id = message.text.split()[1]
            await client.leave_chat(chat_id, delete=True)
            await message.edit_text(f"❖ Successfully Left From [ `{chat_id}` ]")
        else:
            await client.send_message(message.chat.id, "Bye :)") 
            await client.leave_chat(message.chat.id, delete=True)
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Join ====================
@app.on_message(filters.regex(r"^\.join "))
async def join_handler(client, message):
    try:
        link = message.text.replace(".join ", "").replace('+', 'joinchat/')
        await client.join_chat(link)
        await client.send_message(message.chat.id, f'❖ Successfully Joined To [ {link} ]', disable_web_page_preview=True)
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Ban ====================
@app.on_message(filters.regex(r"^\.ban"))
async def ban_handler(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            mention = message.reply_to_message.from_user.mention
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            mention = f'<a href=tg://user?id={user.id}>{user.first_name}</a>'
        
        await client.ban_chat_member(message.chat.id, user_id)
        await client.send_message(message.chat.id, f"❖ User {mention} Successfully Banned !")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Unban ====================
@app.on_message(filters.regex(r"^\.unban"))
async def unban_handler(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            mention = message.reply_to_message.from_user.mention
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            mention = f'<a href=tg://user?id={user.id}>{user.first_name}</a>'
        
        await client.unban_chat_member(message.chat.id, user_id)
        await client.send_message(message.chat.id, f"❖ User {mention} Successfully UnBanned !")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Clear Members ====================
@app.on_message(filters.regex(r"^(\.clear_member|پاکسازی ممبر)"))
async def clear_member_handler(client, message):
    try:
        target = message.text.split()[1]
        await message.edit_text(f"❖ Target Chat: `{target}`\n__Start Ban members__ . . .")
        
        async for member in client.get_chat_members(target):
            try:
                await client.ban_chat_member(target, member.user.id)
            except errors.FloodWait as e:
                await client.send_message("me", f"❖ Wait For {e.x} Seconds")
                await asyncio.sleep(e.x)
                await client.send_message("me", f"❖ **Flood Wait Has Ended**🥳\nSend [ `.clear_member {target}` ] Again")
            except errors.exceptions.bad_request_400.UserAdminInvalid:
                await client.send_message("me", f"**❖ You Are Not Admin in** ( `{target}` )")
            except errors.exceptions.bad_request_400.BadRequest:
                await client.send_message("me", f"**❖ Clear Members of ( {target} ) Has Been Ended**")
            except Exception as er:
                await client.send_message("me", f"❖ **ERROR** :\n(`{er}`)")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Unmute ====================
@app.on_message(filters.regex(r"^(\.delmute|حذف سکوت)"))
async def delmute_handler(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            mention = message.reply_to_message.from_user.mention
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            mention = f'<a href=tg://user?id={user.id}>{user.first_name}</a>'
        
        await client.unban_chat_member(message.chat.id, user_id)
        await client.send_message(message.chat.id, f"❖ User {mention} Successfully UnMuted !")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Mute ====================
@app.on_message(filters.regex(r"^(\.setmute|تنظیم سکوت)"))
async def setmute_handler(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            mention = message.reply_to_message.from_user.mention
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            mention = f'<a href=tg://user?id={user.id}>{user.first_name}</a>'
        
        await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions())
        await client.send_message(message.chat.id, f"❖ User {mention} Muted")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Set Chat Photo ====================
@app.on_message(filters.regex(r"^(\.setchatphoto|تنظیم پروفایل گروه)"))
async def set_chat_photo_handler(client, message):
    try:
        if message.reply_to_message and (message.reply_to_message.photo or message.reply_to_message.video):
            if message.reply_to_message.photo:
                file_id = message.reply_to_message.photo.file_id
            else:
                file_id = message.reply_to_message.video.file_id
            
            await client.set_chat_photo(chat_id=message.chat.id, photo=file_id)
            await client.send_message(message.chat.id, "❖ Chat Photo Changed")
        else:
            await message.edit_text("❖ Please Reply To Photo or Video")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Set Profile ====================
@app.on_message(filters.regex(r"^(\.setprofile|تنظیم پروفایل)"))
async def set_profile_handler(client, message):
    try:
        if message.reply_to_message:
            down = await client.download_media(message.reply_to_message)
            if message.reply_to_message.photo:
                await client.set_profile_photo(photo=down)
                await client.send_message(message.chat.id, "❖ Your Profile Photo Changed")
            elif message.reply_to_message.video:
                await client.set_profile_photo(video=down)
                await client.send_message(message.chat.id, "❖ Your Profile Video Changed")
            os.remove(down)
        else:
            await client.send_message(message.chat.id, "❖ Please Reply To Message")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Delete Profile ====================
@app.on_message(filters.regex(r"^(\.delprofile|حذف پروفایل)"))
async def del_profile_handler(client, message):
    try:
        photos = client.get_chat_photos("me")
        photo = await photos.__anext__()
        await client.delete_profile_photos(photo.file_id)
        await client.send_message(message.chat.id, "❖ Your Profile photo Deleted")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Delete Chat Photo ====================
@app.on_message(filters.regex(r"^(\.delchatphoto|حذف پروفایل گروه)$"))
async def del_chat_photo_handler(client, message):
    try:
        await client.delete_chat_photo(message.chat.id)
        await message.reply("❖ Chat Photo Cleared")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Set Chat Title ====================
@app.on_message(filters.regex(r"^\.setchattitle"))
async def set_chat_title_handler(client, message):
    try:
        kx = message.text.replace(".setchattitle", "").strip()
        await client.set_chat_title(message.chat.id, kx)
        await message.reply(f"❖ Chat Name changed To[ `{kx}` ]")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

@app.on_message(filters.regex(r"^تنظیم نام گروه"))
async def set_chat_title_fa_handler(client, message):
    try:
        kx = message.text.replace("تنظیم نام گروه", "").strip()
        await client.set_chat_title(message.chat.id, kx)
        await message.reply(f"❖ Chat Name changed To[ `{kx}` ]")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Set Chat Bio ====================
@app.on_message(filters.regex(r"^\.setchatbio"))
async def set_chat_bio_handler(client, message):
    try:
        kx = message.text.replace(".setchatbio", "").strip()
        await client.set_chat_description(message.chat.id, kx)
        await message.reply(f"❖ Chat Bio changed To [ `{kx}` ]")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

@app.on_message(filters.regex(r"^تنظیم بیو گروه"))
async def set_chat_bio_fa_handler(client, message):
    try:
        kx = message.text.replace("تنظیم بیو گروه", "").strip()
        await client.set_chat_description(message.chat.id, kx)
        await message.reply(f"❖ Chat Bio changed To [ `{kx}` ]")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Pin ====================
@app.on_message(filters.regex(r"^(\.pin|پین)$"))
async def pin_handler(client, message):
    if message.reply_to_message:
        try:
            await message.reply_to_message.pin(disable_notification=False)
            await message.edit_text('❖ Pinned')
        except Exception as er:
            await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")
    else:
        await message.edit_text("❖ Please Reply To Message")

# ==================== Unpin ====================
@app.on_message(filters.regex(r"^(\.unpin|حذف پین)$"))
async def unpin_handler(client, message):
    try:
        if message.reply_to_message:
            await client.unpin_chat_message(message.chat.id, message.reply_to_message.id)
            await message.edit_text("❖ Unpinned")
        else:
            await message.edit_text("❖ Please Reply To Message")
    except Exception as e:
        await message.edit_text(f"❖ ERROR: {e}")

# ==================== Unpin All ====================
@app.on_message(filters.regex(r"^(\.unpinall|حذف همه پین)$"))
async def unpin_all_handler(client, message):
    try:
        await client.unpin_all_chat_messages(message.chat.id)
        await message.edit_text('❖ All Message Unpinned')
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Set Chat Username ====================
@app.on_message(filters.regex(r"^(\.setchatusername|تنظیم یوزرنیم گروه)"))
async def set_chat_username_handler(client, message):
    try:
        kx = message.text.split()[1]
        await client.set_chat_username(message.chat.id, kx)
        await message.edit_text(f'❖ Chat Username Changed [ `{kx}` ]')
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Create Channel ====================
@app.on_message(filters.regex(r"^(\.creatchannel|ساخت کانال)"))
async def create_channel_handler(client, message):
    try:
        kx = message.text.split()[1]
        await client.create_channel(title=f'{kx}')
        await message.edit_text(f'❖ Channel [ `{kx}` ] Created')
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Create Supergroup ====================
@app.on_message(filters.regex(r"^(\.creatsupergroup|ساخت گروه)"))
async def create_supergroup_handler(client, message):
    try:
        kx = message.text.split()[1]
        await client.create_supergroup(title=f'{kx}')
        await message.edit_text(f'❖ Supergroup [ `{kx}` ] Created')
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Create Group ====================
@app.on_message(filters.regex(r"^\.creatgroup"))
async def create_group_handler(client, message):
    try:
        kx = message.text.split()[1]
        await client.create_group(title=f'{kx}')
        await message.edit_text(f'❖ Group [ `{kx}` ] Created')
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Set Name ====================
@app.on_message(filters.regex(r"^\.setname"))
async def set_name_handler(client, message):
    try:
        kx = message.text.replace(".setname", "").strip()
        await client.invoke(functions.account.UpdateProfile(first_name=kx))
        write("user.txt", kx)
        await message.edit_text(f'❖ Your Name is Updated To [ `{kx}` ]')
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Set Last Name ====================
@app.on_message(filters.regex(r"^\.setlastname"))
async def set_last_name_handler(client, message):
    try:
        kx = message.text.replace(".setlastname", "").strip()
        await client.invoke(functions.account.UpdateProfile(last_name=kx))
        await message.edit_text(f'❖ Your Lastname is Updated To [ `{kx}` ]')
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Set Bio ====================
@app.on_message(filters.regex(r"^\.setbio"))
async def set_bio_handler(client, message):
    try:
        kx = message.text.replace(".setbio", "").strip()
        await client.invoke(functions.account.UpdateProfile(about=kx))
        write("userbio.txt", kx)
        await message.edit_text(f'❖ Your Bio Updated To⤳[ `{kx}` ]')
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Get IP ====================
@app.on_message(filters.regex(r"^\.getip"))
async def get_ip_handler(client, message):
    try:
        if message.reply_to_message:
            HOSTNAME = message.reply_to_message.text
        else:
            HOSTNAME = message.text.split()[1]
        
        ip_address = socket.gethostbyname(HOSTNAME)
        await message.edit_text(f'❖ The [`{HOSTNAME}`] iP address is [`{ip_address}`]')
    except:
        await message.edit_text(f'❖ The `{HOSTNAME}` Not valid !!')

# ==================== Mention ====================
@app.on_message(filters.regex(r"^\.mention"))
async def mention_handler(client, message):
    try:
        if message.reply_to_message:
            await message.edit_text(f"{message.reply_to_message.from_user.mention}")
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            await message.edit_text(f"<a href=tg://user?id={user.id}>{user.first_name}</a>")
    except:
        await message.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

# ==================== Download ====================
@app.on_message(filters.regex(r"^\.dl$"))
async def download_handler(client, message):
    try:
        if message.reply_to_message:
            down = await client.download_media(message.reply_to_message)
            caption = message.reply_to_message.caption if message.reply_to_message.caption else ""
            await client.send_document(message.chat.id, down, caption=caption)
            os.remove(down)
        else:
            await message.edit_text("❖ Please Reply To A Message")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Unzip ====================
@app.on_message(filters.regex(r"^\.unzip$"))
async def unzip_handler(client, message):
    try:
        if message.reply_to_message and message.reply_to_message.document:
            file_name = await message.reply_to_message.download()
            edited = await client.send_message(message.chat.id, "file : \n downloads->")
            await asyncio.sleep(1)
            await edited.edit_text('file : \n downloads->extractfiles->')
            
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall('templ')
            
            count = 0
            for root, dirs, files in os.walk('templ'):
                for name in files:
                    filename = os.path.join(root, name)
                    count += 1
                    if os.path.getsize(filename) == 0:
                        os.remove(filename)
                        continue
                    await client.send_document(message.chat.id, filename, caption=f"file {count} in zip")
                    os.remove(filename)
            
            await edited.edit_text('file : \n downloads->extractfiles->exracted->uploading->uploaded')
            
            for name in dirs:
                dirname = os.path.join(root, name)
                if not os.listdir(dirname):
                    os.rmdir(dirname)
                    
            os.remove(file_name)
        else:
            await message.edit_text("❖ Please Reply To A Zip File")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Sticker to Photo ====================
@app.on_message(filters.regex(r"^\.tp$"))
async def sticker_to_photo_handler(client, message):
    try:
        if message.reply_to_message and message.reply_to_message.sticker:
            down = await client.download_media(message.reply_to_message)
            os.rename(down, 'sticker.jpg')
            await client.send_photo(message.chat.id, "sticker.jpg", caption="**Sticker** To **Picture** By __Jack_self__", reply_to_message_id=message.id)
            os.remove("sticker.jpg")
        else:
            await message.edit_text(f"**ERROR!**\n\n__Please Reply To A Sticker__")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Photo to Sticker ====================
@app.on_message(filters.regex(r"^\.ts$"))
async def photo_to_sticker_handler(client, message):
    try:
        if message.reply_to_message and message.reply_to_message.photo:
            down = await client.download_media(message.reply_to_message)
            os.rename(down, 'sticker.webp')
            await client.send_sticker(message.chat.id, "sticker.webp", reply_to_message_id=message.id)
            os.remove("sticker.webp")
        else:
            await message.edit_text(f"**ERROR!**\n\n__Please Reply To A Photo__")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Photo to GIF ====================
@app.on_message(filters.regex(r"^\.tg$"))
async def photo_to_gif_handler(client, message):
    try:
        if message.reply_to_message and message.reply_to_message.photo:
            down = await client.download_media(message.reply_to_message)
            os.rename(down, 'animation.gif')
            await client.send_animation(message.chat.id, "animation.gif", reply_to_message_id=message.id)
            os.remove("animation.gif")
        else:
            await message.edit_text(f"**ERROR!**\n\n__Please Reply To A Photo__")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Get Message ====================
@app.on_message(filters.regex(r"^\.get_message$"))
async def get_message_handler(client, message):
    if message.reply_to_message:
        await client.send_message(message.chat.id, str(message.reply_to_message), reply_to_message_id=message.id)
    else:
        await client.send_message(message.chat.id, str(message), reply_to_message_id=message.id)

# ==================== Time ====================
@app.on_message(filters.regex(r"^\.time$"))
async def time_handler(client, message):
    try:
        for i in range(0, 10):
            kir = datetime.now(pytz.timezone("Asia/Tehran")).strftime("%H:%M:%S")
            await message.edit_text(f"**Time:** `{kir}`")
            await asyncio.sleep(1)
    except Exception as er:
        await message.edit_text(str(er))

# ==================== Set Time Photo ====================
@app.on_message(filters.regex(r"^\.photo_send_time$"))
async def photo_send_time_handler(client, message):
    if message.reply_to_message and message.reply_to_message.photo:
        file_id = message.reply_to_message.photo.file_id
        write("send_time_photo.txt", file_id)
        await message.edit_text(f"❖ The Photo Of [ `.photo_time` ]👇\n\nFile id: {file_id}")
    else:
        await message.edit_text(f"**❖ Please reply to a photo**")

# ==================== Ping ====================
@app.on_message(filters.regex(r"^\.ping$"))
async def ping_handler(client, message):
    try:
        up_a = strftime('%H:%M:%S', gmtime(uptime()))
        svmem = psutil.virtual_memory()
        await message.edit_text(f"""
    **Jack_Self Status**
    
❖ `User` ⤳ ( `{client.me.first_name}` )
❖ `Uptime` ⤳ (`{up_a}`)
❖ `Ram Usage` ⤳ (`{get_size(svmem.used)}`)
❖ `Python Version` ⤳ (`{platform.python_version()}`)
❖ `Source Version` ⤳ (`{Src_vrsion}`) 
❖ `Library` ⤳ (`Pyrogram`)""")
    except Exception as er:
        await message.edit_text(str(er))

# ==================== CPU Info ====================
@app.on_message(filters.regex(r"^\.cpu$"))
async def cpu_handler(client, message):
    try:
        cpufreq = psutil.cpu_freq()
        await message.edit_text(f"""
❖ `Physical Cores` ⤳  (`{psutil.cpu_count(logical=False)}`)
❖ `Total Cores` ⤳  (`{psutil.cpu_count(logical=True)}`)
❖ `Max Frequency` ⤳  (`{cpufreq.max:.2f}Mhz`)
❖ `Min Frequency` ⤳  (`{cpufreq.min:.2f}Mhz`)
❖ `Current Frequency` ⤳  (`{cpufreq.current:.2f}Mhz`)
❖ `CPU Usage` ⤳  (`{psutil.cpu_percent()}%`)""")
    except Exception as er:
        await message.edit_text(str(er))

# ==================== Memory Info ====================
@app.on_message(filters.regex(r"^\.memory$"))
async def memory_handler(client, message):
    try:
        svmem = psutil.virtual_memory()
        await message.edit_text(f"""
❖ `Total` ⤳ (`{get_size(svmem.total)}`)
❖ `Available` ⤳ (`{get_size(svmem.available)}`)
❖ `Used` ⤳ (`{get_size(svmem.used)}`)
❖ `Percentage` ⤳ (`{svmem.percent}%`)""")
    except Exception as er:
        await message.edit_text(str(er))

# ==================== Logo ====================
@app.on_message(filters.regex(r"^\.logo "))
async def logo_handler(client, message):
    try:
        text = message.text.replace('.logo ', '')
        # Assuming logo() function is defined elsewhere
        logo(text)
        await client.send_photo(message.chat.id, "logo.png", f"**لوگو شما آماده شد** \nلوگو درخواستی : `{text}`", reply_to_message_id=message.id)
        os.remove("logo.png")
    except Exception as er:
        await client.send_message(message.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=message.id)

# ==================== Logo2 ====================
@app.on_message(filters.regex(r"^\.logo2 "))
async def logo2_handler(client, message):
    try:
        text = message.text.replace('.logo2 ', '')
        # Assuming logo2() function is defined elsewhere
        logo2(text)
        await client.send_photo(message.chat.id, "logo.png", f"**لوگو شما آماده شد** \nلوگو درخواستی : `{text}`", reply_to_message_id=message.id)
        os.remove("logo.png")
    except Exception as er:
        await client.send_message(message.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=message.id)

# ==================== Remix Music ====================
@app.on_message(filters.regex(r"^\.remix "))
async def remix_handler(client, message):
    try:
        name = message.text.replace(".remix ", "")
        wait = await message.reply("Wait Please..")
        result = await client.get_inline_bot_results("vkmusic_bot", name)
        if result.results:
            audio_result = result.results[0]
            gett = await client.send_inline_bot_result("me", result.query_id, audio_result.id)
            music_msg = await client.get_messages("me", gett.updates[0].id)
            if music_msg.audio:
                file_path = await client.download_media(music_msg.audio)
                await wait.edit("**Downloaded**")
                await client.delete_messages("me", gett.updates[0].id)
                await message.reply_audio(file_path, caption=f"**Your Music is Ready!", performer="@Jack_self", title=f"{name}", thumb="cache/jack.jpg")
                os.remove(file_path)
            else:
                await wait.edit("No audio found.")
                await client.delete_messages("me", gett.updates[0].id)
        else:
            await wait.edit("No music found.")
        await wait.delete()
    except Exception as er:
        await client.send_message(message.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=message.id)

# ==================== Oqat ====================
@app.on_message(filters.regex(r"^\.oqat "))
async def oqat_handler(client, message):
    try:
        text = message.text.replace('.oqat ', '')
        url = f"https://api.codebazan.ir/owghat/?city={text}"
        response = requests.get(url)
        ms = response.json()
        image = ms["Result"]
        img = image[0]
        mm = json.dumps(img)
        mm1 = json.loads(mm)
        shahr = mm1["shahr"]
        tarikh = mm1["tarikh"]
        azansobh = mm1["azansobh"]
        toloaftab = mm1["toloaftab"]
        azanzohr = mm1["azanzohr"]
        ghorubaftab = mm1["ghorubaftab"]
        azanmaghreb = mm1["azanmaghreb"]
        nimeshab = mm1["nimeshab"]
        msg = f"اوغات شرعي شهر {shahr} عبارت است از \nتاريخ امروز : {tarikh} \nاذان صبح : {azansobh} \nطلوع آفتاب : {toloaftab} \nاذان ظهر : {azanzohr} \nغروب آفتاب : {ghorubaftab} \n اذان مغرب : {azanmaghreb} \nنيمه شب شرعي : {nimeshab} \nاحتياط دودقيقه اي بهتر است رعايت شود"
        await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)
    except Exception as er:
        await client.send_message(message.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=message.id)

# ==================== Password ====================
@app.on_message(filters.regex(r"^\.pass "))
async def pass_handler(client, message):
    try:
        text = message.text.replace('.pass ', '')
        url = f'http://api.codebazan.ir/password/?length={text}'
        response = requests.get(url)
        html_output = response.text
        msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __PASSWORD IS READY__ = **{html_output}** \n __Length__ = **{text}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
        await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)
    except Exception as er:
        await client.send_message(message.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=message.id)

# ==================== Morse Encode ====================
@app.on_message(filters.regex(r"^\.morset "))
async def morset_handler(client, message):
    try:
        text = message.text.replace('.morset ', '')
        url = f'http://api.codebazan.ir/mourse/?lang=en&text={text}'
        response = requests.get(url)
        html_output = response.text
        msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __Morset code__ = **{html_output}** \n __YOUR TEXT__ = **{text}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
        await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)
    except Exception as er:
        await client.send_message(message.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=message.id)

# ==================== Morse Decode ====================
@app.on_message(filters.regex(r"^\.unmorset "))
async def unmorset_handler(client, message):
    try:
        text = message.text.replace('.unmorset ', '')
        url = f'http://api.codebazan.ir/mourse/?lang=en&mourse={text}'
        response = requests.get(url)
        html_output = response.text
        msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __UNMorset code__ = **{html_output}** \n __YOUR Morset__ = **{text}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
        await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)
    except Exception as er:
        await client.send_message(message.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=message.id)

# ==================== Date ====================
@app.on_message(filters.regex(r"^(امروز|\.date)$"))
async def date_handler(client, message):
    try:
        url = f"https://api.codebazan.ir/owghat/?city=تهران"
        response = requests.get(url)
        ms = response.json()
        image = ms["Result"]
        img = image[0]
        mm = json.dumps(img)
        mm1 = json.loads(mm)
        tarikh = mm1["tarikh"]
        msg = f"تاريخ امروز : {tarikh}"
        await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)
    except Exception as er:
        await client.send_message(message.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=message.id)

# ==================== ID ====================
@app.on_message(filters.regex(r"^id$"))
async def id_handler(client, message):
    dd = "ايدي عددي شما : " + str(message.from_user.id)
    await client.send_message(message.chat.id, dd, reply_to_message_id=message.id)

# ==================== Bio ====================
@app.on_message(filters.regex(r"^(\.bio|bio)$"))
async def bio_handler(client, message):
    url = f'https://api.codebazan.ir/bio'
    response = requests.get(url)
    html_output = response.text
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)

# ==================== Memo ====================
@app.on_message(filters.regex(r"^(\.memo|خاطره)$"))
async def memo_handler(client, message):
    url = f'http://api.codebazan.ir/jok/khatere'
    response = requests.get(url)
    html_output = response.text
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)

# ==================== PNP ====================
@app.on_message(filters.regex(r"^(\.pnp|pnp)$"))
async def pnp_handler(client, message):
    url = f'http://api.codebazan.ir/jok/pa-na-pa/'
    response = requests.get(url)
    html_output = response.text
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)

# ==================== Alaki ====================
@app.on_message(filters.regex(r"^(\.alaki|الکی)$"))
async def alaki_handler(client, message):
    url = f'http://api.codebazan.ir/jok/alaki-masalan'
    response = requests.get(url)
    html_output = response.text
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)

# ==================== Dastan ====================
@app.on_message(filters.regex(r"^(\.dastan|داستان)$"))
async def dastan_handler(client, message):
    url = f'http://api.codebazan.ir/dastan/'
    response = requests.get(url)
    html_output = response.text
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)

# ==================== Dialog ====================
@app.on_message(filters.regex(r"^(\.dlg|دیالوگ)$"))
async def dlg_handler(client, message):
    url = f'http://api.codebazan.ir/dialog/'
    response = requests.get(url)
    html_output = response.text
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)

# ==================== Random Name ====================
@app.on_message(filters.regex(r"^(\.rname|اسم رندوم)$"))
async def rname_handler(client, message):
    url = f'https://api.codebazan.ir/name/?type=json'
    response = requests.get(url)
    html_output = response.text
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __Your Random Name__ = **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)

# ==================== Screenshot ====================
@app.on_message(filters.regex(r"^\.screenshot "))
async def screenshot_handler(client, message):
    text = message.text.replace(".screenshot ", "")
    url = requests.get(f"https://domain.com/shot/Sh.php?url=https://{text}").json()
    image_url = url["Link ScreenShot"]
    await client.send_photo(message.chat.id, image_url, caption=f"`{text}`", reply_to_message_id=message.id)

# ==================== Meli Code ====================
@app.on_message(filters.regex(r"^\.meli "))
async def meli_handler(client, message):
    text = message.text.replace('.meli ', '')
    url = f'https://api.codebazan.ir/codemelli/?code={text}'
    response = requests.get(url)
    html_output = response.text
    gpt = json.loads(html_output)
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{gpt}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nدرصورت valid بودن , کد ملی وارد شده صحیح میباشد."
    await client.send_message(message.chat.id, msg, reply_to_message_id=message.id)

# ==================== Melo Voice ====================
@app.on_message(filters.regex(r"^\.melo"))
async def melo_handler(client, message):
    try:
        text = message.text.replace('.melo ', '')
        wait = await message.reply("Wait Please..")
        result = await client.get_inline_bot_results("melobot", text)
        if result.results:
            voice_result = result.results[0]
            gett = await client.send_inline_bot_result("me", result.query_id, voice_result.id)
            image1 = await client.get_messages("me", gett.updates[0].id)
            if image1.voice:
                file_path = await client.download_media(image1.voice)
                await wait.edit("**Downloaded**")
                await client.delete_messages("me", gett.updates[0].id)
                await message.reply_voice(file_path)
                os.remove(file_path)
            else:
                await wait.edit("No voice found.")
                await client.delete_messages("me", gett.updates[0].id)
        else:
            await wait.edit("No voice found.")
        await wait.delete()
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Picture ====================
@app.on_message(filters.regex(r"^\.pic"))
async def pic_handler(client, message):
    try:
        text = message.text.replace('.pic ', '')
        wait = await message.reply("Wait Please..")
        result = await client.get_inline_bot_results("pic", text)
        if result.results:
            photo_result = result.results[0]
            gett = await client.send_inline_bot_result("me", result.query_id, photo_result.id)
            image1 = await client.get_messages("me", gett.updates[0].id)
            if image1.photo:
                file_path = await client.download_media(image1.photo)
                await wait.edit("**Downloaded**")
                await client.delete_messages("me", gett.updates[0].id)
                await message.reply_photo(file_path, caption=f"**{text}**")
                os.remove(file_path)
            else:
                await wait.edit("No Photo found.")
                await client.delete_messages("me", gett.updates[0].id)
        else:
            await wait.edit("No photo found.")
        await wait.delete()
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Like ====================
@app.on_message(filters.regex(r"^\.like"))
async def like_handler(client, message):
    try:
        text = message.text.replace('.like ', '')
        result = await client.get_inline_bot_results("like", text)
        await client.send_inline_bot_result(message.chat.id, result.query_id, result.results[0].id)
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Extract Text ====================
@app.on_message(filters.regex(r"^\.extext$"))
async def extext_handler(client, message):
    try:
        if message.reply_to_message and message.reply_to_message.photo:
            await message.edit_text("Wait For **8** Second . . .")
            await client.send_photo("@oneGooglebot", message.reply_to_message.photo.file_id, caption="")
            await asyncio.sleep(8)
            async for a in client.get_chat_history("@oneGooglebot", limit=1):
                text = a.text.replace("💭 OCR detected:", "")
                await message.edit_text("**OCR** __Detected Successfully :)__")
                await message.reply(f"**❖ OCR Result:**`{text}`", quote=True)
        else:
            await message.edit_text("**Please Reply to a Photo**")
    except Exception as er:
        await client.send_message(message.chat.id, f"❖ **ERROR** :\n(`{er}`)")

# ==================== File Info ====================
@app.on_message(filters.regex(r"^\.file_info$"))
async def file_info_handler(client, message):
    from decimal import Decimal, getcontext
    getcontext().prec = 3
    try:
        if message.reply_to_message:
            if message.reply_to_message.document:
                doc = message.reply_to_message.document
                await message.edit_text(f"""❖ Name ⤳ (`{doc.file_name}`)
❖ Type ⤳ (`{doc.mime_type}`)
❖ File Size ⤳ (`{Decimal(int(doc.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Date ⤳ (`{doc.date}`)
❖ File iD ⤳ (`{doc.file_id}`)""")
            elif message.reply_to_message.photo:
                photo = message.reply_to_message.photo
                await message.edit_text(f"""❖ Size ⤳ (`{photo.width}×{photo.height}`)
❖ File Size ⤳ (`{Decimal(int(photo.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Date ⤳ (`{photo.date}`)
❖ File iD ⤳ (`{photo.file_id}`)""")
            elif message.reply_to_message.video:
                video = message.reply_to_message.video
                await message.edit_text(f"""❖ Type ⤳ (`{video.mime_type}`)
❖ Size ⤳ (`{video.width}×{video.height}`)
❖ Duration ⤳ (`{video.duration}s`)
❖ File Size ⤳ (`{Decimal(int(video.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Date ⤳ (`{video.date}`)
❖ Support Streaming ⤳ (`{video.supports_streaming}`)
❖ File iD ⤳ (`{video.file_id}`)""")
            elif message.reply_to_message.animation:
                animation = message.reply_to_message.animation
                await message.edit_text(f"""❖ Size ⤳ (`{animation.width}×{animation.height}`)
❖ Type ⤳ (`{animation.mime_type}`)
❖ File Size ⤳ (`{Decimal(int(animation.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Duration ⤳ (`{animation.duration}s`)
❖ Date ⤳ (`{animation.date}`)
❖ File iD ⤳ (`{animation.file_id}`)""")
            elif message.reply_to_message.sticker:
                sticker = message.reply_to_message.sticker
                await message.edit_text(f"""❖ Size ⤳ (`{sticker.width}×{sticker.height}`)
❖ Name ⤳ (`{sticker.file_name}`)
❖ Type ⤳ (`{sticker.mime_type}`)
❖ File Size ⤳ (`{Decimal(int(sticker.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Emoji ⤳ (`{sticker.emoji}`)
❖ Is Animated ⤳ (`{sticker.is_animated}`)
❖ Is Video ⤳ (`{sticker.is_video}`)
❖ Sticker Set ⤳ (`{"https://t.me/addstickers/"+sticker.set_name if sticker.set_name else "--"}`)
❖ Date ⤳ (`{sticker.date}`)
❖ File iD ⤳ (`{sticker.file_id}`)""")
            elif message.reply_to_message.voice:
                voice = message.reply_to_message.voice
                await message.edit_text(f"""❖ Type ⤳ (`{voice.mime_type}`)
❖ File Size ⤳ (`{Decimal(int(voice.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Duration ⤳ (`{voice.duration}s`)
❖ Date ⤳ (`{voice.date}`)
❖ File iD ⤳ (`{voice.file_id}`)""")
            elif message.reply_to_message.audio:
                audio = message.reply_to_message.audio
                await message.edit_text(f"""❖ Title ⤳ (`{audio.title}`)
❖ Performer ⤳ (`{audio.performer}`)
❖ Type ⤳ (`{audio.mime_type}`)
❖ File Name ⤳ (`{audio.file_name}`)
❖ File Size ⤳ (`{Decimal(int(audio.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Duration ⤳ (`{audio.duration}s`)
❖ Date ⤳ (`{audio.date}`)
❖ File iD ⤳ (`{audio.file_id}`)""")
            else:
                await message.edit_text(f"**Please Reply To A Media/file**")
        else:
            await message.edit_text(f"**Please Reply To A Media/file**")
    except Exception as er:
        await message.edit_text(str(er))

# ==================== Admin List ====================
@app.on_message(filters.regex(r"^\.tadmin$"))
async def tadmin_handler(client, message):
    try:
        b = "❖ **Admins** :\n\n"
        c = 1
        k = 0
        async for i in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if not i.user.is_deleted:
                b += "├" + str(c) + " ↬ [" + (i.user.mention if i.user.id else "--") + "]\n"
                c += 1
            else:
                k += 1
        if k != 0:
            b += f"├ **Deleted Account Admin** : `{k}`\n└— **Count** : `{k + c - 1}`"
        else:
            b += f"└—  \n **Count** : `{k + c - 1}`"
        await message.reply(b)
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Game ====================
@app.on_message(filters.regex(r"^\.hehe$"))
async def hehe_handler(client, message):
    try:
        games = ["2048", "Flappy Bird", "Hextris"]
        jdkh = random.choice(games)
        await message.edit_text(f"**Game name:** `{jdkh}`")
        result = await client.get_inline_bot_results("awesomebot", jdkh)
        await client.send_inline_bot_result(message.chat.id, result.query_id, result.results[0].id)
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Instagram Download ====================
@app.on_message(filters.regex(r"^\.instadl"))
async def instadl_handler(client, message):
    await message.edit_text(f"**Wait**⤳Sending Request to Api . . .")
    s = ""
    i = 1
    try:
        req = requests.get(f"https://sidepath.ga/api/instagram.php?url={message.text.split()[1]}").json()["Results"]
        for res in req["post"]:
            if res is not None:
                await client.send_document(message.chat.id, res, caption=f"Slide Number {i}")
                i += 1
        await client.send_message(message.chat.id, f" **Successful** ")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Story Download ====================
@app.on_message(filters.regex(r"^\.story"))
async def story_handler(client, message):
    await message.edit_text(f"**Wait**⤳Sending Request to Api . . .")
    s = ""
    i = 1
    try:
        req = requests.get(f"https://sidepath.ga/api/story.php?url={message.text.split()[1]}").json()
        if req["ok"]:
            for res in req["Results"]["story"]:
                if res is not None:
                    await client.send_document(message.chat.id, res["downloadUrl"], caption=f"Story Number {i} of {message.text.split()[1]}")
                    i += 1
            await client.send_message(message.chat.id, f" **Successful** ")
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Pinterest Download ====================
@app.on_message(filters.regex(r"^\.pindl"))
async def pindl_handler(client, message):
    await message.edit_text(f"**Wait**⤳Sending Request to Api . . .")
    try:
        req = requests.get(f"https://api.otherapi.tk/pinterest?url={message.text.replace('.pindl', '')[1::]}").json()["pinterest"]
        if "image" in req:
            await client.send_photo(message.chat.id, req["image"], caption=f"__Image__ Downloaded From **Pinterest**", reply_to_message_id=message.id)
        elif "video" in req:
            await client.send_video(message.chat.id, req["video"], caption=f"__Video__ Downloaded From **Pinterest**", reply_to_message_id=message.id)
    except Exception as er:
        await message.edit_text(f"❖ **ERROR** :\n(`{er}`)")

# ==================== Mute User ====================
@app.on_message(filters.regex(r"^\.mute"))
async def mute_handler(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            mention = message.reply_to_message.from_user.mention
            if user_id not in mutey:
                if user_id != client.me.id:
                    mutey.append(user_id)
                    await message.edit_text(f'❖ {mention} Added To Mute List')
                else:
                    await message.edit_text("❖ Cannot mute yourself")
            else:
                await message.edit_text(f'**⌯⌲ This User {mention} Already in mute List**')
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            mention = f'<a href=tg://user?id={user.id}>{user.first_name}</a>'
            if user.id not in mutey:
                if user.id != client.me.id:
                    mutey.append(user.id)
                    await message.edit_text(f'**⌯⌲ {mention} Added To Mute List**')
                else:
                    await message.edit_text("❖ Cannot mute yourself")
            else:
                await message.edit_text(f'**⌯⌲ This User {mention} Already in Mute List**')
    except Exception as er:
        await message.edit_text(f" | 𝐄𝐑𝐑𝐎𝐑!")

# ==================== Unmute User ====================
@app.on_message(filters.regex(r"^حذف سکوت"))
async def unmute_handler(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            mention = message.reply_to_message.from_user.mention
            if user_id in mutey:
                mutey.remove(user_id)
                await message.edit_text(f'**✔️ کاربر {mention} از لیست سکوت حذف شد!**')
            else:
                await message.edit_text(f'**(⚠️) کاربر {mention} در لیست سکوت نبوده است!**')
        else:
            user_id = message.text.split()[1]
            user = await client.get_users(user_id)
            mention = f'<a href=tg://user?id={user.id}>{user.first_name}</a>'
            if user.id in mutey:
                mutey.remove(user.id)
                await message.edit_text(f'**✔️ کاربر {mention} از لیست سکوت حذف شد!**')
            else:
                await message.edit_text(f'**(⚠️) کاربر {mention} در لیست سکوت نبوده است!**')
    except Exception as er:
        await message.edit_text(f"**(⚠️) خطای نامشخص!")

# ==================== Clear Enemy List ====================
@app.on_message(filters.regex(r"^حذف لیست دشمن$"))
async def clear_enemy_handler(client, message):
    een = ""
    t_een = 1
    if len(enemy) >= 1:
        for user in enemy:
            user_obj = await client.get_users(user)
            een += f"{t_een} - <a href=tg://user?id={user}>{user_obj.first_name}</a>\n"
            t_een += 1
        await message.edit_text(f"**✔️ لیست دشمن پاکسازی شد!**\n{een}")
        enemy.clear()
    else:
        await message.edit_text(f"**(⚠️) لیست دشمن خالی است!**")

# ==================== Clear Friend List ====================
@app.on_message(filters.regex(r"^حذف لیست دوست$"))
async def clear_friend_handler(client, message):
    een = ""
    t_een = 1
    if len(love) >= 1:
        for user in love:
            user_obj = await client.get_users(user)
            een += f"{t_een} - <a href=tg://user?id={user}>{user_obj.first_name}</a>\n"
            t_een += 1
        await message.edit_text(f"**✔️ لیست دوست پاکسازی شد!**\n{een}")
        love.clear()
    else:
        await message.edit_text(f"**(⚠️) لیست دوست خالی است!**")

# ==================== Clear Mute List ====================
@app.on_message(filters.regex(r"^حذف لیست سکوت$"))
async def clear_mute_handler(client, message):
    eem = ""
    t_eem = 1
    if len(mutey) >= 1:
        for user in mutey:
            user_obj = await client.get_users(user)
            eem += f"{t_eem} - <a href=tg://user?id={user}>{user_obj.first_name}</a>\n"
            t_eem += 1
        await message.edit_text(f"**✔️ لیست سکوت پاکسازی شد!**\n{eem}")
        mutey.clear()
    else:
        await message.edit_text(f"**(⚠️) لیست سکوت خالی است!**")

# ==================== Time Bio V1 ====================
@app.on_message(filters.regex(r"^ساعت بیو اول (روشن|خاموش)$"))
async def time_bio_v1_handler(client, message):
    if message.text.split()[2] == "روشن":
        json_database.update({"timebiov1": "on"})
        write("data.json", json.dumps(json_database))
        await message.edit_text(f"**✔️ ساعت در بیوگرافی 1 روشن شد!**")
    elif message.text.split()[2] == "خاموش":
        json_database.update({"timebiov1": "off"})
        write("data.json", json.dumps(json_database))
        await message.edit_text(f"**✔️ ساعت در بیوگرافی 1 خاموش شد!**")
    else:
        await message.edit_text(f"**(⚠️) خطای نامشخص!**")

# ==================== Timezone ====================
@app.on_message(filters.regex(r"^منطقه زمانی (ایران|انگلیس)$"))
async def timezone_handler(client, message):
    area = message.text.split()[1]
    try:
        with open("data.json", "r") as file:
            settings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        settings = {}
    
    if area == "ایران":
        settings["timezone"] = "Asia/Tehran"
        response_text = "**✔️ منطقه زمانی روی ایران تنظیم شد!**"
    elif area == "انگلیس":
        settings["timezone"] = "America/New_York"
        response_text = "**منطقه زمانی روی انگلیس تنطیم شد!**"
    else:
        response_text = "**(⚠️) منطقه نامشخص، لطفا از منطقه زمانی ایران یا انگلیس استفاده نمایید!**"
        await message.edit_text(response_text)
        return
    
    with open("data.json", "w") as file:
        json.dump(settings, file)

    await message.edit_text(response_text)

# ==================== Font Name ====================
@app.on_message(filters.regex(r"^فونت نام (روشن|خاموش)$"))
async def font_name_handler(client, message):
    if message.text.split()[1] == "روشن":
        json_database.update({"fontname": "on"})
        write("data.json", json.dumps(json_database))
        await message.edit_text(f"**✔️ فونت نام روشن شد!**")
    elif message.text.split()[1] == "خاموش":
        json_database.update({"fontname": "off"})
        write("data.json", json.dumps(json_database))
        await message.edit_text(f"**✔️ فونت نام خاموش شد!**")
    else:
        await message.edit_text(f"**(⚠️) خطای نامشخص!**")

# ==================== Stats ====================
@app.on_message(filters.regex(r"^آمار$"))
async def stats_handler(client, message):
    mh = ""
    a = json_read("data.json")
    pairs = a.items()
    for key, value in pairs:
        mh += f"**⌯⌲ {key} => {value}\n"
    await message.edit_text(f"{mh}")

# ==================== Dice ====================
@app.on_message(filters.regex(r"^\.tas "))
async def tas_handler(client, message):
    if 0 < int(message.text.split()[1]) < 7:
        await client.delete_messages(message.chat.id, message.id)
        while True:
            msg = await client.send_dice(message.chat.id, "🎲")
            if msg.dice.value != int(message.text.split()[1]):
                await msg.delete()
            else:
                break
    else:
        await message.edit_text(f"**(⚠️) لطفا عدد 1 یا 4 را وارد نمایید.**")

# ==================== Dart ====================
@app.on_message(filters.regex(r"^\.dart$"))
async def dart_handler(client, message):
    await client.delete_messages(message.chat.id, message.id)
    while True:
        msg = await client.send_dice(message.chat.id, "🎯")
        if msg.dice.value != 6:
            await msg.delete()
        else:
            break

# ==================== Bowling ====================
@app.on_message(filters.regex(r"^\.bowling$"))
async def bowling_handler(client, message):
    await client.delete_messages(message.chat.id, message.id)
    while True:
        msg = await client.send_dice(message.chat.id, "🎳")
        if msg.dice.value != 6:
            await msg.delete()
        else:
            break

# ==================== Basketball ====================
@app.on_message(filters.regex(r"^\.basketball$"))
async def basketball_handler(client, message):
    await client.delete_messages(message.chat.id, message.id)
    while True:
        msg = await client.send_dice(message.chat.id, "🏀")
        if msg.dice.value != 4:
            await msg.delete()
        else:
            break

# ==================== Football ====================
@app.on_message(filters.regex(r"^\football|فوتبال"))
async def football_handler(client, message):
    json_database = json_read("data.json")
    current_lang = json_database.get("language", "fa")
    if current_lang == "fa":
        if int(message.text.split()[1]) == 1 or int(message.text.split()[1]) == 4:
                await client.delete_messages(message.chat.id, message.id)
                while True:
                    msg = await client.send_dice(message.chat.id, "⚽")
                    if msg.dice.value != int(message.text.split()[1]):
                        await msg.delete()
                    else:
                        break
        else:
            await message.edit_text(f"**(⚠️) لطفا عدد 1 یا 4 را وارد نمایید.**")
    else:
        await message.edit_text(f"**(⚠️) please enter 1 or 4 command**")

# ==================== Panel ====================
@app.on_message(filters.regex(r"^\.پنل$"))
async def panel_handler(client, message):
    bot_results = await client.get_inline_bot_results("Help_ShahBot", "EXISCUTEMIX")
    await client.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[0].id)

# ==================== Help ====================
@app.on_message(filters.regex(r"^راهنما$"))
async def help_handler(client, message):
    bot_results = await client.get_inline_bot_results("Shah_helpBot", "EXISCUTEMIX")
    await client.send_inline_bot_result(message.chat.id, bot_results.query_id, bot_results.results[0].id)

async def initialize_online_status():
    """تنظیم وضعیت آنلاین در شروع ربات"""
    try:
        json_database = json_read("data.json")
        
        if json_database.get("keep_online", "off") == "on":
            await app.invoke(functions.account.UpdateStatus(offline=False))
            print("✅ حالت همیشه آنلاین فعال شد")
            
    except Exception as e:
        print(f"خطا در تنظیم وضعیت آنلاین اولیه: {e}")

scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=5)
scheduler.add_job(mak, "interval", hours=2)
scheduler.add_job(TimeName, "interval", seconds=30)
scheduler.add_job(keep_online_job, "interval", seconds=5)
scheduler.add_job(initialize_online_status, "interval", minutes=5)
scheduler.start()
app.start() , print(Fore.YELLOW+"Started ...") ,print(Fore.GREEN+" https://t.me/Jack_self"), app.send_message("me" , f"**سلف شما با موفقیت فعال شد ✔️\n• با استفاده از دستور « `.پنل` » یا « `.راهنما` » پنل برات باز میشه؛\n• مشکلی بود : @PY_PARSA\n•» نسخه ربات Version: [ V3.1.0 ]**"),idle(), app.stop()