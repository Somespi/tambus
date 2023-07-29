import re


class TambusEngine:

    def translate(self,content: str, **variables):
        self.varaibles: dict = variables
        self.content: str = content 
        
        if re.search(r"{[^#/:](.*)}", self.content):
            self.translate_variables()
        
        
        return self.content


    def translate_variables(self):
            match = re.search(r"{[^#/:](.*)}", self.content)
            while match:
                variable = match.group[1:-2]
                if variable in list(self.variables.keys()):
                    self.content = self.content.replace(match.group(), self.variables[variable])
                match = re.search(r"{[^#/:](.*)}", self.content)

    def translate_if():
        ...

    def translate_each():
        ...