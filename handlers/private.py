from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
š š§šµš¶š šš šš±šš®š»š°š² š§š²š¹š²š“šæš®šŗ š ššš¶š° šš¼š \n š„šš» š¢š» š£šæš¶šš®šš² š©š£š¦ š¦š²šæšš²šæ \nš¼šš²š²š¹ šš¶š“šµ š¤šš®š¹š¶šš š ššš¶š° šš» š©š \nā­šš²šš²š¹š¼š½š²š± šš [š„š®šš²-šš®š°š°šµš](https://t.me/Its_Hexor)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š¢šš»š²šæ", url="https://t.me/XDacchuX")
                  ],[
                    InlineKeyboardButton(
                        "š¦šš½š½š¼šæš", url="https://t.me/Raze_support"
                    ),
                    InlineKeyboardButton(
                        "ššæš¼šš½", url="https://t.me/RazeFriendsZone"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ššµš®š»š»š²š¹", url="https://t.me/RazeBots"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**š ššš¶š° šš¼š š¢š»š¹š¶š»š² š”š¼š\nš š„š®šš² ššš±š² <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š¦šš½š½š¼šæš", url="https://t.me/Raze_support")
                ]
            ]
        )
   )
