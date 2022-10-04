import random
import asyncio
from pyrogram import filters
from sarena import pbot

__mod_name__ = "𝚂ʜᴀʏʀɪ"

__help__ = """
*➻ ʟᴏᴠᴇ ꜱʜᴀʏʀɪ 💕*
⟳ /lucky - ꜱᴇɴᴅꜱ ꜱʜᴀʏʀɪ ( ʟᴏᴠᴇ )

*➻ ʀᴏᴍᴀɴᴛɪᴄ 💘*
⟳ /romantic - ʏᴏᴜ ᴋɴᴏᴡ 😁
"""


"""
    |----╒════════════╕----|
          |  Kang with credits |
          |----- Coded by: ----|
          |       @Cute_Boy701      |
          |----(2142595466)----|
          |      on telegram   |
    |----╘════════════╛----|
"""

ROMANTIC_STRINGS = [
    "Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...",
    "Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...",
    "Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...",
    "Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...",
    "Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...",
    "Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...",
    "Udas shamo me wo lout\nKar aana bhul jate hain..❤️\nKar ke khafa mujhko wo\nManana bhul jate hain....💞😌",
    "Chalo phir yeha se ghar kaise jaoge...?\n\n🙂🔪Ye humare akhri mulakat h kuch kehna chahoge?🙃❤️\n😔❤️M to khr khel rhi thi tum to sacha isq karte the na😓🔪\nKaise karte karke dekhau..😷🤧\n🤒❤️Tum to kehte the m bichrungi to mar jaooge marke dekhau😖❤️\n😌✨Ek bhola bhala khelta huya dil tut gyi na....🙂❤️\n👀❤️....Ladka chup kyu pata ..?\n😊❤️ ....ladki to margyi naa",
    "Toote huye dil ne bhi uske liye dua\n maangi,\nmeri har saans ne uske liye khushi\n maangi,\nna jaane kaisi dillagi thi uss bewafa se,\naakhiri khwahish mein bhi uski hi wafa maangi.........✍\n\n~ @ii_1444 ♡",
    "Main waqt ban jaaun tu ban jaana koi \nlamha, \nMain tujhnme gujar jaaun tu mujhme gujar \njana............✍ \n\n~ @ii_1444 ♡ 💘",
    "Udaas lamhon 😞 ki na koi yaad\nrakhna, \ntoofan mein bhi wajood apna sambhal\nRakhna,\nkisi ki zindagi ki khushi ho tum,\n🥰  bs yehi soch tum apna khayal\nRkhna,\n\n~ @ii_1444 ♡ 💘❤️",
]

LOVE_STRINGS = [
    "🦋 ख्वाब बनकर तेरी आंखों में समाना है,\nदवा बनकर तेरे हर दर्द को मिटाना है💕,\n💘हासिल हैं मुझे जमाने भर की खुशियां,\nमेरी हर खुशी को बस तुझ पर लुटाना है।🍷\n\n~ @ii_1444 💘",
    "💕 दिल में राज छुपा है दिखाऊं कैसे,\nहो गया है प्यार आपसे बताऊं कैसे🙂,\n🦋 दुनिया कहती है मत लिखो नाम दिल पर\nजो नाम है दिल में उसे मिटाऊं कैसे।❤️\n\n~ @ii_1444 💘",
    "👀 इन आँखों को जब तेरा दीदार हो जाता है…\nदिन कोई भी हो लेकिन त्यौहार हो जाता है 💕\n\n~ @ii_1444 🥀",
    "🥺 काश मैं पानी होता और तू प्यास होती,\nन मैं खफा होता और न तू उदास होती,🦋\n😫 जब भी तुम मेरी निगाहों से दूर होते,\nमैं तेरा नाम लेता और तू मेरे पास होती।❤️\n\n~ @ii_1444 🥀",
    "😍 मीठी मीठी यादें पलकों पे सजा लेना\nएक साथ गुजारे पल को दिल में बसा लेना 🥰\n🦋नजर न आऊं हकीकत में अगर,\nमुस्कुराकर मुझे सपनो में बुला लेना।🍷\n\n~ @ii_1444 🥀",
    "💘 कभी हंसाता है ये प्यार,\nकभी रुलाता है ये प्यार,🥺\n🥀 हर पल की याद दिलाता है ये प्यार,\nचाहो या न चाहो पर आपके होने का,🙂\nएहसास दिलाता है ये प्यार।🍷\n\n~ @ii_1444",
    "💞 अंदाजा मेरी मोहब्बत का\nसब लगा लेते हैं,🦋\n🍷 जब तुम्हारा नाम सुनकर\nहम मुस्कुरा देते हैं।😊\n\n~ @ii_1444 💘",
]


"""
    Hello kangers, 
    How are you all??
    So if you want to add more shyari add it between '', example 'Yes I'm kanging your codes', 
    I hope it's clear to you!

    So if you're really kanging this atleast don't remove this line it takes a lot of time to code things.
    Coded by : @Cute_Boy701 on telegram...
"""


@pbot.on_message(filters.command("romantic"))
async def lel(bot, message):
    ran = random.choice(ROMANTIC_STRINGS)
    await asyncio.sleep(1.0)
    return await message.reply_text(text=ran)

@pbot.on_message(filters.command("lucky"))
async def lel(bot, message):
    ran = random.choice(LOVE_STRINGS)
    await asyncio.sleep(1.0)
    return await message.reply_text(text=ran)

