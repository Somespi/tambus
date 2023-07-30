import re
from mdengine import MDEngine
from components import Component

class TambusEngine:
    
    def md_integrate(self, content: str, md: str, components):
        """
        for base.html
        """
        md = MDEngine(components).translate(md)
        content = self.translate(content)
        match = re.search(r"{@placehold\s(.*?)}", self.content, flags=re.DOTALL)
        if match:
            if match.group(1).strip() == '__content':
                content = content.replace(match.group(), md)
        return content


    def translate(self, content: str, **kwargs):
        """
        Translates the given template.

        Parameters:
            content (str): The content to be translated.
            **kwargs (dict): The dictionary of variables to be used for translation.

        Returns:
            str: The translated content.
        """
        self.variables = kwargs
        self.content = content
        if re.search(r"{#repeat\s(.*?)}", self.content) is not None:
            self.translate_repeat()
        if re.search(r"{([^@#/:]).*?}", self.content) is not None:
            self.translate_expressions()
        if re.search(r"{#if\s(.*?)}", self.content) is not None:
            self.translate_if()
        return self.content
    
    def translate_repeat(self):
        """
        Translates each occurrence of the repeat block in the content string.
        
        Parameters:
            self (TranslateEach): The instance of the TranslateEach class.
        
        Returns:
            None
        """
        match = re.search(r"{#repeat\s(.*?)}", self.content, flags=re.DOTALL)
        while match:
            number = match.group(1)
            if isinstance(eval(number, self.variables), int):
                try:
                    elem = self.content.split(match.group())
                    elem[1] = elem[1].split("{/repeat}")
                except:
                    raise ValueError("Closing repeat was not found")
                repeated_elem = [elem[1][0]] * int(number)

                self.content =  ''.join([elem[0], ''.join(map(str, repeated_elem)), elem[1][1]])
            else:
                raise ValueError("Value after repeat block must be: integer")
        
            match = re.search(r"{#repeat\s(.*?)}", self.content, flags=re.DOTALL)




    def translate_if(self):
        """
        Finds and evaluates the conditional statements within the content of HTML.

        Returns:
            None.
        """
        match = re.search(r"{#if\s(.*?)}", self.content, flags=re.DOTALL)
        while match:
            expression = match.group(1)
            if eval(expression, self.variables):
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
        pattern = r"{([^@#/:]).*?}"
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