from pyrogram.filters import Filter 
from pyrogram.client import Client 
from pyrogram.types import Update, Message
from ..config import Config

class MitaChatFilter(Filter):

    async def __call__(
        self, 
        client: Client, 
        update: Update
    ) -> bool:
        
        if not isinstance(update, Message):
            return False
        
        if not update.from_user:
            return False
        
        if update.from_user.id != Config.myid:
            return False 
        
        if update.chat.id != Config.mita_chat_id:
            return False

        if not update.text:
            return False 
        
        return True