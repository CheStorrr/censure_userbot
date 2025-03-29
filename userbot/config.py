from dotenv import load_dotenv 
from os import getenv 

from typing import Optional

load_dotenv()

class Config:
    api_id: Optional[int] = getenv('api_id')
    api_hash: Optional[str] = getenv('api_hash')
    password: Optional[str] = getenv('password')
    phone_number: Optional[int] = getenv('phone_number')

    mita_chat_id: int = -1002338011582
    myid: int = 6574898357