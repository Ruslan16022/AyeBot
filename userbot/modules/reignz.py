# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio
from asyncio import wait

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.gangsta$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`EVERyBOdy`")
        await asyncio.sleep(0.3)
        await e.edit("`iZ`")
        await asyncio.sleep(0.2)
        await e.edit("`GangSTur`")
        await asyncio.sleep(0.5)
        await e.edit("`UNtIL`")
        await asyncio.sleep(0.2)
        await e.edit("`I`")
        await asyncio.sleep(0.3)
        await e.edit("`ArRivE`")
        await asyncio.sleep(0.3)
        await e.edit("🔥")
        await asyncio.sleep(0.3)
        await e.edit("`EVERyBOdy iZ GangSTur UNtIL I ArRivE` 🔥")

@register(outgoing=True, pattern="^.noobda$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`EVERyOne`")
        await asyncio.sleep(0.4)
        await e.edit("`iZ`")
        await asyncio.sleep(0.2)
        await e.edit("`Noob`")
        await asyncio.sleep(0.5)
        await e.edit("`UNtIL`")
        await asyncio.sleep(0.2)
        await e.edit("`Ultra Noob`")
        await asyncio.sleep(0.3)
        await e.edit("`ArRiVe`")
        await asyncio.sleep(0.3)
        await e.edit("🔥")
        await asyncio.sleep(0.3)
        await e.edit("`EVERyOne iZ Noob UNtIL Ultra Noob ArRivE` 🔥")
        
@register(outgoing=True, pattern="^.hacker$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("•••••••")
        await asyncio.sleep(0.4)
        await e.edit("`Hacking`")
        await asyncio.sleep(0.2)
        await e.edit("`Started`")
        await asyncio.sleep(0.5)
        await e.edit("`Your`")
        await asyncio.sleep(0.2)
        await e.edit("`id`")
        await asyncio.sleep(0.3)
        await e.edit("`Hacked`")
        await asyncio.sleep(0.3)
        await e.edit("🔥")
        await asyncio.sleep(0.3)
        await e.edit("`Your account has been haXed.` 🔥") 
        
@register(outgoing=True, pattern="^.pruhack$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("••")
        await asyncio.sleep(0.3)
        await e.edit("••••")
        await asyncio.sleep(0.2)
        await e.edit("•••••••")
        await asyncio.sleep(0.7)
        await e.edit("`Id Found`")
        await asyncio.sleep(0.2)
        await e.edit("`Hacking Started`")
        await asyncio.sleep(0.3)
        await e.edit("`Traget Account`")
        await asyncio.sleep(0.3)
        await e.edit("`Hacked`")
        await asyncio.sleep(0.3)
        await e.edit("`Your account iz hacked now... Pay moni to remove get rid of it` 🔥")


CMD_HELP.update({
    "gangsta": "Gangta Slag"
})
CMD_HELP.update({
    "noobda": "Just A Fucking Noob"
})
CMD_HELP.update({
    "hacker": "Account` Hacked And Deleted"
})
CMD_HELP.update({
    "pruhack": "Account`Hacked Need Money xD"
})
