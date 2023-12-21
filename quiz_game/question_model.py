class Question:
    """Questions Class"""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        """String Representation of Question Object"""
        return f"Question('{self.text}', '{self.answer}')"
