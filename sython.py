 sython.start()
 c = requests.session()
 bot_username = '@KBKBOT'
 bot_username = '@zmmbot'
 bot_usernamee = '@A_MAN9300BOT'

 y = datetime.datetime.now().year
Expand Down
Expand Up	@@ -131,14 +131,14 @@ async def update(event):
 async def _(event):
         await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
         channel_entity = await sython.get_entity(bot_username)
         await sython.send_message('@KBKBOT', 'جاري التجميع بواسطة | SOMY TEAM')
         await sython.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
         channel_entity = await sython.get_entity(bot_username)
         await sython.send_message('@KBKBOT', '/start')
         await sython.send_message('@zmmbot', '/start')
         await asyncio.sleep(5)
         msg0 = await sython.get_messages('@KBKBOT', limit=1)
         msg0 = await sython.get_messages('@zmmbot', limit=1)
         await msg0[0].click(2)
         await asyncio.sleep(5)
         msg1 = await sython.get_messages('@KBKBOT', limit=1)
         msg1 = await sython.get_messages('@zmmbot', limit=1)
         await msg1[0].click(0)

         chs = 1
Expand All	@@ -159,7 +159,7 @@ async def _(event):
                 except:
                     bott = url.split('/')[-1]
                     await sython(ImportChatInviteRequest(bott))
                 msg2 = await sython.get_messages('@KBKBOT', limit=1)
                 msg2 = await sython.get_messages('@zmmbot', limit=1)
                 await msg2[0].click(text='تحقق')
                 chs += 1
