from dataclasses import dataclass 
from typing import Optional

@dataclass
class TypeCensure:
    is_banwords: bool 
    index: Optional[int]