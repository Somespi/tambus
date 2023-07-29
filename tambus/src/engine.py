import re

class TambusEngine:
    def translate(self, content: str, kwargs):
        self.variables: dict = kwargs
        self.content: str = content

        if re.search(r"{([^#/:]+?(\[\w+\])?)}", self.content):
            self.translate_expressions()
        if re.search(r"{#if\s(.*?)}", self.content):
            self.translate_if()
        return self.content






    def translate_if(self):
        """
        Finds and evaluates the conditional statements within the content of HTML.

        Returns:
            None.
        """
        match = re.search(r"{#if\s(.*?)}", self.content)
        while match:
            expression = match.group()[5:-1]
            if eval(expression):
                try:
                    self.content = self.content.replace(match.group(), '',1)
                    self.content = self.content.replace("{/if}", '', 1)
                except:
                    raise ValueError("if brace was not closed")
            else:
                try:
                    self.content = re.sub(r'{#if\s.*?}.*?{\/if}', "", self.content, flags=re.DOTALL)
                except:
                    raise ValueError("if brace was not closed")
        
            match = re.search(r"{([^#/:]+?(\[\w+\])?)}", self.content)

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
