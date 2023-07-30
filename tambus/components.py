from dataclasses import dataclass
import re 


@dataclass
class Component:
    pattern: str
    replace: str 
    
    def replace_regex(self, content: str):
        return re.sub(self.pattern,self.replace,  content) 

