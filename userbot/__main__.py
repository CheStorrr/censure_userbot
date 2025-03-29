from pyrogram.client import Client
from pyrogram.types import Message
from .config import Config 
from .services import (
    CensureService,
    EditService    
)

from .filters import MitaChatFilter 

import logging 

logging.basicConfig(level=logging.INFO)

app = Client(
    name="Censure",
    api_id=Config.api_id,
    api_hash=Config.api_hash,
    password=Config.password,
    phone_number=Config.phone_number
)


@app.on_message(MitaChatFilter())
async def mita_chat_handler(
    client: Client,
    message: Message
):
    censure_service = CensureService()

    censured = censure_service(
        message=message.text    
    )

    if censured.is_banwords:

        edit_service = EditService()
        new_message = edit_service(
            message=message.text    
        )
        
        if new_message == message.text:
            return None 
        
        await message.edit_text(
            text=new_message 
        )

app.run()