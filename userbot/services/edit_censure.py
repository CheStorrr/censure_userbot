
class EditService:

    def __init__(
        self, 
        path_to_banroots: str = './userbot/ban_roots.txt',
        *args, 
        **kwargs
    ) -> None:
        with open(path_to_banroots) as file:
            self.banroots = file.readlines()



    def __call__(
        self,
        message: str
    ) -> str:
        

        for banroot in self.banroots:
            banroot = banroot.strip()
            message = message.replace(
                banroot,
                "#"*len(banroot)    
            )
                
            
        return message
