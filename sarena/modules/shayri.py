import random
import asyncio
from pyrogram import filters
from sarena import pbot

__mod_name__ = "πΚα΄ΚΚΙͺ"

__help__ = """
*β» Κα΄α΄ α΄ κ±Κα΄ΚΚΙͺ π*
β³ /lucky - κ±α΄Ι΄α΄κ± κ±Κα΄ΚΚΙͺ ( Κα΄α΄ α΄ )

*β» Κα΄α΄α΄Ι΄α΄Ιͺα΄ π*
β³ /romantic - Κα΄α΄ α΄Ι΄α΄α΄‘ π
"""


"""
    |----ββββββββββββββ----|
          |  Kang with credits |
          |----- Coded by: ----|
          |       @Cute_Boy701      |
          |----(2142595466)----|
          |      on telegram   |
    |----ββββββββββββββ----|
"""

ROMANTIC_STRINGS = [
    "Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...",
    "Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...",
    "Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...",
    "Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...",
    "Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...",
    "Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...",
    "Udas shamo me wo lout\nKar aana bhul jate hain..β€οΈ\nKar ke khafa mujhko wo\nManana bhul jate hain....ππ",
    "Chalo phir yeha se ghar kaise jaoge...?\n\nππͺYe humare akhri mulakat h kuch kehna chahoge?πβ€οΈ\nπβ€οΈM to khr khel rhi thi tum to sacha isq karte the naππͺ\nKaise karte karke dekhau..π·π€§\nπ€β€οΈTum to kehte the m bichrungi to mar jaooge marke dekhauπβ€οΈ\nπβ¨Ek bhola bhala khelta huya dil tut gyi na....πβ€οΈ\nπβ€οΈ....Ladka chup kyu pata ..?\nπβ€οΈ ....ladki to margyi naa",
    "Toote huye dil ne bhi uske liye dua\n maangi,\nmeri har saans ne uske liye khushi\n maangi,\nna jaane kaisi dillagi thi uss bewafa se,\naakhiri khwahish mein bhi uski hi wafa maangi.........β\n\n~ @ii_1444 β‘",
    "Main waqt ban jaaun tu ban jaana koi \nlamha, \nMain tujhnme gujar jaaun tu mujhme gujar \njana............β \n\n~ @ii_1444 β‘ π",
    "Udaas lamhon π ki na koi yaad\nrakhna, \ntoofan mein bhi wajood apna sambhal\nRakhna,\nkisi ki zindagi ki khushi ho tum,\nπ₯°  bs yehi soch tum apna khayal\nRkhna,\n\n~ @ii_1444 β‘ πβ€οΈ",
]

LOVE_STRINGS = [
    "π¦ ΰ€ΰ₯ΰ€΅ΰ€Ύΰ€¬ ΰ€¬ΰ€¨ΰ€ΰ€° ΰ€€ΰ₯ΰ€°ΰ₯ ΰ€ΰ€ΰ€ΰ₯ΰ€ ΰ€?ΰ₯ΰ€ ΰ€Έΰ€?ΰ€Ύΰ€¨ΰ€Ύ ΰ€Ήΰ₯,\nΰ€¦ΰ€΅ΰ€Ύ ΰ€¬ΰ€¨ΰ€ΰ€° ΰ€€ΰ₯ΰ€°ΰ₯ ΰ€Ήΰ€° ΰ€¦ΰ€°ΰ₯ΰ€¦ ΰ€ΰ₯ ΰ€?ΰ€Ώΰ€ΰ€Ύΰ€¨ΰ€Ύ ΰ€Ήΰ₯π,\nπΰ€Ήΰ€Ύΰ€Έΰ€Ώΰ€² ΰ€Ήΰ₯ΰ€ ΰ€?ΰ₯ΰ€ΰ₯ ΰ€ΰ€?ΰ€Ύΰ€¨ΰ₯ ΰ€­ΰ€° ΰ€ΰ₯ ΰ€ΰ₯ΰ€Άΰ€Ώΰ€―ΰ€Ύΰ€,\nΰ€?ΰ₯ΰ€°ΰ₯ ΰ€Ήΰ€° ΰ€ΰ₯ΰ€Άΰ₯ ΰ€ΰ₯ ΰ€¬ΰ€Έ ΰ€€ΰ₯ΰ€ ΰ€ͺΰ€° ΰ€²ΰ₯ΰ€ΰ€Ύΰ€¨ΰ€Ύ ΰ€Ήΰ₯ΰ₯€π·\n\n~ @ii_1444 π",
    "π ΰ€¦ΰ€Ώΰ€² ΰ€?ΰ₯ΰ€ ΰ€°ΰ€Ύΰ€ ΰ€ΰ₯ΰ€ͺΰ€Ύ ΰ€Ήΰ₯ ΰ€¦ΰ€Ώΰ€ΰ€Ύΰ€ΰ€ ΰ€ΰ₯ΰ€Έΰ₯,\nΰ€Ήΰ₯ ΰ€ΰ€―ΰ€Ύ ΰ€Ήΰ₯ ΰ€ͺΰ₯ΰ€―ΰ€Ύΰ€° ΰ€ΰ€ͺΰ€Έΰ₯ ΰ€¬ΰ€€ΰ€Ύΰ€ΰ€ ΰ€ΰ₯ΰ€Έΰ₯π,\nπ¦ ΰ€¦ΰ₯ΰ€¨ΰ€Ώΰ€―ΰ€Ύ ΰ€ΰ€Ήΰ€€ΰ₯ ΰ€Ήΰ₯ ΰ€?ΰ€€ ΰ€²ΰ€Ώΰ€ΰ₯ ΰ€¨ΰ€Ύΰ€? ΰ€¦ΰ€Ώΰ€² ΰ€ͺΰ€°\nΰ€ΰ₯ ΰ€¨ΰ€Ύΰ€? ΰ€Ήΰ₯ ΰ€¦ΰ€Ώΰ€² ΰ€?ΰ₯ΰ€ ΰ€ΰ€Έΰ₯ ΰ€?ΰ€Ώΰ€ΰ€Ύΰ€ΰ€ ΰ€ΰ₯ΰ€Έΰ₯ΰ₯€β€οΈ\n\n~ @ii_1444 π",
    "π ΰ€ΰ€¨ ΰ€ΰ€ΰ€ΰ₯ΰ€ ΰ€ΰ₯ ΰ€ΰ€¬ ΰ€€ΰ₯ΰ€°ΰ€Ύ ΰ€¦ΰ₯ΰ€¦ΰ€Ύΰ€° ΰ€Ήΰ₯ ΰ€ΰ€Ύΰ€€ΰ€Ύ ΰ€Ήΰ₯β¦\nΰ€¦ΰ€Ώΰ€¨ ΰ€ΰ₯ΰ€ ΰ€­ΰ₯ ΰ€Ήΰ₯ ΰ€²ΰ₯ΰ€ΰ€Ώΰ€¨ ΰ€€ΰ₯ΰ€―ΰ₯ΰ€Ήΰ€Ύΰ€° ΰ€Ήΰ₯ ΰ€ΰ€Ύΰ€€ΰ€Ύ ΰ€Ήΰ₯ π\n\n~ @ii_1444 π₯",
    "π₯Ί ΰ€ΰ€Ύΰ€Ά ΰ€?ΰ₯ΰ€ ΰ€ͺΰ€Ύΰ€¨ΰ₯ ΰ€Ήΰ₯ΰ€€ΰ€Ύ ΰ€ΰ€° ΰ€€ΰ₯ ΰ€ͺΰ₯ΰ€―ΰ€Ύΰ€Έ ΰ€Ήΰ₯ΰ€€ΰ₯,\nΰ€¨ ΰ€?ΰ₯ΰ€ ΰ€ΰ€«ΰ€Ύ ΰ€Ήΰ₯ΰ€€ΰ€Ύ ΰ€ΰ€° ΰ€¨ ΰ€€ΰ₯ ΰ€ΰ€¦ΰ€Ύΰ€Έ ΰ€Ήΰ₯ΰ€€ΰ₯,π¦\nπ« ΰ€ΰ€¬ ΰ€­ΰ₯ ΰ€€ΰ₯ΰ€? ΰ€?ΰ₯ΰ€°ΰ₯ ΰ€¨ΰ€Ώΰ€ΰ€Ύΰ€Ήΰ₯ΰ€ ΰ€Έΰ₯ ΰ€¦ΰ₯ΰ€° ΰ€Ήΰ₯ΰ€€ΰ₯,\nΰ€?ΰ₯ΰ€ ΰ€€ΰ₯ΰ€°ΰ€Ύ ΰ€¨ΰ€Ύΰ€? ΰ€²ΰ₯ΰ€€ΰ€Ύ ΰ€ΰ€° ΰ€€ΰ₯ ΰ€?ΰ₯ΰ€°ΰ₯ ΰ€ͺΰ€Ύΰ€Έ ΰ€Ήΰ₯ΰ€€ΰ₯ΰ₯€β€οΈ\n\n~ @ii_1444 π₯",
    "π ΰ€?ΰ₯ΰ€ ΰ₯ ΰ€?ΰ₯ΰ€ ΰ₯ ΰ€―ΰ€Ύΰ€¦ΰ₯ΰ€ ΰ€ͺΰ€²ΰ€ΰ₯ΰ€ ΰ€ͺΰ₯ ΰ€Έΰ€ΰ€Ύ ΰ€²ΰ₯ΰ€¨ΰ€Ύ\nΰ€ΰ€ ΰ€Έΰ€Ύΰ€₯ ΰ€ΰ₯ΰ€ΰ€Ύΰ€°ΰ₯ ΰ€ͺΰ€² ΰ€ΰ₯ ΰ€¦ΰ€Ώΰ€² ΰ€?ΰ₯ΰ€ ΰ€¬ΰ€Έΰ€Ύ ΰ€²ΰ₯ΰ€¨ΰ€Ύ π₯°\nπ¦ΰ€¨ΰ€ΰ€° ΰ€¨ ΰ€ΰ€ΰ€ ΰ€Ήΰ€ΰ₯ΰ€ΰ€€ ΰ€?ΰ₯ΰ€ ΰ€ΰ€ΰ€°,\nΰ€?ΰ₯ΰ€Έΰ₯ΰ€ΰ₯ΰ€°ΰ€Ύΰ€ΰ€° ΰ€?ΰ₯ΰ€ΰ₯ ΰ€Έΰ€ͺΰ€¨ΰ₯ ΰ€?ΰ₯ΰ€ ΰ€¬ΰ₯ΰ€²ΰ€Ύ ΰ€²ΰ₯ΰ€¨ΰ€Ύΰ₯€π·\n\n~ @ii_1444 π₯",
    "π ΰ€ΰ€­ΰ₯ ΰ€Ήΰ€ΰ€Έΰ€Ύΰ€€ΰ€Ύ ΰ€Ήΰ₯ ΰ€―ΰ₯ ΰ€ͺΰ₯ΰ€―ΰ€Ύΰ€°,\nΰ€ΰ€­ΰ₯ ΰ€°ΰ₯ΰ€²ΰ€Ύΰ€€ΰ€Ύ ΰ€Ήΰ₯ ΰ€―ΰ₯ ΰ€ͺΰ₯ΰ€―ΰ€Ύΰ€°,π₯Ί\nπ₯ ΰ€Ήΰ€° ΰ€ͺΰ€² ΰ€ΰ₯ ΰ€―ΰ€Ύΰ€¦ ΰ€¦ΰ€Ώΰ€²ΰ€Ύΰ€€ΰ€Ύ ΰ€Ήΰ₯ ΰ€―ΰ₯ ΰ€ͺΰ₯ΰ€―ΰ€Ύΰ€°,\nΰ€ΰ€Ύΰ€Ήΰ₯ ΰ€―ΰ€Ύ ΰ€¨ ΰ€ΰ€Ύΰ€Ήΰ₯ ΰ€ͺΰ€° ΰ€ΰ€ͺΰ€ΰ₯ ΰ€Ήΰ₯ΰ€¨ΰ₯ ΰ€ΰ€Ύ,π\nΰ€ΰ€Ήΰ€Έΰ€Ύΰ€Έ ΰ€¦ΰ€Ώΰ€²ΰ€Ύΰ€€ΰ€Ύ ΰ€Ήΰ₯ ΰ€―ΰ₯ ΰ€ͺΰ₯ΰ€―ΰ€Ύΰ€°ΰ₯€π·\n\n~ @ii_1444",
    "π ΰ€ΰ€ΰ€¦ΰ€Ύΰ€ΰ€Ύ ΰ€?ΰ₯ΰ€°ΰ₯ ΰ€?ΰ₯ΰ€Ήΰ€¬ΰ₯ΰ€¬ΰ€€ ΰ€ΰ€Ύ\nΰ€Έΰ€¬ ΰ€²ΰ€ΰ€Ύ ΰ€²ΰ₯ΰ€€ΰ₯ ΰ€Ήΰ₯ΰ€,π¦\nπ· ΰ€ΰ€¬ ΰ€€ΰ₯ΰ€?ΰ₯ΰ€Ήΰ€Ύΰ€°ΰ€Ύ ΰ€¨ΰ€Ύΰ€? ΰ€Έΰ₯ΰ€¨ΰ€ΰ€°\nΰ€Ήΰ€? ΰ€?ΰ₯ΰ€Έΰ₯ΰ€ΰ₯ΰ€°ΰ€Ύ ΰ€¦ΰ₯ΰ€€ΰ₯ ΰ€Ήΰ₯ΰ€ΰ₯€π\n\n~ @ii_1444 π",
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

