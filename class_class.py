

class MyRef:
    def __init__(self):
        self.author = "" # assumption being that there is only one author
        self.title = ""

    def __str__(self):
        return f"""
                AUTHOR: {self.author}
                TITLE: {self.title}  
                """
