from components import Component

class MDEngine:
    
    def __init__(self, components: list[Component]):
        self.components = components 
    
    def translate(self, content: str):
        self.content = content 
        
        for component in self.components:
            self.content = component.replace_regex(self.content)


