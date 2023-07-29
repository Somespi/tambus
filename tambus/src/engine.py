import re

class TambusEngine:

    def translate(self, content: str, **kwargs):
        self.variables: dict = kwargs
        self.content: str = content

        if re.search(r"{(.*?)}", self.content):
            self.translate_variables()
            
        return self.content

    def translate_variables(self):
        match = re.search(r"{(.*?)}", self.content)
        while match:
            variable = match.group(1)
            if variable in self.variables:
                self.content = self.content.replace(match.group(), self.variables[variable])
            else:
                raise ValueError(f"Variable '{variable}' not found in the provided kwargs.")
            match = re.search(r"{(.*?)}", self.content)


engine = TambusEngine()
print(engine.translate("<h1>{greeting}</h1>", greeting="Hello"))
