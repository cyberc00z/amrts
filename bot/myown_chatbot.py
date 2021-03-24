import os
from flask.signals import template_rendered
from flask.wrappers import Response

from typing_extensions import runtime
from werkzeug.exceptions import RequestedRangeNotSatisfiable
from rasa_core.channels.rasa_chat import RasaChatInput
from rasa_core.channels.channel import CollectingOutput, UserMessage
from rasa_core.agent import Agent 
from rasa_core.interpreter import RasaNLUInterpereter
from rasa_core.utils import EndPointConfig
from rasa_core import utils 
from flask import render_template, Blueprint, jsonify, request

#load your tained model
interpreter = RasaNLUInterpereter("models/nlu/default/horoscopebot")
MODEL_PATH = "models/dialogue"
action_endpoint = EndPointConfig(url="http://url")

agent = Agent.load(MODEL_PATH, interpreter=interpreter, action_endpoint=action_endpoint)

class MyNewInput (RasaChatInput):
    @classmethod
    def name(cls):
        return "rasa"

    def _check_token(self, token):
        if token == "secret":
            return {'username': 1234}

        else :
            print('Failed to check token: {}'.format(token))
            return None

    def blueprint(self, on_new_message):
        template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'myown_chatbot')
        custom_webhook = Blueprint('custom_webhook', __name__, template_folder=template_folder)

        @custom_webhook.route("/", methods=['GET'])
        
        def health():
            return jsonify({"status": "ok"})
        
        @custom_webhook.route('/chat', methods=['GET'])

        def chat():
            return render_template('index.html')

        @custom_webhook.route("/webhook", methods=['POST'])

        def receive():
            sender_id =self._extract_sender(request)
            text = self._extract_message(request)
            should_use_stream = utils.bool_arg("stream", default=False)

            if should_use_stream:
                return Response(
                    self.stream_response(on_new_message, text, sender_id), 
                    content_type='text/event-stream'
                
                )

            else:
                collector = CollectingOutputChannel()
                on_new_message(UserMessage(text, collector, sender_id))
                return jsonify(collector.messages)

        return custom_webhook


input_channel = MyNewInput(url='')
# set serve_forever=False if you wan to keep the server running
s = agent.handle_channels([input_channel], int(os.environ.get('PORT', 5004)), serve_forever=True)

