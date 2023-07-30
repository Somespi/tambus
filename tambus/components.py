from dataclasses import dataclass
import re 


@dataclass
class Component:
    content: str
    regex: str 
    
    def replace_regex(self, content: str):
        return re.sub(self.regex, self.content, content) 
