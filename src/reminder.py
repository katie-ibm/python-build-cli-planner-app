from sys import prefix


class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """
    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'

class PoliteReminder(PrefixedReminder):
    """This class inherits from PrefixReminder.
    It will help make our text more exciting.
    """
    def __init__(self, text, date=None):
        super().__init__("please ")
        self.text = self.prefix + text
    
    def __iter__(self):
        return iter([self.text])