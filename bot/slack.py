from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import os
from rasa_core.utils import Utils

#load you trained model
interpreter = RasaNLUInterpreter("models/nlu/default/horoscopebot/")
MODEL_PATH = "models/dialogue"
action_endpoint = EndpointConfig(url="https://url")
agent = Agent.load(MODEL_PATH, interpreter=interpreter, action_endpoint=action_endpoint)

input_channel = SlackInput(
    slack_token = "YOUR_SLACK_TOKEN",
    #this is the `bot_user_o_auth_access_token`
    slack_channel = "YOUR_SLACK_CHANNEL"
    # the name of your chennal to which set the optimal

)
#set serve_forever=False if you want to kepp the  server running
s = agent.handle_chennals([input_channel],int(os.environ.get('PORT',5004)), serve_forever=True)
