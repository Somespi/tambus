import re

class TambusEngine:
    def translate(self, content: str, kwargs):
        self.variables: dict = kwargs
        self.content: str = content

        if re.search(r"{([^#/:]+?(\[\w+\])?)}", self.content):
            self.translate_expressions()

        return self.content

    def translate_expressions(self):
        """
        Translates expressions in the content by replacing them with their evaluated values.

        Returns:
            None
        
        Raises:
            ValueError: If an invalid expression is encountered.
            ValueError: If there is an error evaluating an expression.
        """
        match = re.search(r"{([^#/:]+?(\[\w+\])?)}", self.content)
        while match:
            variable = match.group()[1:-1]
            try:
                self.content = self.content.replace(match.group(), str(eval(match.group()[1:-1], self.variables)))
                
            except KeyError:
                raise ValueError(f"Invalid expression: '{variable}'")
            except Exception as e:
                raise ValueError(f"Error evaluating expression: '{variable}'. {e}")

            match = re.search(r"{([^#/:]+?(\[\w+\])?)}", self.content)

t = TambusEngine()
print(t.translate("<h1>{a}</h1>", {'a': 44}))
