from googlesearch import search
from requests import get
from urllib.parse import quote_plus
from selenium import webdriver
from userbot.events import register
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, CHROME_DRIVER


@register(outgoing=True, pattern=r"^.google (.*)")
async def gsearch(q_event):
    """ For .google command, Do a Google search. """
    if not q_event.text[0].isalpha() and q_event.text[0] not in (
            "/", "#", "@", "!"):
        match_ = q_event.pattern_match.group(1)
        match = quote_plus(match_)
        result = ""
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
        for i in search(match, stop=10):
            driver.get(i)
            title = driver.title
            result += f"📍{title}\n{i}\n\n"
        await q_event.edit(
            "Google Search Query:\n\n" + match_ + "\n\nResults:\n\n" + result,
            link_preview = False
            )
        if BOTLOG:
            await q_event.client.send_message(
                BOTLOG_CHATID,
                "Google Search query " + match_ + " was executed successfully",
            )


CMD_HELP.update({
    'google': '.google <query>\
        \nUsage: Do a Google search.'
})
