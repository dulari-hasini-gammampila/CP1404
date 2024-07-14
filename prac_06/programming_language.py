class ProgrammingLanguage:
    """represent the Programming Language"""
    def __init__(self, name="", typing="", reflection=True, year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """check if the programming language is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """return the information of the programming language"""
        return f"{self.name},{self.typing} Typing, Reflection={self.reflection}First appeared in {self.year}"
