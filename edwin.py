import sys
import traceback

class EDWIN():
    def __init__(self):
        self.responses = {}

    def response(self, intent_str):
        def decorator(f):
            self.responses[intent_str] = f
            return f
        return decorator

    def respond(self, text):
        intent = text
        response_function = self.responses.get(intent)
        if response_function:
            return response_function()
        else:
            raise ValueError(
                "Response '{}' has not been registered".format(intent))

    def run(self):
        while True:
            question = raw_input("> ")
            try:
                self.respond(question)
            except Exception:
                traceback.print_exc(file=sys.stdout)