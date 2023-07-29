import re

class TambusEngine:
    def translate(self, content: str, kwargs):
        """
        Translates the given template.

        Parameters:
            content (str): The content to be translated.
            kwargs (dict): The dictionary of variables to be used for translation.

        Returns:
            str: The translated content.
        """
        self.variables = kwargs
        self.content = content

        if re.search(r"{([^#/:]+?(\[\w+\])?)}", self.content) is not None:
            self.translate_expressions()
        if re.search(r"{#if\s(.*?)}", self.content) is not None:
            self.translate_if()
        return self.content


    def translate_if(self):
        """
        Finds and evaluates the conditional statements within the content of HTML.

        Returns:
            None.
        """
        match = re.search(r"{#if\s(.*?)}", self.content, flags=re.DOTALL)
        while match:
            expression = match.group()[5:-1]
            if eval(expression):
                self.content = self.content.replace(match.group(), '', 1).replace("{/if}", '', 1)
            else:
                self.content = re.sub(r'{#if\s.*?}.*?{\/if}', "", self.content, flags=re.DOTALL)
        
            match = re.search(r"{#if\s(.*?)}", self.content, flags=re.DOTALL)

    def translate_expressions(self):
        """
        Translates expressions in the content by replacing them with their evaluated values.

        Returns:
            None
        
        Raises:
            ValueError: If an invalid expression is encountered.
            ValueError: If there is an error evaluating an expression.
        """
        pattern = r"{([^#/:]+?(\[\w+\])?)}"
        match = re.search(pattern, self.content)
        while match:
            variable = match.group()[1:-1]
            try:
                expr = match.group()[1:-1]
                value = str(eval(expr, self.variables))
                self.content = self.content.replace(match.group(), value)
                
            except KeyError:
                raise ValueError(f"Invalid expression: '{variable}'")
            except Exception as e:
                raise ValueError(f"Error evaluating expression: '{variable}'. {e}")

            match = re.search(pattern, self.content)
