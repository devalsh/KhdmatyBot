import sqlite3
import telebot
import requests
import kvsqlite
import random
from time import sleep
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from sqlite3 import Error
import time, json, datetime
from multiprocessing.pool import ThreadPool
from datetime import datetime

USEING_INFO_TEXT = """
📜 *شروط الاستخدام *📜

مرحبًا بكم في البوت الخاص بنا! نحن سعداء بانضمامكم إلينا. لضمان أفضل تجربة لكم، يُرجى قراءة شروط الاستخدام التالية بعناية:

*القبول بالشروط:*

باستخدام هذا البوت، فإنك توافق على الالتزام بشروط الاستخدام هذه. إذا كنت لا توافق على أي من هذه الشروط، يُرجى عدم استخدام البوت.

*استخدام البوت:*

يُمنع استخدام البوت لأي غرض غير قانوني أو غير أخلاقي.
يُمنع استخدام أي وسائل غش لتحقيق النقاط أو المكافآت.
يُمنع إساءة استخدام البوت أو محاولة تعطيله بأي شكل من الأشكال.

*البيانات الشخصية:*

نحن نحترم خصوصيتك ونلتزم بحماية بياناتك الشخصية.
قد نقوم بجمع بعض المعلومات لتحسين خدماتنا وتخصيص تجربتك مع البوت.

*النقاط والمكافآت:*

نظام النقاط مصمم لتشجيع التفاعل والمشاركة.
نحن نحتفظ بالحق في تعديل أو إلغاء نظام النقاط والمكافآت في أي وقت دون إشعار مسبق.

*إخلاء المسؤولية:*

نحن نبذل قصارى جهدنا لضمان أن يكون البوت متاحًا ويعمل بشكل صحيح في جميع الأوقات. ومع ذلك، لا نتحمل أي مسؤولية عن أي انقطاع أو خطأ في الخدمة.
استخدامك للبوت هو على مسؤوليتك الشخصية.

*التعديلات على الشروط:*

نحن نحتفظ بالحق في تعديل شروط الاستخدام هذه في أي وقت. سيتم إشعار المستخدمين بأي تعديلات جوهرية.
استمرار استخدامك للبوت بعد أي تعديل يُعتبر قبولًا منك بالشروط المعدلة.

*إنهاء الاستخدام:*

نحن نحتفظ بالحق في إنهاء أو تعليق وصولك إلى البوت في أي وقت، دون إشعار مسبق، إذا انتهكت أيًا من هذه الشروط.
إذا كانت لديكم أي استفسارات أو تحتاجون إلى مساعدة، لا تترددوا في الاتصال بفريق الدعم الخاص بنا.

*باستخدامك للبوت، فإنك تقر بأنك قد قرأت وفهمت وتوافق على الالتزام بشروط الاستخدام هذه.*

*شكراً لكم ونأمل أن تستمتعوا باستخدام البوت الخاص بنا!*
"""
SPEED_CHANNELS = ["@khdmatyUp"] # قنوات البوست .
CHANNELS = ["@AlsHCh1","@ithbat","@khdmatyUp"] # قنوات الاشتراك الاجباري .
BOT_TMWEL = "https://t.me/ii88BOT" # رابط البوت .
BOT_LINK = "t.me/ii88BOT" # رابط البوت .
ORDERS_CHANNEL = "@KhdmatyOrders" # قناة الطلبات .
ITHBAT_CHANNEL = "@ithbat" # قناة الاثباتات .
DEV = "[AlsH](t.me/DevAlsH)" # قناة المطور .
INVITE = 10 # عدد نقاط الدعوة عند الانضمام . 
ADMIN_USERNAME = "BXUUU" # يوزر الادمن .
REPLAY = "10" # نقاط الخصم عند التحويل .
CEO_ID = "1067280015" # ايدي المالك .
ADMIN = "1476820455" # ايدي الادمن .
BOT = "@ii88BOT" # يوزر البوت .
BOT_NAME = "خدماتي ." # اسم البوت .
CURNNCY = "نقطة" # العملة .
DilayGift = "5" # الهدية اليوميه .
Def_AlsH_ID = 1981897842
token = '7455426596:AAEYcuavZcX3Es71fueVgUWz3vV3dpdrVmw' # BOT LINK : https://t.me/ii88Bot .
#token = '7281113132:AAFhRAIFU1djECGEQok4XDJw_PZ_H1DVgds' # BOT LINK : https://t.me/ii252Bot .
bot = telebot.TeleBot(token, num_threads=20, skip_pending=True)

try :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
except Error as e:
  print(e)
  print("THE ERROR IN LINE 40 !!!!!!!")

def AdminStart(USER_ID,MSGID) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' LIMIT 1")
  USER_INFO = con.fetchone()
  USER_NAME = USER_INFO[3]
  USER_POINTS = USER_INFO[6]
  USER_SAT = USER_INFO[10]
  if USER_SAT == "Admin" :
    key = InlineKeyboardMarkup(row_width=2)
    a1 = types.InlineKeyboardButton(text="قسم الاذاعه",callback_data="cast")
    a2 = types.InlineKeyboardButton(text="قسم الادمنيه",callback_data="ad")
    a3 = types.InlineKeyboardButton(text="قسم الاحصائيات",callback_data="info")
    a4 = types.InlineKeyboardButton(text="اضافة نقاط",callback_data="addpoints")
    a5 = types.InlineKeyboardButton(text="خصم نقاط",callback_data="delpoints")
    a5 = types.InlineKeyboardButton(text="حالة البوت",callback_data="Test")
    key.add(a1,a2,a3)
    key.add(a4,a5)
    TADMIN = F"*اهلا بك في بوحة تحكم الادمن الخاصة بالبوت*\n\n- يمكنك التحكم بالبوت الخاص بك من هنا"
    bot.send_message(USER_ID,TADMIN,parse_mode='markdown',reply_markup=key)

def Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM) :
  print(F"{USER_ID} <==> {USER_USERNAME}")
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"UPDATE users SET username='{USER_USERNAME}', fname='{USER_FIRSTNAME}', lname='{USER_LASTNAME}', premium='{USER_IS_PREMUIM}' WHERE tele_id='{USER_ID}'")
  conn.commit()
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' LIMIT 1")
  USER_INFO = con.fetchone()
  USER_NAME = USER_INFO[3]
  USER_POINTS = USER_INFO[6]
  USER_SAT = USER_INFO[10]
  BOT_SAT = USER_INFO[13]
  #if USER_SAT == "Admin" :
  #  AdminStart(USER_ID,MSGID)
  if BOT_SAT == "Active" :
    key = InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton(text=F"💰 ⫶ نقاطك {USER_POINTS} .",callback_data="points")
    a2 = types.InlineKeyboardButton(text="👤 ⫶ الحساب .",callback_data="Account")
    a3 = types.InlineKeyboardButton(text="➕ ⫶ تجميع نقاط .",callback_data="CollectPoints")
    a4 = types.InlineKeyboardButton(text="🦾 ⫶ سحب اللارباح .",callback_data="Offers")
    a5 = types.InlineKeyboardButton(text="🔁 ⫶ تحويل نقاط .",callback_data="transPoints")
    a6 = types.InlineKeyboardButton(text="📮 ⫶ إستعلام طلب .",callback_data="OrderInfo")
    a8 = types.InlineKeyboardButton(text="💸 ⫶ شراء نقاط .",callback_data="Paypoints")
    a7 = types.InlineKeyboardButton(text="⚙ ⫶ الإعدادات .",callback_data="settings")
    key.add(a1)
    key.add(a2,a3)
    key.add(a4,a5)
    key.add(a6,a8)
    key.add(a7)
    T = F"🧑🏻‍💻︙مرحباً بك  {USER_NAME} \n🙋🏻︙في بوت {BOT_NAME} \n🆔︙أيدي حسابك : `{USER_ID}` \n💸︙عدد كوينز لديك : {USER_POINTS} \n✳️︙يمكن التحكم بالبوت عبر الأزرار في الاسفل👇🏻"
    bot.send_message(USER_ID,T,parse_mode='markdown',reply_markup=key)
  elif BOT_SAT == "Editing" :
    T = "*⌔︙عذرا البوت تحت الصيانه الان .*"
    bot.send_message(USER_ID,T,parse_mode='markdown')
  else :
    T = "*ERROR !*"
    bot.send_message(USER_ID,T,parse_mode='markdown')

def ch(user_id: str):
  user_id = str(user_id)
  x = requests.get(
    "https://api.telegram.org/bot"
    + f"{token}"
    + "/getchatmember?chat_id=alshch1&user_id="
    + user_id
  )
  if any(["member" in x.text, "administrator" in x.text, "creator" in x.text]):
    return True
  else:
    # bot.reply_to(message, "You Must Be In The Channel To Use The Bot !")
    return False

@bot.message_handler(commands=['help'])
def help(message):
  k = '''
*قريبـاً...*
  '''
  bot.reply_to(message,k,parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(message):
  MSGID = message.id
  USER_ID = str(message.chat.id)
  USER_FIRSTNAME = message.chat.first_name 
  USER_LASTNAME = message.chat.last_name
  USER_USERNAME = message.from_user.username
  USER_LANGUAGE = message.from_user.language_code
  USER_IS_PREMUIM = message.from_user.is_premium
  if USER_LASTNAME == None :
    USER_LINK = F"[{USER_FIRSTNAME}](tg://openmessage?user_id={USER_ID})"
  else :
    USER_LINK = F"[{USER_FIRSTNAME} {USER_LASTNAME}](tg://openmessage?user_id={USER_ID})"
  try :
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"SELECT * FROM users WHERE id='2' ")
    gg = con.fetchone()
    BOT_SAT = gg[13]
    con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' LIMIT 1")
    result = con.fetchone()
    try :
      if result == None : # MEAN THE USER NOT IN DATABASE .
        StartFrom = message.text
        TextSplit = StartFrom.split()[1:]
        if " " in StartFrom : # MEAN THE USER COME FROM OTHER USER .
          ComFrom = TextSplit[0]
          con.execute(F"SELECT * FROM users WHERE tele_id='{ComFrom}'")
          ComFromInfo = con.fetchone()
          if ComFromInfo !=None : # MEAN HE REALLY COME FROM OTHER USER IN DATABASE . 
            for i in CHANNELS:
              checkInvite = bot.get_chat_member(i, USER_ID)
              START_LINK = F"[/start](https://{BOT_LINK}?start={ComFrom})"
              if checkInvite.status == 'left' :
                msg_start = "*🍔 لأستخدام هذا البوت يجب عليك الانضمام في القناة - *"
                for i in CHANNELS:
                  msg_start += f"*\n➡️ {i} \n*"
                msg_start += "\n"
                msg_start += F"*- أشترك ثم أرسل *{START_LINK} *.*"
                bot.send_message(USER_ID,msg_start,parse_mode="Markdown")
                bot.delete_message(USER_ID,MSGID)
                exit(0)
            if checkInvite.status == 'left' :
              pass
            else :
              ComFromUSERNAME = ComFromInfo[1]
              ComFromNAME = ComFromInfo[3]
              ComFromPoints = ComFromInfo[6]
              ComFromShareLink = ComFromInfo[7]
              ComFromLink = F"[{ComFromNAME}](t.me/{ComFromUSERNAME})"
              StartedUser = F"[{USER_FIRSTNAME}](t.me/{USER_USERNAME})"
              NewShareLink = int(ComFromShareLink) + 1
              NewPoints = int(ComFromPoints) + int(INVITE)
              con.execute(F"UPDATE users SET link_share='{NewShareLink}', points='{NewPoints}' WHERE tele_id='{ComFrom}' ")
              conn.commit()
              conn = sqlite3.connect("DBIQ.DB")
              con = conn.cursor()
              con.execute(F"INSERT INTO users (tele_id,username,fname,lname,lang,bot_sat,premium) VALUES ('{USER_ID}','{USER_USERNAME}','{USER_FIRSTNAME}','{USER_LASTNAME}','{USER_LANGUAGE}','{BOT_SAT}','{USER_IS_PREMUIM}')")
              conn.commit()
              Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
              bot.send_message(ComFrom,text=F"*قام *{StartedUser}*, بالدخول الى الرابط الخاص بك وحصلت على {INVITE} {CURNNCY} .\n -  أصبحت نقاطك {NewPoints} .*",parse_mode='markdown',disable_web_page_preview=True)
              All_USERS = 0
              con.execute(F"SELECT id FROM users")
              AllUSERS = con.fetchall()
              for i in AllUSERS:
                All_USERS+=1
              if USER_LASTNAME == None :
                USER_LASTNAME = ""
              if USER_USERNAME == None :
                iUSER_LINK = "لايوجد"
              else :
                iUSER_LINK = F"[{USER_USERNAME}](https://t.me/{USER_USERNAME})"
              T = F"""*تم دخول شخص جديد الى البوت الخاص بك 👾*
                            *-----------------------*
                • معلومات العضو الجديد .

                • الاسم : {USER_LINK}
                • المعرف : {iUSER_LINK} 
                • الايدي : `{USER_ID}` 
                            *-----------------------*
                • عدد الاعضاء الكلي :* {All_USERS}* """
              bot.send_message(CEO_ID,T,parse_mode="Markdown",disable_web_page_preview=True) 
              bot.send_message(CEO_ID,text=F"*قام *{StartedUser}*, بالدخول الى الرابط الخاص بـ *{ComFromLink}* وحصل على {INVITE} {CURNNCY} .\n - أصبحت نقاطه {NewPoints} .*",parse_mode='markdown',disable_web_page_preview=True)
          else : # MEAN HE USE RANGER LINK TO START THE BOT .
            conn = sqlite3.connect("DBIQ.DB")
            con = conn.cursor()
            con.execute(F"INSERT INTO users (tele_id,username,fname,lname,lang,bot_sat,premium) VALUES ('{USER_ID}','{USER_USERNAME}','{USER_FIRSTNAME}','{USER_LASTNAME}','{USER_LANGUAGE}','{BOT_SAT}','{USER_IS_PREMUIM}')")
            conn.commit()
            Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
            All_USERS = 0
            con.execute(F"SELECT id FROM users")
            ids = con.fetchall()
            for i in ids:
              All_USERS+=1
            if USER_LASTNAME == None :
              USER_LASTNAME = " "
            if USER_USERNAME == None :
              iUSER_LINK = "لايوجد"
            else :
              iUSER_LINK = F"[{USER_USERNAME}](https://t.me/{USER_USERNAME})"
            Tii = F"""*تم دخول شخص جديد الى البوت الخاص بك 👾*
                      *-----------------------*
            • معلومات العضو الجديد .

            • الاسم : {USER_LINK}
            • المعرف : {iUSER_LINK} 
            • الايدي : `{USER_ID}` 
                      *-----------------------*
            • عدد الاعضاء الكلي :* {All_USERS}* """
            bot.send_message(CEO_ID,Tii,parse_mode="Markdown",disable_web_page_preview=True) 
        else : # MEAN THE USER DIDNT COME FROM OTHER USER .
          for i in CHANNELS:
            checkInvite = bot.get_chat_member(i, USER_ID)
            START_LINK = F"[/start](https://{BOT_LINK}?start)"
            if checkInvite.status == 'left' :
              msg_start = "*🍔 لأستخدام هذا البوت يجب عليك الانضمام في القناة - *"
              for i in CHANNELS:
                msg_start += f"*\n➡️ {i} \n*"
              msg_start += "\n"
              msg_start += F"*- أشترك ثم أرسل *{START_LINK} *.*"
              bot.send_message(USER_ID,msg_start,parse_mode="Markdown")
              bot.delete_message(USER_ID,MSGID)
              exit(0)
          if checkInvite.status == 'left' :
            pass
          else :
            conn = sqlite3.connect("DBIQ.DB")
            con = conn.cursor()
            con.execute(F"INSERT INTO users (tele_id,username,fname,lname,lang,bot_sat,premium) VALUES ('{USER_ID}','{USER_USERNAME}','{USER_FIRSTNAME}','{USER_LASTNAME}','{USER_LANGUAGE}','{BOT_SAT}','{USER_IS_PREMUIM}')")
            conn.commit()
            Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
            All_USERS = 0
            con.execute(F"SELECT id FROM users")
            ids = con.fetchall()
            for i in ids:
              All_USERS+=1
            if USER_LASTNAME == None :
              USER_LASTNAME = " "
            if USER_USERNAME == None :
              iUSER_LINK = "لايوجد"
            else :
              iUSER_LINK = F"[{USER_USERNAME}](https://t.me/{USER_USERNAME})"
            Tii = F"""*تم دخول شخص جديد الى البوت الخاص بك 👾*
                      *-----------------------*
            • معلومات العضو الجديد .

            • الاسم : {USER_LINK}
            • المعرف : {iUSER_LINK} 
            • الايدي : `{USER_ID}` 
                      *-----------------------*
            • عدد الاعضاء الكلي :* {All_USERS}* """
            bot.send_message(CEO_ID,Tii,parse_mode="Markdown",disable_web_page_preview=True) 
      else : # MEAN THE USER IN DATABASE .
        Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
    except Error as e:
      print(e)
  except Error as e:
    print(e)

@bot.message_handler(func=lambda m:True)
def m2(message):
  USER_ID = str(message.chat.id)
  USER_FIRSTNAME = message.chat.first_name 
  USER_LASTNAME = message.chat.last_name 
  USER_USERNAME = message.chat.username
  USER_LANGUAGE = message.from_user.language_code
  USER_LINK = F"[{USER_FIRSTNAME}](tg://openmessage?user_id={USER_ID})"
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' ")
  USER_INFO = con.fetchone()
  USER_SAT = USER_INFO[10]
  if message.text.startswith("/admin") and USER_SAT == "Admin" :
    MSGID = message.message_id
    AdminStart(USER_ID,MSGID)
  if message.text.startswith("/botsat") and USER_SAT == "Admin" :
    MSGID = message.message_id
    BotSat(USER_ID,MSGID)
  if message.text.startswith("/getorderinfo ") and USER_SAT == "Admin" :
    MSGID = message.message_id
    ORDER_CODE = message.text.split("/getorderinfo ")[1]
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"SELECT * FROM orders WHERE order_code='{ORDER_CODE}' LIMIT 1")
    ORDER_INFO = con.fetchone()
    if ORDER_INFO != None :
      bot.send_message(USER_ID,text="*تم العثور على الطلب بنجاح .*",parse_mode="Markdown")
    else :
      bot.send_message(USER_ID,text="*لم يتم العثور على طلب بهذا الكود !!*",parse_mode="Markdown")
  if message.text.startswith("/ban ") and USER_SAT == "Admin" :
    USER = int(message.text.split("/ban ")[1])
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"UPDATE users SET statuse='Banded' WHERE tele_id='{USER}' ")
    conn.commit()
    bot.reply_to(message, 'تم حظره  !!')
    try:
      bot.send_message(chat_id=USER, text='تم حظرك .')
    except:
      return
  if message.text.startswith("/unban ") and USER_SAT == "Admin" :
    USER = message.text.split("/unban ")[1]
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"UPDATE users SET statuse='Active' WHERE tele_id='{USER}' ")
    conn.commit()
    bot.reply_to(message, 'تم الغاء حظره !!')
    try:
      bot.send_message(chat_id=USER, text='تم فك حظرك .')
    except:
      return
  if message.text.startswith("/cast") and USER_SAT == "Admin" :
    x = bot.reply_to(message, 'ارسل الاذاعه هسه (صورة، نص ، فويس، تحويل، ملف )')
    bot.register_next_step_handler(x, checkcast)
  if message.text.startswith("/addpoints ") and USER_SAT == "Admin" : # أضافة نقاط .
    spil = message.text.split(" ")
    USER = spil[1]
    addpoints = spil[2]
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"SELECT * FROM users WHERE tele_id={USER}")
    USER_INFO = con.fetchone()
    add_FNAME = USER_INFO[3]
    USER_POINTS = USER_INFO[6]
    add_LINK = F"[{add_FNAME}](tg://openmessage?user_id={USER})"
    new_points = int(USER_POINTS) + int(addpoints)
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"UPDATE users SET points='{new_points}' WHERE tele_id='{USER}' ")
    conn.commit()
    bot.reply_to(message, F'تم اضافة {addpoints} الى {add_LINK} وأصبحت نقاطه {new_points} .',parse_mode="Markdown")
    bot.send_message(chat_id=USER, text=F'تم اضافة {addpoints} نقطة الى حسابك من قبل الادمن .',parse_mode="Markdown")
  if message.text.startswith("/delpoints ") | message.text.startswith("Delpoints ") | message.text.startswith("delpoints ") and USER_SAT == "Admin" : # حذف نقاط .
    spil = message.text.split(" ")
    USER = spil[1]
    addpoints = spil[2]
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"SELECT * FROM users WHERE tele_id={USER}")
    USER_INFO = con.fetchone()
    add_FNAME = USER_INFO[3]
    USER_POINTS = USER_INFO[6]
    add_LINK = F"[{add_FNAME}](tg://openmessage?user_id={USER})"
    new_points = int(USER_POINTS) - int(addpoints)
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"UPDATE users SET points='{new_points}' WHERE tele_id='{USER}' ")
    conn.commit()
    bot.reply_to(message, F'تم خصم {addpoints} من {add_LINK} وأصبحت نقاطه {new_points} .',parse_mode="Markdown")
    bot.send_message(chat_id=USER, text=F'تم خصم {addpoints} نقطة من حسابك من قبل الادمن .',parse_mode="Markdown")
  if message.text.startswith("/sendmessage ") | message.text.startswith("/sendmsg ") and USER_SAT == "Admin" : # حذف نقاط .
    spil = message.text.split(" ")
    USER = spil[1]
    MSG = spil[2]
    con.execute(F"SELECT * FROM users WHERE tele_id={USER} LIMIT 1")
    USER_INFO = con.fetchone()
    if USER_INFO != None :
      try :
        bot.send_message(USER,MSG,parse_mode="Markdown")
      except :
        bot.send_message(USER_ID,text="*هذا المستخدم قام بحظر البوت !!*",parse_mode="Markdown")
    else :
      bot.send_message(USER_ID,text="*هذا المستخدم غير موجود في البوت !!*",parse_mode="Markdown")
  if message.text.startswith("/setlink ") | message.text.startswith("/link") :
    MSGID = message.message_id
    bot.register_next_step_handler(message,SETORDERLINK,USER_ID)
    bot.send_message(USER_ID,F"*أرسل كود الطلب :*",parse_mode="Markdown")
  if message.text.startswith("/active ") | message.text.startswith("Active ") | message.text.startswith("active ") and USER_SAT == "Admin" :
    spil = message.text.split(" ")
    USER = spil[1]
    print(USER)
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"SELECT * FROM users WHERE tele_id={USER}")
    t = con.fetchone()
    if t != None :
      try :
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"UPDATE users SET bot_sat='Active' WHERE tele_id={USER}")
        conn.commit()
        bot.send_message(USER,text="*تم تفعيل البوت لديك من قبل الأدمن*",parse_mode="markdown")
        bot.send_message(USER_ID,text=F"*تم تفعيل البوت لـ{USER} .*",parse_mode="markdown")
      except :
        bot.send_message(USER_ID,text="*حدث خطأ ما !*",parse_mode="markdown")
    else :
      bot.send_message(USER_ID,text="*هذا اليوزر غير موجود في البوت !*",parse_mode="markdown")
  if message.text.startswith("/editing ") | message.text.startswith("Editing ") | message.text.startswith("editing ") and USER_SAT == "Admin" :
    spil = message.text.split(" ")
    USER = spil[1]
    print(USER)
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"SELECT * FROM users WHERE tele_id={USER}")
    t = con.fetchone()
    if t != None :
      try :
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"UPDATE users SET bot_sat='Editing' WHERE tele_id={USER}")
        conn.commit()
        bot.send_message(USER_ID,text=F"*تم تعطيل البوت لـ{USER} .*",parse_mode="markdown")
      except :
        bot.send_message(USER_ID,text="*حدث خطأ ما !*",parse_mode="markdown")
    else :
      bot.send_message(USER_ID,text="*هذا اليوزر غير موجود في البوت !*",parse_mode="markdown")

@bot.callback_query_handler(func=lambda m:True)
def call(call):
  USER_ID = call.from_user.id
  USER_FIRSTNAME = call.from_user.first_name 
  USER_LASTNAME = call.from_user.last_name 
  USER_USERNAME = call.from_user.username
  USER_LINK = F"[{USER_FIRSTNAME}](tg://openmessage?user_id={USER_ID})"
  USER_IS_PREMUIM = call.from_user.is_premium
  MSGID = call.message.id
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id={USER_ID}")
  USER_INFO = con.fetchone()
  USER_POINTS = USER_INFO[6]
  USER_DEPOSIT = USER_INFO[8]
  USER_STATUSE = USER_INFO[9]
  USER_SAT = USER_INFO[10]
  BOT_SAT = USER_INFO[13]
  if USER_STATUSE == "Banded" :
    bot.send_message(USER_ID,"*المعذرة أنت محظور لا يمكنك استخدام البوت .*",parse_mode="Markdown")
  elif BOT_SAT == "Editing" :
    T = "*⌔︙عذرا البوت  تحت الصيانه الان .*"
    try :
      bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown')
    except :
      bot.send_message(USER_ID,T,parse_mode='markdown')
  else :
    for i in CHANNELS:
      checkInvite = bot.get_chat_member(i, USER_ID)
      if BOT_SAT == "Active" :
        if checkInvite.status == 'left' :
          msg_start = "*🍔 لأستخدام هذا البوت يجب عليك الانضمام في القناة - "
          for i in CHANNELS:
            msg_start += f"\n➡️ {i} \n"
          msg_start += "*\n"
          msg_start += "*- أشترك ثم أرسل /start .*"
          bot.send_message(USER_ID,msg_start,parse_mode="Markdown")
          return
      else :
        T = "*ERROR !*"
        bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown')
    if checkInvite.status == 'left' :
      pass
    else :
      # - - | ORDER CALLS | - -
      if "AcceptOrder " in call.data and USER_SAT == "Admin" :
        ORDER_ID = call.data.split()[1:]
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM orders WHERE order_code='{str(ORDER_ID[0])}' LIMIT 1")
        ORDER_INFO = con.fetchone()
        con.execute(F"SELECT * FROM users WHERE tele_id='{ORDER_INFO[2]}' LIMIT 1")
        USER_INFO = con.fetchone()
        if ORDER_INFO != None :
          ORDER_CODE = ORDER_INFO[1]
          ORDER_USER_ID = ORDER_INFO[2]
          ORDER_NAME = ORDER_INFO[3]
          ORDER_NUM = ORDER_INFO[4]
          ORDER_PRICE = ORDER_INFO[5]
          ORDER_URL = ORDER_INFO[6]
          ORDER_STATUSE = ORDER_INFO[7]
          ORDER_DATE = ORDER_INFO[8]
          NEW_STATUSE = "تحت التنفيذ"
          con.execute(F"UPDATE orders SET statuse='{NEW_STATUSE}' WHERE order_code='{ORDER_CODE}' ")
          conn.commit()
          key = InlineKeyboardMarkup()
          a1 = types.InlineKeyboardButton(text=F"❌ ¦ إلغاء الطلب .",callback_data=F"CancelOrderCouse {ORDER_CODE}")
          a2 = types.InlineKeyboardButton(text=F"✅ ¦ التحديث إلى مكتمل .",callback_data=F"CompletedOrder {ORDER_CODE}")
          a3 = types.InlineKeyboardButton(text=F"🔗 ¦ إضافة رابط .",callback_data=F"AddLink {ORDER_CODE}")
          key.add(a1)
          key.add(a2)
          key.add(a3)
          T = F"*NEW ORDER :*\n*                  <--------------->*\nكود الطلب : `{ORDER_CODE}`\nالطلب : *{ORDER_NAME}*\nالعدد : *{ORDER_NUM}*\nالسعر : *{ORDER_PRICE}*\nالرابط : `{ORDER_URL}`\nحالة الطلب : *{NEW_STATUSE}*\nالتوقيت : *{ORDER_DATE}*\n*                  <--------------->*\nمعلومات المستخدم :\nالاسم : {USER_INFO[3]}\nايديه : `{USER_INFO[2]}`\nيوزره : *@{USER_INFO[1]}*\nعدد نقاطه : *{USER_INFO[6]}*"
          bot.edit_message_text(T,ORDERS_CHANNEL,MSGID,parse_mode='markdown',reply_markup=key)
          key = InlineKeyboardMarkup()
          a1 = types.InlineKeyboardButton(text=F"📮 ¦ الإستفسار عن الطلب أعلاه .",url=F"https://t.me/devalsh?text=بخصوص الطلب :`{ORDER_CODE}`, \n\n")
          key.add(a1)
          TT = F"*تحديث الطلب :*\n🎟 *¦* كود الطلب :- `{ORDER_CODE}` . \n🏷 *¦*  السلعة :- *{ORDER_NUM}* - *{ORDER_NAME}* .\n⛓ *¦* الرابط :- `{ORDER_URL}` \n📍 *¦* حالة الطلب :- *{NEW_STATUSE}* ."
          bot.send_message(USER_INFO[2],TT,parse_mode='markdown',reply_markup=key)
      if "CompletedOrder " in call.data and USER_SAT == "Admin" :
        ORDER_ID = call.data.split()[1:]
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM orders WHERE order_code='{str(ORDER_ID[0])}' LIMIT 1")
        ORDER_INFO = con.fetchone()
        if ORDER_INFO != None :
          ORDER_CODE = ORDER_INFO[1]
          ORDER_USER_ID = ORDER_INFO[2]
          ORDER_NAME = ORDER_INFO[3]
          ORDER_NUM = ORDER_INFO[4]
          ORDER_PRICE = ORDER_INFO[5]
          ORDER_URL = ORDER_INFO[6]
          ORDER_STATUSE = ORDER_INFO[7]
          ORDER_DATE = ORDER_INFO[8]
          NEW_STATUSE = "مكتمل"
          con.execute(F"UPDATE orders SET statuse='{NEW_STATUSE}' WHERE order_code='{ORDER_CODE}' ")
          conn.commit()
          T = F"*NEW ORDER :*\n*                  <--------------->*\nكود الطلب : `{ORDER_CODE}`\nالطلب : *{ORDER_NAME}*\nالعدد : *{ORDER_NUM}*\nالسعر : *{ORDER_PRICE}*\nالرابط : `{ORDER_URL}`\nحالة الطلب : *{NEW_STATUSE}*\nالتوقيت : *{ORDER_DATE}*\n*                  <--------------->*\nمعلومات المستخدم :\nالاسم : {USER_INFO[3]}\nايديه : `{USER_INFO[2]}`\nيوزره : *@{USER_INFO[1]}*\nعدد نقاطه : *{USER_INFO[6]}*"
          bot.edit_message_text(T,ORDERS_CHANNEL,MSGID,parse_mode='markdown')
          key = InlineKeyboardMarkup()
          a1 = types.InlineKeyboardButton(text=F"📮 ¦ الإستفسار عن الطلب أعلاه .",url=F"https://t.me/devalsh?text=بخصوص الطلب :`{ORDER_CODE}`, \n\n")
          key.add(a1)
          TT = F"*تحديث الطلب :*\n🎟 *¦* كود الطلب :- `{ORDER_CODE}` . \n🏷 *¦*  السلعة :- *{ORDER_NUM}* - *{ORDER_NAME}* .\n⛓ *¦* الرابط :- `{ORDER_URL}`\n📍 *¦* حالة الطلب :- *{NEW_STATUSE}* ."
          bot.send_message(USER_INFO[2],TT,parse_mode='markdown',reply_markup=key)
      if "CancelOrderCouse " in call.data and USER_SAT == "Admin" :
        ORDER_ID = call.data.split()[1:]
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM orders WHERE order_code='{str(ORDER_ID[0])}' LIMIT 1")
        ORDER_INFO = con.fetchone()
        con.execute(F"SELECT * FROM users WHERE tele_id='{ORDER_INFO[2]}' LIMIT 1")
        ORDER_USER_INFO = con.fetchone()
        if ORDER_INFO != None :
          ORDER_CODE = ORDER_INFO[1]
          ORDER_USER_ID = ORDER_INFO[2]
          ORDER_NAME = ORDER_INFO[3]
          ORDER_NUM = ORDER_INFO[4]
          ORDER_PRICE = ORDER_INFO[5]
          ORDER_URL = ORDER_INFO[6]
          ORDER_STATUSE = ORDER_INFO[7]
          ORDER_DATE = ORDER_INFO[8]
          NEW_STATUSE = "ملغي"
          NEW_USER_POINTS = int(ORDER_USER_INFO[6]) + int(ORDER_PRICE)
          con.execute(F"UPDATE orders SET statuse='{NEW_STATUSE}' WHERE order_code='{ORDER_CODE}' ")
          conn.commit()
          con.execute(F"UPDATE users SET points='{NEW_USER_POINTS}' WHERE tele_id='{ORDER_USER_ID}' ")
          conn.commit()
          bot.register_next_step_handler_by_chat_id(USER_ID,CancelCouse,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT,ORDER_CODE)
          bot.send_message(USER_ID,F"*أرسل سبب الغاء طلب *`{ORDER_CODE}`* :*",parse_mode="Markdown")
      if "AddLink " in call.data and USER_SAT == "Admin" :
        ORDER_ID = call.data.split()[1:]
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM orders WHERE order_code='{str(ORDER_ID[0])}' LIMIT 1")
        ORDER_INFO = con.fetchone()
        con.execute(F"SELECT * FROM users WHERE tele_id='{ORDER_INFO[2]}' LIMIT 1")
        ORDER_USER_INFO = con.fetchone()
        if ORDER_INFO != None :
          ORDER_CODE = ORDER_INFO[1]
          ORDER_USER_ID = ORDER_INFO[2]
          ORDER_NAME = ORDER_INFO[3]
          ORDER_NUM = ORDER_INFO[4]
          ORDER_PRICE = ORDER_INFO[5]
          ORDER_URL = ORDER_INFO[6]
          ORDER_STATUSE = ORDER_INFO[7]
          ORDER_DATE = ORDER_INFO[8]
          bot.register_next_step_handler_by_chat_id(USER_ID,AddLinkToOrder,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT,ORDER_CODE)
          bot.send_message(USER_ID,F"*أرسل رابط الطلب *`{ORDER_CODE}`* :*",parse_mode="Markdown")
      # - - | START CALLS | - - 
      if call.data == 'BTS':
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"💰 ⫶ نقاطك {USER_POINTS} .",callback_data="points")
        a2 = types.InlineKeyboardButton(text="👤 ⫶ الحساب .",callback_data="Account")
        a3 = types.InlineKeyboardButton(text="➕ ⫶ تجميع نقاط .",callback_data="CollectPoints")
        a4 = types.InlineKeyboardButton(text="🦾 ⫶ سحب اللارباح .",callback_data="Offers")
        a5 = types.InlineKeyboardButton(text="🔁 ⫶ تحويل نقاط .",callback_data="transPoints")
        a6 = types.InlineKeyboardButton(text="📮 ⫶ إستعلام طلب .",callback_data="OrderInfo")
        a8 = types.InlineKeyboardButton(text="💸 ⫶ شراء نقاط .",callback_data="Paypoints")
        a7 = types.InlineKeyboardButton(text="⚙ ⫶ الإعدادات .",callback_data="settings")
        key.add(a1)
        key.add(a2,a3)
        key.add(a4,a5)
        key.add(a6,a8)
        key.add(a7)
        T = F"🧑🏻‍💻︙مرحباً بك  {USER_FIRSTNAME} \n🙋🏻︙في بوت {BOT_NAME} \n🆔︙أيدي حسابك : `{USER_ID}` \n💸︙عدد كوينز لديك : {USER_POINTS} \n✳️︙يمكن التحكم بالبوت عبر الأزرار في الاسفل👇🏻"
        bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)
      if call.data == 'BTO':
        Offers(USER_ID,MSGID)
      if call.data == 'Account':
        Account(USER_ID,MSGID)
      if call.data == 'settings':
        Settings(USER_ID,MSGID)
      if call.data == "info" :
        Bot_Info(USER_ID,MSGID)
      if call.data == "ad" :
        Bot_Admins(USER_ID,MSGID)
      if call.data == "cast" :
        x = bot.send_message(USER_ID, 'ارسل الاذاعه هسه (صورة، نص ، فويس، تحويل، ملف )')
        bot.register_next_step_handler(x, checkcast)
      if call.data == "CollectPoints" :
        collectpoints(USER_ID,MSGID)
      if call.data == "AdminsBACK" :
        bot.delete_message(USER_ID,call.message.id)
        AdminStart(USER_ID,MSGID)
      if call.data == "UsingInfo" :
        key = InlineKeyboardMarkup()
        aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
        key.add(aa)
        bot.edit_message_text(USEING_INFO_TEXT,USER_ID,MSGID,parse_mode="markdown",reply_markup=key)
      if call.data == "Offers" :
        Offers(USER_ID,MSGID)
      if call.data == "OrderInfo" :
        bot.delete_message(USER_ID,MSGID)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row(F'🚫 ⫶ إلغاء .')
        bot.register_next_step_handler_by_chat_id(USER_ID,OrderInfo,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT)
        bot.send_message(USER_ID,F"*أرسل كود الطلب :*",reply_markup=keyboard,parse_mode="Markdown")
      if call.data == "AddAdmin" :
        bot.delete_message(USER_ID,call.message.id)
        bot.send_message(USER_ID,"*- أرسل ايدي المستخدم لرفعه ادمن في البوت :*",parse_mode="Markdown")
        bot.register_next_step_handler_by_chat_id(USER_ID,AddAdmin)
      if call.data == "Dilygift" :
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y")
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' ")
        result = con.fetchone()
        USER_POINTS = result[6]
        USER_LSAT_GIFT = result[11]
        USER_MANY_GIFTS = result[12]
        if USER_LSAT_GIFT == date_time :
          T = "لقد استلمت الهديه مسبقا ."
          bot.send_message(USER_ID,T)
        else :
          COUNT = int(USER_MANY_GIFTS) + 1
          NEWPOINTS = int(USER_POINTS) + int(DilayGift)
          con.execute(F"UPDATE users SET LastGift='{date_time}', points='{NEWPOINTS}', manygifts='{COUNT}' WHERE tele_id='{USER_ID}' ")
          conn.commit()
          bot.delete_message(USER_ID,call.message.id)
          Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
          T = "تم تحصيل الهديه."
          bot.send_message(USER_ID,T)
      if call.data == "SetBotEditing" :
        SetBotEditing(USER_ID,MSGID)
      if call.data == "SetBotActive" :
        SetBotActive(USER_ID,MSGID)
      if call.data == "BuyedOrders" :
        BuyedOrders(USER_ID,MSGID)
      # - - | PAY CALL | - - 
      if "PAY " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"{GET_PROD_CODE[0]} {GET_PROD_CODE[1]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        PROD_CODE = PROD_INFO[1]
        PROD_NAME = PROD_INFO[2]
        PROD_PRICE = PROD_INFO[3]
        PROD_NUM = PROD_INFO[4]
        PROD_STATUSE = "تحت المعالجة"
        ORDER_URL = "لايوجد"
        if int(PROD_PRICE) <= int(USER_POINTS) :
          NEWPOINTS = int(USER_POINTS) - int(PROD_PRICE)
          NEWDEPOSIT = int(USER_DEPOSIT) + int(PROD_PRICE)
          con.execute(F"UPDATE users SET points='{NEWPOINTS}', deposit='{NEWDEPOSIT}' WHERE tele_id='{USER_ID}' ")
          conn.commit()
          ABC = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
          RAND_INT = random.randint(1000, 99999)
          ABC_RES = random.choices(ABC, k=4)
          ORDER_CODE = F"{ABC_RES[0]}{ABC_RES[1]}{ABC_RES[2]}{ABC_RES[3]}-{RAND_INT}"
          now = datetime.now()
          date_time = now.strftime("%d/%m/%Y")
          conn = sqlite3.connect("DBIQ.DB")
          con = conn.cursor()
          con.execute(F"SELECT * FROM orders WHERE order_code='{ORDER_CODE}' LIMIT 1")
          check_order_id = con.fetchone()
          if check_order_id != None :
            RAND_INT = random.randint(1000, 99999)
            ABC_RES = random.choices(ABC, k=4)
            ORDER_CODE = F"{ABC_RES[0]}{ABC_RES[1]}{ABC_RES[2]}{ABC_RES[3]}-{RAND_INT}"
          key = InlineKeyboardMarkup()
          a1 = types.InlineKeyboardButton(text=F"📮 ¦ الإستفسار عن الطلب أعلاه .",url=F"https://t.me/devalsh?text=بخصوص الطلب :`{ORDER_CODE}`, \n\n")
          key.add(a1)
          T = F"*تم شراء الطلب بنجاح*\n🎟 *¦* كود الطلب :- `{ORDER_CODE}` . \n🏷 *¦*  السلعة :- *{PROD_NUM}* - *{PROD_NAME}* . \n💰 *¦* السعر :- *{PROD_PRICE}* *{CURNNCY}* .\n⛓ *¦* الرابط :- `{ORDER_URL}`\n📍 *¦* حالة الطلب :- *{PROD_STATUSE}* ."
          bot.edit_message_text(T,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
          key = InlineKeyboardMarkup()
          a1 = types.InlineKeyboardButton(text=F"🤖 ¦ الدخول للبوت .",url=F"{BOT_LINK}?start={CEO_ID}")
          key.add(a1)
          TT = F'*- تم تسليم طلب جديد 📦 ✅*\n- من بوت : {BOT} 🤍\n\n🏷 ¦ السلعة :- *{PROD_NUM}* - *{PROD_NAME}.*\n💰 ¦ السعر :- *{PROD_PRICE}* *{CURNNCY}* .\n\n\n*- معلومات المُشتري 👤 :-*\n🏷 ¦ الاسم :- {USER_LINK}\n🆔 ¦ الأيدي :- {USER_ID}'
          bot.send_message(ITHBAT_CHANNEL,TT,parse_mode="Markdown",disable_web_page_preview=True,reply_markup=key)
          key = InlineKeyboardMarkup()
          a1 = types.InlineKeyboardButton(text=F"❌ ¦ إلغاء الطلب .",callback_data=F"CancelOrderCouse {ORDER_CODE}")
          a2 = types.InlineKeyboardButton(text=F"✅ ¦ التحديث إلى جاري العمل .",callback_data=F"AcceptOrder {ORDER_CODE}")
          a3 = types.InlineKeyboardButton(text=F"🔗 ¦ إضافة رابط .",callback_data=F"AddLink {ORDER_CODE}")
          key.add(a1)
          key.add(a2)
          key.add(a3)
          TTT = F"*NEW ORDER :*\n*                  <--------------->*\n:كود الطلب : `{ORDER_CODE}`\nالطلب : *{PROD_INFO[2]}*\nالعدد : *{PROD_INFO[4]}*\nالسعر : *{PROD_PRICE}*\nالرابط : `{ORDER_URL}`\nحالة الطلب : *تحت المعالجة*\nالتوقيت : *{date_time}*\n*                  <--------------->*\nمعلومات المستخدم :\nالاسم : {USER_LINK}\nايديه : `{USER_ID}`\nيوزره : *@{USER_USERNAME}*\nعدد نقاطه : *{NEWPOINTS}*"
          bot.send_message(ORDERS_CHANNEL,TTT,parse_mode="Markdown",disable_web_page_preview=True,reply_markup=key)
          con.execute(F"INSERT INTO orders (order_code, USER, 'order', count, price, url, statuse, date) VALUES ('{ORDER_CODE}', {USER_ID}, '{PROD_NAME}', '{PROD_NUM}', {PROD_PRICE}, '{ORDER_URL}', '{PROD_STATUSE}', '{date_time}')")
          conn.commit()
        else :
          key = InlineKeyboardMarkup()
          a1 = types.InlineKeyboardButton(text="➕ ⫶ تجميع نقاط .",callback_data="CollectPoints")
          aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
          key.add(a1,aa)
          T = "*لا تمتلك ما يكفي من النقاط !*"
          bot.edit_message_text(T,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
        exit(0)
      # - - Call Of Withdrawl AsiaCell - -
      if call.data == "Asiasell" :
        DrawlAsia(USER_ID,MSGID,USER_POINTS)
      if call.data == "NoAsia" :
        Offers(USER_ID,MSGID)
      if "ASIASEEL " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"ASIASEEL {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"NoAsia")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* أسياسيل بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl ZainCash - -
      if call.data == "Zaincash" :
        DrawlZain(USER_ID,MSGID,USER_POINTS)
      if call.data == "NoZain" :
        Offers(USER_ID,MSGID)
      if "ZAIN " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"ZAIN {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"NoAsia")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* زين العراق بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl FIB - -
      if call.data == "FIB" :
        DrawlFIB(USER_ID,MSGID,USER_POINTS)
      if call.data == "NoFIB" :
        Offers(USER_ID,MSGID)
      if "FIB " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"FIB {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"NoAsia")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* مصرف العراق الاول بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Wthdrawl MasterCard - -
      if call.data == "MasterCard" :
        DrawlMasterCard(USER_ID,MSGID,USER_POINTS)
      if call.data == "NoMasterCard" :
        Offers(USER_ID,MSGID)
      if "MASTERCARD " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"MASTERCARD {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"NoAsia")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* ماستر كارد بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Wthdrawl Instagram - -
      if call.data == "Instagram" :
        ChoeseInstagram(USER_ID,MSGID,USER_POINTS)
      # - - Call Of Wthdrawl Instagram Followers - -
      if call.data == "InstagramFollowers" :
        InstagramFollowers(USER_ID,MSGID,USER_POINTS)
      if "INSTAGRAMFOLLOWERS " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"INSTAGRAMFOLLOWERS {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Instagram")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* متابع انستا بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Wthdrawl Instagram Veiows - -
      if call.data == "InstagramVeiows" :
        InstagramVeiows(USER_ID,MSGID,USER_POINTS) 
      if "INSTAGRAMVEIOWS " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"INSTAGRAMVEIOWS {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Instagram")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* مشاهدة انستا بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Wthdrawl Instagram LIKES - -
      if call.data == "InstagramLikes" :
        InstagramLikes(USER_ID,MSGID,USER_POINTS)
      if "INSTAGRAMLIKES " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"INSTAGRAMLIKES {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Instagram")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* لايك انستا بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - CALL OF WITHDRAWL PUBG - - 
      if call.data == "Pubg" :
        Pubg(USER_ID,MSGID,USER_POINTS)
      if "PUBG " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"PUBG {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Pubg")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* {PROD_INFO[2]} بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl telegram - - 
      if call.data == "Tele" :
        ChoeseTle(USER_ID,MSGID) 
      # - - CALL OF WITHDRAWL TELEGRAM FOLLOWERS - -
      if call.data == "TelegramFollowers" :
        TelegramFollowers(USER_ID,MSGID,USER_POINTS)
      if "TELEGRAMFOLLOWERS " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"TELEGRAMFOLLOWERS {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Tele")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* مشترك تلي بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl TELEGRAM VEIOWS - - 
      if call.data == "TelegramVeiows" :
        TelegramVeiows(USER_ID,MSGID,USER_POINTS)
      if "TELEGRAMVEIOWS " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"TELEGRAMVEIOWS {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Tele")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* مشاهدة تلي بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl TikTok - - 
      if call.data == "TelegramLikes" :
        TelegramLikes(USER_ID,MSGID,USER_POINTS)
      if "TELEGRAMLIKES " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"TELEGRAMLIKES {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Tele")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* لايكات تلي بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl TikTok - - 
      if call.data == "Tik" :
        ChoeseTik(USER_ID,MSGID,USER_POINTS) 
      # - - Call Of Withdrawl TikTok Followers - - 
      if call.data == "TikTokFollowers" :
        TikTokFollowers(USER_ID,MSGID,USER_POINTS)
      if "TIKTOKFOLLOWERS " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"TIKTOKFOLLOWERS {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Tik")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* متابع تيك توك بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl TikTok Veiows - - 
      if call.data == "TikTokVeiows" :
        TikTokVeiows(USER_ID,MSGID,USER_POINTS)
      if "TIKTOKVEIOWS " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"TIKTOKVEIOWS {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Tik")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* مشاهدة تيك توك بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl TikTok Likes - - 
      if call.data == "TikLikes" :
        TikLikes(USER_ID,MSGID,USER_POINTS)
      if "TIKTOKLIKES " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"TIKTOKLIKES {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Tik")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* لايكات تيك توك بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Withdrawl TikTok Shares - - 
      if call.data == "TikShares" :
        TikShares(USER_ID,MSGID,USER_POINTS)
      if "TIKTOKSHARES " in call.data :
        GET_PROD_CODE = call.data.split()[1:]
        PROD_CODE = F"TIKTOKSHARES {GET_PROD_CODE[0]}"
        conn = sqlite3.connect("DBIQ.DB")
        con = conn.cursor()
        con.execute(F"SELECT * FROM products WHERE prod_code='{PROD_CODE}' LIMIT 1")
        PROD_INFO = con.fetchone()
        key = InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text=F"✅ - تأكيد الشراء .",callback_data=F"PAY {PROD_CODE}")
        a2 = types.InlineKeyboardButton(text=F"❌ - إلغاء الشراء .",callback_data=F"Tik")
        key.add(a1,a2)
        T1ASIA = F"هل تريد تأكيد شراء* {PROD_INFO[4]}* اكسبلور تيك توك بسعر *{PROD_INFO[3]}* ؟"
        bot.edit_message_text(T1ASIA,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)
      # - - Call Of Trans points - - 
      if call.data == "transPoints" :
        bot.delete_message(USER_ID,MSGID)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row(F'🚫 ⫶ إلغاء .')
        bot.register_next_step_handler_by_chat_id(USER_ID,TransPoints,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT)
        bot.send_message(USER_ID,F"*أرسل ايدي المستخدم \n - علماً أن عمولة التحويل هي {REPLAY} {CURNNCY} .*",reply_markup=keyboard,parse_mode="Markdown")
      # - - Call Of Set Code - - 
      if call.data == "Code" :
        t = "*أرسل كود لتحصيل الهدية .*"
        bot.edit_message_text(t,USER_ID,MSGID,parse_mode="markdown")
        bot.register_next_step_handler_by_chat_id(USER_ID,Code,MSGID,USER_ID)
      # - - Call Of Join Channels - - 
      if call.data == "Channels" :
        Soon(USER_ID,MSGID,USER_POINTS) 
      # - - Call Of Buy Points - - 
      if call.data == "Paypoints" :
        PayPoints(USER_ID,MSGID,USER_POINTS) 
      # - - |  | - - 


# - - SET LINK - - 
def SETORDERLINK(message,USER_ID) :
  spil = message.text.split(" ")
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM orders WHERE order_code='{spil[0]}' LIMIT 1")
  ORDER_INFO = con.fetchone()
  if ORDER_INFO != None :
    ORDER_CODE = ORDER_INFO[1]
    ORDER_USER_ID = ORDER_INFO[2]
    ORDER_NAME = ORDER_INFO[3]
    ORDER_NUM = ORDER_INFO[4]
    ORDER_PRICE = ORDER_INFO[5]
    ORDER_URL = ORDER_INFO[6]
    ORDER_STATUSE = ORDER_INFO[7]
    ORDER_DATE = ORDER_INFO[8]
    con.execute(F"UPDATE orders SET url='{spil[1]}' WHERE order_code='{spil[0]}' ")
    conn.commit()
    key = InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton(text=F"📮 ¦ الإستفسار عن الطلب أعلاه .",url=F"https://t.me/devalsh?text=بخصوص الطلب :`{ORDER_CODE}`, \n\n")
    key.add(a1)
    T = F"*تم حفظ الرابط بنجاح .*"
    bot.send_message(USER_ID,T,parse_mode='markdown')
    TT = F"*تحديث الطلب :*\n🎟 *¦* كود الطلب :- `{spil[0]}` . \n🏷 *¦*  السلعة :- *{ORDER_NUM}* - *{ORDER_NAME}* . \n⛓ *¦* الرابط :- `{spil[1]}`\n📍 *¦* حالة الطلب :- *{ORDER_STATUSE}* . \n"
    bot.send_message(ORDER_USER_ID,TT,parse_mode='markdown',reply_markup=key)
    bot.reply_to(message,text="*تم تحديث رابط الطلب بنجاح .*",parse_mode='markdown')

# - - Buyed dOrders - - 
def BuyedOrders(USER_ID,MSGID) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM orders WHERE USER='{USER_ID}'")
  ORDERS = con.fetchall()
  ALIORDERS_MSG = "*~ الطلبات التي تم شرائها :\n*"
  ALIORDERS_NUM = 0
  for i in ORDERS:
    if i[7] == "ملغي" :
      ALIORDERS_MSG += f"\n🎟 ¦ كود الطلب :- `{i[1]}`"
      ALIORDERS_MSG += f"\n🎫 ¦ الطلب :- *{i[4]} - {i[3]}*"
      ALIORDERS_MSG += f"\n💰 ¦ السعر :- *{i[5]}*"
      ALIORDERS_MSG += f"\n📍 ¦ حالة الطلب :- *{i[7]}*"
      ALIORDERS_MSG += f"\n⁉️ ¦ سبب الإلغاء :- *{i[9]}*"
      ALIORDERS_MSG += f"\n🕑 ¦ تاريخ الشراء :- *{i[8]}*"
      ALIORDERS_MSG += F"\n*  ـ ــ ـ ـ ـــــــــــــــــ «» ـــــــــــــــــ ــ ـ  ـ ـ*"
      ALIORDERS_NUM+=1
    else :
      ALIORDERS_MSG += f"\n🎟 ¦ كود الطلب :- `{i[1]}`"
      ALIORDERS_MSG += f"\n🎫 ¦ الطلب :- *{i[4]} - {i[3]}*"
      ALIORDERS_MSG += f"\n💰 ¦ السعر :- *{i[5]}*"
      ALIORDERS_MSG += f"\n📍 ¦ حالة الطلب :- *{i[7]}*"
      ALIORDERS_MSG += f"\n🕑 ¦ تاريخ الشراء :- *{i[8]}*"
      ALIORDERS_MSG += F"\n*  ـ ــ ـ ـ ـــــــــــــــــ «» ـــــــــــــــــ ــ ـ  ـ ـ*"
      ALIORDERS_NUM+=1
  ALIORDERS_MSG += F"\n\n🔢 ¦ عدد طلباتك :- *{ALIORDERS_NUM} .*"
  key = InlineKeyboardMarkup()
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
  key.add(aa)
  bot.edit_message_text(ALIORDERS_MSG,USER_ID,MSGID,parse_mode="Markdown",reply_markup=key)

# - - Add Link To Order - - 
def AddLinkToOrder(message,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT,ORDER_CODE) :
  Order_link = message.text
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM orders WHERE order_code='{ORDER_CODE}' LIMIT 1")
  ORDER_INFO = con.fetchone()
  con.execute(F"SELECT * FROM users WHERE tele_id='{int(ORDER_INFO[2])}' LIMIT 1")
  USER_INFO = con.fetchone()
  if ORDER_INFO != None :
    ORDER_CODE = ORDER_INFO[1]
    ORDER_USER_ID = ORDER_INFO[2]
    ORDER_NAME = ORDER_INFO[3]
    ORDER_NUM = ORDER_INFO[4]
    ORDER_PRICE = ORDER_INFO[5]
    ORDER_URL = ORDER_INFO[6]
    ORDER_STATUSE = ORDER_INFO[7]
    ORDER_DATE = ORDER_INFO[8]
    con.execute(F"UPDATE orders SET url='{str(Order_link)}' WHERE order_code='{ORDER_CODE}' ")
    conn.commit()
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    if ORDER_STATUSE == "ملغي" :
      key = InlineKeyboardMarkup()
    elif ORDER_STATUSE == "تحت المعالجة" :
      key = InlineKeyboardMarkup()
      a1 = types.InlineKeyboardButton(text=F"❌ ¦ إلغاء الطلب .",callback_data=F"CancelOrderCouse {ORDER_CODE}")
      a2 = types.InlineKeyboardButton(text=F"✅ ¦ التحديث إلى جاري العمل .",callback_data=F"AcceptOrder {ORDER_CODE}")
      a3 = types.InlineKeyboardButton(text=F"🔗 ¦ إضافة رابط .",callback_data=F"AddLink {ORDER_CODE}")
      key.add(a1)
      key.add(a2)
      key.add(a3)
    else :
      key = InlineKeyboardMarkup()
      a1 = types.InlineKeyboardButton(text=F"❌ ¦ إلغاء الطلب .",callback_data=F"CancelOrderCouse {ORDER_CODE}")
      a2 = types.InlineKeyboardButton(text=F"✅ ¦ التحديث إلى مكتمل .",callback_data=F"CompletedOrder {ORDER_CODE}")
      a3 = types.InlineKeyboardButton(text=F"🔗 ¦ تعديل الرابط .",callback_data=F"AddLink {ORDER_CODE}")
      key.add(a1)
      key.add(a2)
      key.add(a3)
    T = F"*NEW ORDER :*\n*                  <--------------->*\nكود الطلب : `{ORDER_CODE}`\nالطلب : *{ORDER_NAME}*\nالعدد : *{ORDER_NUM}*\nالسعر : *{ORDER_PRICE}*\nالرابط : `{Order_link}`\nحالة الطلب : *{ORDER_STATUSE}*\nالتوقيت : *{ORDER_DATE}*\n*                  <--------------->*\nمعلومات المستخدم :\nالاسم : {USER_INFO[3]}\nايديه : `{USER_INFO[2]}`\nيوزره : *@{USER_INFO[1]}*\nعدد نقاطه : *{USER_INFO[6]}*"
    bot.edit_message_text(T,ORDERS_CHANNEL,MSGID,parse_mode='markdown',reply_markup=key)
    key = InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton(text=F"📮 ¦ الإستفسار عن الطلب أعلاه .",url=F"https://t.me/devalsh?text=بخصوص الطلب :`{ORDER_CODE}`, \n\n")
    key.add(a1)
    TT = F"*تحديث الطلب :*\n🎟 *¦* كود الطلب :- `{ORDER_CODE}` . \n🏷 *¦*  السلعة :- *{ORDER_NUM}* - *{ORDER_NAME}* .\n⛓ *¦* الرابط :- `{Order_link}` \n📍 *¦* حالة الطلب :- *{ORDER_STATUSE}* ."
    bot.send_message(USER_INFO[2],TT,parse_mode='markdown',reply_markup=key)
    bot.reply_to(message,text="*تم تحديث رابط الطلب بنجاح .*",parse_mode='markdown')

# - - Cancel Couse - - 
def CancelCouse(message,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT,ORDER_CODE) :
  CancelCouse = message.text

  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM orders WHERE order_code='{ORDER_CODE}' LIMIT 1")
  ORDER_INFO = con.fetchone()
  con.execute(F"SELECT * FROM users WHERE tele_id='{int(ORDER_INFO[2])}' LIMIT 1")
  USER_INFO = con.fetchone()
  if ORDER_INFO != None :
    ORDER_CODE = ORDER_INFO[1]
    ORDER_USER_ID = ORDER_INFO[2]
    ORDER_NAME = ORDER_INFO[3]
    ORDER_NUM = ORDER_INFO[4]
    ORDER_PRICE = ORDER_INFO[5]
    ORDER_URL = ORDER_INFO[6]
    ORDER_STATUSE = ORDER_INFO[7]
    ORDER_DATE = ORDER_INFO[8]
    NEW_STATUSE = "ملغي"
    con.execute(F"UPDATE orders SET cancel_cous='{str(CancelCouse)}' WHERE order_code='{ORDER_CODE}' ")
    conn.commit()
  CancelCouse = message.text
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  T = F"*NEW ORDER :*\n*                  <--------------->*\nكود الطلب : `{ORDER_CODE}`\nالطلب : *{ORDER_NAME}*\nالعدد : *{ORDER_NUM}*\nالسعر : *{ORDER_PRICE}*\nالرابط : `{ORDER_URL}`\nحالة الطلب : *{NEW_STATUSE}*\nسبب الالغاء : *{CancelCouse}*\nالتوقيت : *{ORDER_DATE}*\n*                  <--------------->*\nمعلومات المستخدم :\nالاسم : {USER_INFO[3]}\nايديه : `{USER_INFO[2]}`\nيوزره : *@{USER_INFO[1]}*\nعدد نقاطه : *{USER_INFO[6]}*"
  bot.edit_message_text(T,ORDERS_CHANNEL,MSGID,parse_mode='markdown')
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"📮 ¦ الإستفسار عن الطلب أعلاه .",url=F"https://t.me/devalsh?text=بخصوص الطلب :`{ORDER_CODE}`, \n\n")
  key.add(a1)
  TT = F"*تحديث الطلب :*\n🎟 *¦* كود الطلب :- `{ORDER_CODE}` . \n🏷 *¦*  السلعة :- *{ORDER_NUM}* - *{ORDER_NAME}* .\n⛓ *¦* الرابط :- `{ORDER_URL}` \n📍 *¦* حالة الطلب :- *{NEW_STATUSE}* . \n⁉️ *¦* سبب الإلغاء :- *{CancelCouse}*"
  bot.send_message(USER_INFO[2],TT,parse_mode='markdown',reply_markup=key)
  bot.reply_to(message,text="*تم الغاء الطلب بنجاح .*",parse_mode='markdown')

# - - SET BOT EDITING - - 
def SetBotEditing(USER_ID,MSGID) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT tele_id FROM users")
  USERS = con.fetchall()
  for i in USERS :
    try :
      conn = sqlite3.connect("DBIQ.DB")
      con = conn.cursor()
      con.execute(F"UPDATE users SET bot_sat='Editing' WHERE tele_id='{i}' ")
      conn.commit()
    except :
      continue
  key = InlineKeyboardMarkup()
  aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
  key.add(aa)
  T = F"*تم تفعيل البوت .*"
  bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)

# - - SET BOT ACTIVE - - 
def SetBotActive(USER_ID,MSGID) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT tele_id FROM users ")
  USERS = con.fetchall()
  for i in USERS :
    try :
      conn = sqlite3.connect("DBIQ.DB")
      con = conn.cursor()
      con.execute(F"UPDATE users SET bot_sat='Active' WHERE tele_id='{i}' ")
      conn.commit()
    except :
      continue
  key = InlineKeyboardMarkup()
  aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
  key.add(aa)
  T = F"*تم تفعيل وضع الصيانة .*"
  bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)

# - - BOT SAT - - 
def BotSat(USER_ID,MSGID) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='0' ")
  gg = con.fetchone()
  BOT_SAT = gg[13]
  if BOT_SAT == "Active" :
    key = InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton(text="مفعل ✅.",callback_data="SetBotActive")
    a2 = types.InlineKeyboardButton(text="تفعيل وضع الصيانه .",callback_data="SetBotEditing")
    aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
    key.add(a1)
    key.add(a2)
    key.add(aa)
    T = F"*حالة البوت الان : مفعل .*"
    bot.send_message(USER_ID,T,parse_mode='markdown',reply_markup=key)
  elif BOT_SAT == 'Editing' :
    key = InlineKeyboardMarkup()
    a1 = types.InlineKeyboardButton(text="تفعيل البوت .",callback_data="SetBotActive")
    a2 = types.InlineKeyboardButton(text="وضع الصيانه ✅.",callback_data="SetBotEditing")
    aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
    key.add(a1)
    key.add(a2)
    key.add(aa)
    T = F"*حالة البوت الان : في وضع الصيانه .*"
    bot.send_message(USER_ID,T,parse_mode='markdown',reply_markup=key)

# - - AddAdmin - - 
def AddAdmin(message) :
  USER_ID = message.from_user.id
  USER_FIRSTNAME = message.from_user.first_name 
  USER_LASTNAME = message.from_user.last_name 
  USER_USERNAME = message.from_user.username
  USER_LINK = F"[{USER_FIRSTNAME}](tg://openmessage?user_id={USER_ID})"
  NEWADMIN = message.text
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{NEWADMIN}'")
  USER_INFO = con.fetchone()
  if USER_INFO !=None :
    con.execute(F"UPDATE users SET sat='Admin' WHERE tele_id='{NEWADMIN}' ")
    conn.commit()
    T = F"*تم رفعه ادمن .*"
    key = InlineKeyboardMarkup()
    aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
    key.add(aa)
    bot.reply_to(message,T,parse_mode='markdown',reply_markup=key)
    T = F"*تم رفع رتبتك الى أدمن بواسطة * {USER_LINK}"
    bot.send_message(NEWADMIN,T,parse_mode='markdown')
  else :
    T = F"*لم يتم العثور على المستخدم .*"
    key = InlineKeyboardMarkup()
    aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
    key.add(aa)
    bot.reply_to(message,T,parse_mode='markdown',reply_markup=key)

# - - CollectPoints - -
def collectpoints(USER_ID,MSGID) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' ")
  result = con.fetchone()
  USER_LINK_SHARE = result[7]
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"🎁 ⫶ الهدية اليومية .",callback_data="Dilygift")
  a2 = types.InlineKeyboardButton(text="💳 ⫶ إستخدام رمز .",callback_data="Code")
  a3 = types.InlineKeyboardButton(text="👾 ⫶ أنضمام الى قنوات .",callback_data="Channels")
  a5 = types.InlineKeyboardButton(text="🔙 ⫶ رجوع .",callback_data="BTS")
  key.add(a1)
  key.add(a2,a3)
  key.add(a5)
  T = F'''
اضغط على الرابط ثم قم بمشاركته مع اصدقائك 📥 . 

- كل شخص يقوم بالدخول ستحصل على *{INVITE}* {CURNNCY} 📊 .

- بإمكانك عمل اعلان خاص برابط الدعوة الخاص بك 📬 .

~ رابط الدعوة :\n `https://{BOT_LINK}?start={USER_ID}`

*- أضغط على الرابط للنسخ .*

- *مشاركتك للرابط : {USER_LINK_SHARE}* 🌀

'''
  #conn = sqlite3.connect("DBIQ.DB")
  #con = conn.cursor()
  #con.execute(F"SELECT * FROM users WHERE link_share='{USER_ID}' ")
  #TREND_SHARE = con.fetchone()
  #for i in TREND_SHARE :
  #  TREND_SHARE_ID = TREND_SHARE[2]
  #  TREND_SHARE_NUM = TREND_SHARE[6]
  bot.edit_message_text(T,USER_ID,MSGID,disable_web_page_preview=True,parse_mode="markdown",reply_markup=key)

# - - PAY POINTS - - 
def PayPoints(USER_ID,MSGID,USER_POINTS) :
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"الدعم .",url="http://t.me/DevAlsH")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
  key.add(a1)
  key.add(aa)
  T = F"""
*🟡 اسعار شحن نقاط بوت  {BOT_NAME} ❤️

ـ 1$ ~> 1,000 {CURNNCY}
ـ 2$ ~> 2,000 {CURNNCY}
ـ 3$ ~> 3,000 {CURNNCY}
ـ 4$ ~> 4,000 {CURNNCY}
ـ 5$ ~> 5,000 {CURNNCY}
ـ 10$ ~> 10,000 {CURNNCY}
ـ 20$ ~> 20,000 {CURNNCY}
- يوجد شحن جميع الكميات .
     ـ ــ ـ ـ ـــــــــــــــــ «» ـــــــــــــــــ ــ ـ  ـ ـ   
•  طرق الدفع : 🌐
( أسياسيل - زين كاش - FIB - ماستر كارد ).*

*🤖 ┆ {BOT_NAME} :* {BOT}
*🔎 ┆ الـدعم الفني :* @DevAlsH
*📊 ┆ قـنـاة البــوت :* @khdmatyUp
"""
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode="markdown",reply_markup=key)

# - - ORDER INFO - - 
def OrderInfo(message,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT) :
  ORDER_CODE = message.text
  USER_IS_PREMUIM = message.from_user.is_premium
  if ORDER_CODE == "🚫 ⫶ إلغاء ." :
    Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
    return
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM orders WHERE order_code='{ORDER_CODE}' LIMIT 1")
  check = con.fetchone()
  if check != None :
    if USER_ID == check[2] :
      key = InlineKeyboardMarkup()
      aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
      key.add(aa)
      T = F"*Doneeeeeeeeee !*"
      bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)
    else :
      key = InlineKeyboardMarkup()
      aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
      key.add(aa)
      T = F"*الطلب ليس لك لتستعلم معلوماته !*"
      bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)
  else :
    key = InlineKeyboardMarkup()
    aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
    key.add(aa)
    T = F"*الطلب غير موجود في البوت !*"
    bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)

# - - SETTINGS - -
def Settings(USER_ID,MSGID) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' ")
  T = F"*الإعدادات .*"
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"☎️︙الدعم .",url="https://t.me/DevAlsH")
  a2 = types.InlineKeyboardButton(text=F"🌍 ⫶ اللغة .",callback_data="lang")
  a2 = types.InlineKeyboardButton(text=F"ℹ️ ⫶ شروط الإستخدام .",callback_data="UsingInfo")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
  key.add(a1)
  key.add(a2)
  key.add(aa)
  bot.edit_message_text(T,USER_ID,message_id=MSGID,parse_mode="Markdown",reply_markup=key)

# - - ACCOUNT - -
def Account(USER_ID,MSGID) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' ")
  result = con.fetchone()
  USER_USERNAME = result[1]
  USER_FNAME = result[3]
  USER_LNAME = result[4]
  USER_LANGUAGE = result[5]
  USER_POINTS = result[6]
  USER_LINK_SHARE = result[7]
  USER_DEPOSIT = result[8]
  USER_STATUSE = result[9]
  USER_SAT = result[10]
  USER_MANY_GIFTS = result[12]
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"♻️ ¦ الطلبات التي تم شرائها .",callback_data="BuyedOrders")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
  key.add(a1)
  key.add(aa)
  if USER_LNAME == "None" :
    USER_LNAME = ""
  if USER_USERNAME == "None" :
    USER_USERNAME = "لايوجد"
  else :
    USER_USERNAME = F"@{USER_USERNAME}"
  T = F"""
*جميع معلومات حسابك داخل البوت :*

▪︎* معلومات الحساب :*
• * نقاطك :* {USER_POINTS} .
• *الإسم الكامل :* {USER_FNAME} {USER_LNAME} .
• * اليوزر :* {USER_USERNAME} .
• * الآيدي :* `{USER_ID}` .
• * الرتبة :* {USER_SAT} .
• * حالة الحساب الأن :* {USER_STATUSE} .
• * مشاركاتك للرابط الخاص بك :* {USER_LINK_SHARE} .
• * عدد الهدايا اليومية المستلمة :* {USER_MANY_GIFTS} .
• * أنفقت في البوت :* {USER_DEPOSIT} .
  """
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode="Markdown",disable_web_page_preview=True,reply_markup=key)

# - - CODE - - 
def Code(message,MSGID,USER_ID) :
  USER_IS_PREMUIM = message.from_user.is_premium
  CODE = message.text
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' LIMIT 1")
  USER_INFO = con.fetchone()
  USER_USERNAME = USER_INFO[2]
  USER_FIRSTNAME = USER_INFO[3]
  USER_LASTNAME = USER_INFO[4]
  USER_LANGUAGE = USER_INFO[5]
  USER_POINTS = USER_INFO[6]
  USER_LINK_SHSARE = USER_INFO[7]
  USER_SAT = USER_INFO[10]
  BOT_SAT = USER_INFO[13]
  try :
    if CODE == "🚫 ⫶ إلغاء ." :
      Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
    else :
      conn = sqlite3.connect("DBIQ.DB")
      con = conn.cursor()
      con.execute(F"SELECT * FROM codes WHERE code='{CODE}' ")
      CODE_INFO = con.fetchone()
      if CODE_INFO == None :
        key = InlineKeyboardMarkup()
        aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
        key.add(aa)
        T = F"*الكود خاطئ !*"
        bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)
      elif CODE == CODE_INFO[1] :
        CODE_USE = CODE_INFO[3]
        CODE_ID = CODE_INFO[0]
        if int(CODE_USE) > int(0) :
          CODE_POINTS = CODE_INFO[2]
          NEW_USER_POINTS = int(USER_POINTS) + int(CODE_POINTS)
          NEW_USE_CODE = int(CODE_USE) - int(1)
          con.execute(F"UPDATE users SET points='{NEW_USER_POINTS}' WHERE tele_id='{USER_ID}'")
          conn.commit()
          con.execute(F"UPDATE codes SET use='{NEW_USE_CODE}' WHERE id='{CODE_ID}'")
          conn.commit()
          key = InlineKeyboardMarkup()
          aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
          key.add(aa)
          T = F"لقد حصلت على *{CODE_POINTS}* من الكود `{CODE_INFO[1]}` بنجاح ."
          bot.send_message(USER_ID,T,parse_mode="Markdown",reply_markup=key)
        else :
          key = InlineKeyboardMarkup()
          aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
          key.add(aa)
          T = F"*تم الوصول الى الحد الاقصى لاستعمال هذا الكود !*"
          bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)

  except :
    Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)

# - - OFFERS - - 
def Offers(USER_ID,MSGID) :
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"أسياسيل .",callback_data="Asiasell")
  a2 = types.InlineKeyboardButton(text=F"زين كاش .",callback_data="Zaincash")
  a4 = types.InlineKeyboardButton(text=F"مصرف العراق الاول .",callback_data="FIB")
  a6 = types.InlineKeyboardButton(text=F"ماستر كارد .",callback_data="MasterCard")
  a7 = types.InlineKeyboardButton(text=F"انستجرام .",callback_data="Instagram")
  a8 = types.InlineKeyboardButton(text=F"تليجرام .",callback_data="Tele")
  a9 = types.InlineKeyboardButton(text=F"تيك توك .",callback_data="Tik")
  a10 = types.InlineKeyboardButton(text=F"ببجي موبايل .",callback_data="Pubg")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
  key.add(a1,a2)
  key.add(a4,a6)
  key.add(a7,a8,a9)
  key.add(a10)
  key.add(aa)
  T = F"*أختر ما تريد أستبداله بنقاطك :*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode="markdown",reply_markup=key)

# - - SUCSSES CAST - - 
def checkcast(message) :
  Y = message.message_id
  keyboard = telebot.types.ReplyKeyboardMarkup(True)
  keyboard.row(F'نشر .','لا .')
  T = F"*هل تريد نشر هذا ؟*"
  e = bot.reply_to(message,T,parse_mode="markdown",reply_markup=keyboard,disable_web_page_preview=True)
  bot.register_next_step_handler(e, brodcast,Y)

# - - SEND CAST - - 
def brodcast(message,Y):
  if message.text == "نشر ." :
    conn = sqlite3.connect("DBIQ.DB")
    con = conn.cursor()
    con.execute(F"SELECT tele_id FROM users WHERE statuse='Active' ")
    ids = con.fetchall()
    how = 0
    for i in ids:
      try:
        bot.copy_message(chat_id=i, from_chat_id=message.chat.id, message_id=Y,parse_mode='markdown')
        how+=1
      except:
        continue
    key = InlineKeyboardMarkup()
    aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
    key.add(aa)
    bot.reply_to(message, f'تمت بنجاح.\nتم الارسال لـ*{how}* مستخدم .',parse_mode='markdown',reply_markup=key)
  else :
    key = InlineKeyboardMarkup()
    aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
    key.add(aa)
    T = F"* تم الغاء العملية *"
    bot.reply_to(message,T,parse_mode='markdown',reply_markup=key)

# - - BOT INFO - - 
def Bot_Info(USER_ID,MSGID) :
  All_USERS = 0
  Banded_USERS = 0
  ADMIN_USERS = 0
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT id FROM users")
  ids = con.fetchall()
  for i in ids:
    All_USERS+=1
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT id FROM users WHERE statuse='Banded' ")
  ids = con.fetchall()
  for e in ids:
    Banded_USERS+=1
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT id FROM users WHERE sat='Admin' ")
  ids = con.fetchall()
  for e in ids:
    ADMIN_USERS+=1
  T = F"""
  *مرحبًا بك في قسم الإحصائيات 📊*

*• المستخدمون:*

- العدد الإجمالي للمستخدمين :  *{All_USERS}* .
- عدد القنوات والمجموعات : *Soon* .
- عدد المحظورين : *{Banded_USERS}* .
- عدد الادمنيه : *{ADMIN_USERS}* .

  """
  key = InlineKeyboardMarkup()
  aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
  key.add(aa)
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - BOT ADMINS - - 
def Bot_Admins(USER_ID,MSGID) :
  admin = 0
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE sat='Admin' ")
  admin_info = con.fetchall()
  for i in admin_info :
    admin_id = admin_info[int(F"{admin}")][1] # ايدي الادمن .
    admin_name = admin_info[int(F"{admin}")][3] # اسم الادمن .
    admin+= 1
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"{admin_name}",url=F"tg://openmessage?user_id={admin_id}")
  a2 = types.InlineKeyboardButton(text=F"🗑",callback_data=F"SET_USER_{admin_id}")
  a3 = types.InlineKeyboardButton(text=F"اضافة ادمن",callback_data=F"AddAdmin")
  aa = types.InlineKeyboardButton(text="رجوع",callback_data="AdminsBACK")
  key.add(a1,a2)
  key.add(a3)
  key.add(aa)
  sleep(0.2)
  T = """
  مرحبا بك في قسم الادمنيه :\n\n

  """
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - ASIASELL - -
def DrawlAsia(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='أسياسيل'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  aName = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  aPrice = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTO")
  key.add(aName,aPrice)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت أسياسيل ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - ZAINCASH - -
def DrawlZain(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='زين العراق'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTO")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت زين العراق ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - FIB - - 
def DrawlFIB(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='مصرف العراق الاول'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTO")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت مصرف العراق لاول ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - MasterCard - -
def DrawlMasterCard(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='ماستر كارد'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTO")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت ماستر كارد ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - Choese Instagram - - 
def ChoeseInstagram(USER_ID,MSGID,USER_POINTS) :
  key = InlineKeyboardMarkup()
  a7 = types.InlineKeyboardButton(text=F"👥 ⫶ متابعين .",callback_data="InstagramFollowers")
  a9 = types.InlineKeyboardButton(text=F"👁 ⫶ مشاهدات .",callback_data="InstagramVeiows")
  a8 = types.InlineKeyboardButton(text=F"❤️ ⫶ لايكات .",callback_data="InstagramLikes")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTO")
  key.add(a7)
  key.add(a9,a8)
  key.add(aa)
  T = F"*أختر ما تريد زيادته من الازرار ادناه .*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - Instagram Followers - -
def InstagramFollowers(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='متابع انستا'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Instagram")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت متابعين انستا ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - Instagram Veiows - - 
def InstagramVeiows(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='مشاهدة انستا'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Instagram")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت مشاهدات انستا ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - Instagram Likes - - 
def InstagramLikes(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='لايكات انستا'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Instagram")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت لايكات انستا ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - Choese TikTok - - 
def ChoeseTik(USER_ID,MSGID,USER_POINTS) :
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"👥 ⫶ متابعين .",callback_data="TikTokFollowers")
  a2 = types.InlineKeyboardButton(text=F"👁 ⫶ مشاهدات .",callback_data="TikTokVeiows")
  a3 = types.InlineKeyboardButton(text=F"❤️ ⫶ لايكات .",callback_data="TikLikes")
  a4 = types.InlineKeyboardButton(text=F"⤴️ ⫶ أكسبلور .",callback_data="TikShares")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTO")
  key.add(a1)
  key.add(a2,a3)
  key.add(a4)
  key.add(aa)
  T = F"*أختر ما تريد زيادته من الازرار ادناه .*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - TikTok Followers - - 
def TikTokFollowers(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='متابع تيك توك'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Tik")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت متابعين تيك توك ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - TikTok Veiows - - 
def TikTokVeiows(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='مشاهدات تيك توك'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Tik")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت مشاهدات تيك توك ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - TikTok Shares - - 
def TikShares(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='مشاركات تيك توك'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Tik")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت اكسبلور تيك توك ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - TikTok Likes - - 
def TikLikes(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='لايكات تيك توك'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Tik")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت لايكات تيك توك ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - Choese Tele - - 
def ChoeseTle(USER_ID,MSGID) :
  key = InlineKeyboardMarkup()
  a1 = types.InlineKeyboardButton(text=F"👥 ⫶ مشتركين .",callback_data="TelegramFollowers")
  a2 = types.InlineKeyboardButton(text=F"👁 ⫶ مشاهدات .",callback_data="TelegramVeiows")
  a3 = types.InlineKeyboardButton(text=F"❤️ ⫶ لايكات .",callback_data="TelegramLikes")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTO")
  key.add(a1)
  key.add(a2,a3)
  key.add(aa)
  T = F"*أختر ما تريد زيادته من الازرار ادناه .*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - TELEGRAM FOLLOWERS  - -
def TelegramFollowers(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='مشترك تلي'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Tele")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت مشتركين تلي ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - TELEGRAM VEIOWS  - -
def TelegramVeiows(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='مشاهدات تلي'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Tele")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت مشاهدات تلي ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - TELEGRAM LIKES  - -
def TelegramLikes(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='لايكات تلي'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="Tele")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت لايكات تلي ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - PUBG - - 
def Pubg(USER_ID,MSGID,USER_POINTS) :
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM products WHERE prod_name='شدة'")
  PROD_INFO = con.fetchall()
  key = InlineKeyboardMarkup()
  Name = types.InlineKeyboardButton(text=F"الكمية .",callback_data="None")
  Price = types.InlineKeyboardButton(text=F"السعر .",callback_data="None")
  a1 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][4]}",callback_data=F"{PROD_INFO[0][1]}")
  a3 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][4]}",callback_data=F"{PROD_INFO[1][1]}")
  a5 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][4]}",callback_data=F"{PROD_INFO[2][1]}")
  a7 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][4]}",callback_data=F"{PROD_INFO[3][1]}")
  a9 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][4]}",callback_data=F"{PROD_INFO[4][1]}")
  a2 = types.InlineKeyboardButton(text=F"{PROD_INFO[0][3]}",callback_data=F"{PROD_INFO[0][1]}")
  a4 = types.InlineKeyboardButton(text=F"{PROD_INFO[1][3]}",callback_data=F"{PROD_INFO[1][1]}")
  a6 = types.InlineKeyboardButton(text=F"{PROD_INFO[2][3]}",callback_data=F"{PROD_INFO[2][1]}")
  a8 = types.InlineKeyboardButton(text=F"{PROD_INFO[3][3]}",callback_data=F"{PROD_INFO[3][1]}")
  a10 = types.InlineKeyboardButton(text=F"{PROD_INFO[4][3]}",callback_data=F"{PROD_INFO[4][1]}")
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTO")
  key.add(Name,Price)
  key.add(a1,a2)
  key.add(a3,a4)
  key.add(a5,a6)
  key.add(a7,a8)
  key.add(a9,a10)
  key.add(aa)
  T = F"*لقد أخترت شدات ببجي ,*\n*الان أختر الكمية التي تريدها :*\n*عدد نقاطك {USER_POINTS}*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode='markdown',reply_markup=key)

# - - TRANS POINTS - - 
def TransPoints(message,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT) :
  TransTo_ID = message.text
  USER_IS_PREMUIM = message.from_user.is_premium
  if TransTo_ID == "🚫 ⫶ إلغاء ." :
    Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
    return
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{TransTo_ID}' LIMIT 1")
  check = con.fetchone()
  if check != None :
    USER_REPLAY_POINTS = check[6]
    try :
      float(TransTo_ID)
      if int(TransTo_ID) == int(USER_ID) :
        key = InlineKeyboardMarkup()
        aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
        key.add(aa)
        T = F"*لايمكنك التحويل الى نفسك !*"
        bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)
      elif check :
        bot.send_message(USER_ID,"*- أرسل عدد النقاط التي تريد تحويلها :*",parse_mode='markdown',disable_web_page_preview=True)
        bot.register_next_step_handler(message,ReplayPoints2,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT,TransTo_ID,USER_REPLAY_POINTS)
      else :
        key = InlineKeyboardMarkup()
        aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
        key.add(aa)
        T = F"*المستخدم غير موجود في البوت !*"
        bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)
    except :
        key = InlineKeyboardMarkup()
        aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
        key.add(aa)
        T = F"*يرجى إرسال ارقام فقط !*"
        bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)
  else :
    key = InlineKeyboardMarkup()
    aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
    key.add(aa)
    T = F"*المستخدم غير موجود في البوت !*"
    bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)

# - - REPLAY POINTS 2 - - 
def ReplayPoints2(message,USER_ID,MSGID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,BOT_SAT,TransTo_ID,USER_REPLAY_POINTS) :
  Many_POINTS = message.text
  USER_IS_PREMUIM = message.from_user.is_premium
  USER_LINK = F"[{USER_FIRSTNAME}](tg://openmessage?user_id={USER_ID})"
  TRANS_TO_LINK = F"[{TransTo_ID}](tg://openmessage?user_id={TransTo_ID})"
  conn = sqlite3.connect("DBIQ.DB")
  con = conn.cursor()
  con.execute(F"SELECT * FROM users WHERE tele_id='{USER_ID}' LIMIT 1")
  check = con.fetchone()
  USER_POINTS = check[6]
  
  
  if TransTo_ID == "🚫 ⫶ إلغاء ." :
    Start(USER_ID,USER_USERNAME,USER_FIRSTNAME,USER_LASTNAME,MSGID,BOT_SAT,USER_IS_PREMUIM)
    return
  try : 
    float(Many_POINTS)
    a = int(Many_POINTS) + int(REPLAY)
    New_user_points = int(USER_POINTS) - int(a)
    New_trans_to_points = int(USER_REPLAY_POINTS) + int(Many_POINTS) 
    if int(Many_POINTS) <= int(0) :
      key = InlineKeyboardMarkup()
      aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
      key.add(aa)
      T = F"*لا يمكن ارسال اقل من 1 نقطة !*"
      bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)
    elif int(USER_POINTS) >= int(a) :
      con.execute(F"UPDATE users SET points='{New_user_points}' WHERE tele_id='{USER_ID}'")
      conn.commit()
      con.execute(F"UPDATE users SET points='{New_trans_to_points}' WHERE tele_id='{TransTo_ID}'")
      conn.commit()
      T = F"""
*تمت عملية التحويل بنجاح ؛*

المستلم : {TRANS_TO_LINK}
عدد النقاط : {Many_POINTS}
عمولة التحويل : {REPLAY}

""" 
      TT = F"""
      تم إستلام *{Many_POINTS}* من {USER_LINK}

      أصبحت نقاطك : `{New_trans_to_points}`
      """
      TTT = F"""
      *تمت عملية تحويل ناجحة : *

      المرسل : {USER_LINK}
      عدد النقاط : {Many_POINTS}
      نقاطه الحالية : {New_user_points}

      المستلم : {TRANS_TO_LINK}
      عدد نقاطه : {New_trans_to_points}
      """
      bot.send_message(USER_ID,T,parse_mode="markdown")
      bot.send_message(TransTo_ID,TT,parse_mode="markdown")
      bot.send_message(CEO_ID,TTT,parse_mode="markdown")
    else :
      key = InlineKeyboardMarkup()
      aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
      key.add(aa)
      T = F"*لا تملك ما يكفي من النقاط !*"
      bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)
  except :
    T = F"*يرجى إرسال ارقام فقط !!!!*"
    bot.send_message(USER_ID,T,parse_mode="markdown",reply_markup=key)

# - - SOON - - 
def Soon(USER_ID,MSGID,USER_POINTS) :
  key = InlineKeyboardMarkup()
  aa = types.InlineKeyboardButton(text=F"🔙 ⫶ رجوع .",callback_data="BTS")
  key.add(aa)
  T = F"*قريبًا ...*"
  bot.edit_message_text(T,USER_ID,MSGID,parse_mode="markdown",reply_markup=key)











#PJZzTUUtKTgdA44



print("BOT IS ACTIVE !.")
bot.infinity_polling()