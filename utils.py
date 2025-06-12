import random #kaka BOTS
import time #kaka BOTS
import math #kaka BOTS
import os #kaka BOTS
from vars import CREDIT #kaka BOTS
from pyrogram.errors import FloodWait #kaka BOTS
from datetime import datetime,timedelta #kaka BOTS

class Timer: #NIKHIL SAINI BOTS
    def __init__(self, time_between=5): #KAKA BOTS
        self.start_time = time.time() #KAKA BOTS
        self.time_between = time_between #KAKA BOTS

    def can_send(self): #NIKHIL SAINI BOTS
        if time.time() > (self.start_time + self.time_between): #NIKHIL SAINI BOTS
            self.start_time = time.time() #KAKA BOTS
            return True #KAKA BOTS
        return False #KAKA BOTS

#lets do calculations #KAKA BOTS
def hrb(value, digits= 2, delim= "", postfix=""): #KAKA BOTS
    """Return a human-readable file size. #KAKA
    """ #NIKHIL SAINI BOTS
    if value is None: #NIKHIL SAINI BOTS
        return None #NIKHIL SAINI BOTS
    chosen_unit = "B" #NIKHIL SAINI BOTS
    for unit in ("KB", "MB", "GB", "TB"): #KAKA BOTS
        if value > 1000: #NIKHIL SAINI BOTS
            value /= 1024 #NIKHIL SAINI BOTS
            chosen_unit = unit #KAKA BOTS
        else: #NIKHIL SAINI BOTS
            break #KAKA BOTS
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #KAKA BOTS

def hrt(seconds, precision = 0): #KAKA BOTS
    """Return a human-readable time delta as a string. #KAKA BOTS
    """ #NIKHIL SAINI BOTS
    pieces = [] #NIKHIL SAINI BOTS
    value = timedelta(seconds=seconds) #kaka BOTS

    if value.days: #NIKHIL SAINI BOTS
        pieces.append(f"{value.days}day") #kaka BOTS

    seconds = value.seconds #kaka BOTS

    if seconds >= 3600: #kaka BOTS
        hours = int(seconds / 3600) #kaka BOTS
        pieces.append(f"{hours}hr") #kaka BOTS
        seconds -= hours * 3600 #kaka BOTS

    if seconds >= 60: #kaka BOTS
        minutes = int(seconds / 60) #KAKA BOTS
        pieces.append(f"{minutes}min") #KAKA BOTS
        seconds -= minutes * 60 #KAKA BOTS

    if seconds > 0 or not pieces: #KAKA BOTS
        pieces.append(f"{seconds}sec") #KAKA BOTS

    if not precision: #KAKA BOTS
        return "".join(pieces) #KAKABOTS

    return "".join(pieces[:precision]) #NIKHIL SAINI BOTS

timer = Timer() #NIKHIL SAINI BOTS

async def progress_bar(current, total, reply, start): #NIKHIL SAINI BOTS
    if timer.can_send(): #NIKHIL SAINI BOTS
        now = time.time() #NIKHIL SAINI BOTS
        diff = now - start #NIKHIL SAINI BOTS
        if diff < 1: #NIKHIL SAINI BOTS
            return #NIKHIL SAINI BOTS
        else: #NIKHIL SAINI BOTS
            perc = f"{current * 100 / total:.1f}%" #NIKHIL SAINI BOTS
            elapsed_time = round(diff) #NIKHIL SAINI BOTS
            speed = current / elapsed_time #NIKHIL SAINI BOTS
            remaining_bytes = total - current #NIKHIL SAINI BOTS
            if speed > 0: #NIKHIL SAINI BOTS
                eta_seconds = remaining_bytes / speed #NIKHIL SAINI BOTS
                eta = hrt(eta_seconds, precision=1) #NIKHIL SAINI BOTS
            else: #NIKHIL SAINI BOTS
                eta = "-" #NIKHIL SAINI BOTS
            sp = str(hrb(speed)) + "/s" #NIKHIL SAINI BOTS
            tot = hrb(total) #NIKHIL SAINI BOTS
            cur = hrb(current) #NIKHIL SAINI BOTS
            bar_length = 10 #NIKHIL SAINI BOTS
            completed_length = int(current * bar_length / total) #NIKHIL SAINI BOTS
            remaining_length = bar_length - completed_length #NIKHIL SAINI BOTS

            symbol_pairs = [ #NIKHIL SAINI BOTS
                ("▬", "▭"), #NIKHIL SAINI BOTS
                ("✅", "☑️"), #NIKHIL SAINI BOTS
                ("🐬", "🦈"), #NIKHIL SAINI BOTS
                ("💚", "💛"), #NIKHIL SAINI BOTS
                ("🌟", "⭐"), #NIKHIL SAINI BOTS
                ("▰", "▱") #NIKHIL SAINI BOTS
            ] #NIKHIL SAINI BOTS
            chosen_pair = random.choice(symbol_pairs) #NIKHIL SAINI BOTS
            completed_symbol, remaining_symbol = chosen_pair #NIKHIL SAINI BOTS

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #NIKHIL SAINI BOTS

            try: #NIKHIL SAINI BOTS
                await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{CREDIT}🦋✨═══─╯`') 
                #await reply.edit(f'`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎🦋✨═══─╯`') 
            except FloodWait as e: #NIKHIL SAINI BOTS
                time.sleep(e.x) #NIKHIL SAINI BOTS 
