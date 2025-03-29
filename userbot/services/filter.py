from ..types import TypeCensure
import logging

class CensureService:

    def __init__(
        self, 
        path_to_banwords: str = './userbot/ban_words.txt',
        *args, 
        **kwargs
    ) -> None:
        with open(path_to_banwords) as file:
            self.banwords = file.readlines()
        

    def __call__(
        self,
        message: str
    ) -> TypeCensure:
        for index, word in enumerate(message.split()):
            for banword in self.banwords:
                banword = banword.strip()
                if word in self.banwords or banword in word or word == banword:
                    return TypeCensure(
                        is_banwords=True,
                        index=index
                    )
            
        return TypeCensure(
            is_banwords=False,
            index=None
        )
