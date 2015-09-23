import ConfigParser
import json
import sys
import traceback

import wit

import responses


class EDWIN():
    def __init__(self, config='./config/wit.cfg'):
        self.responses = {}
        self.config = ConfigParser.RawConfigParser()
        self.config.read(config)

    def response(self, intent_str):
        def decorator(f):
            self.responses[intent_str] = f
            return f
        return decorator

    def callback(self, response):
        wit_response = json.loads(response)
        best_outcome = max(
            wit_response["outcomes"], key=lambda x: x['confidence'])

        response_function = self.responses.get(best_outcome["intent"])

        if response_function:
            return response_function()
        else:
            raise ValueError("Response '{}' has not been registered".format(
                best_outcome["intent"]))

    def respond(self, text):
        access_token = self.config.get('API', 'access_token')
        wit.text_query_async(text, access_token, self.callback)

    def run(self):
        responses.load_all()
        wit.init()
        while True:
            try:
                question = raw_input("> ")
            except EOFError:
                print "\nExiting..."
                wit.close()
                sys.exit()

            try:
                self.respond(question)
            except Exception:
                traceback.print_exc(file=sys.stdout)
