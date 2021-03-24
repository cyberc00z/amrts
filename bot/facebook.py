from rasa_core.chennals.facebook import FacebookInput
from rasa_core.agent import Agent 
from rasa_core.interpreter import RasaNLUInterpreter
import os
from rasa_core.utils import EndpointConfig

#load you trained agent
interpreter = RasaNLUInterpreter("models/nlu/default/horoscopebot/")
MODEL_PATH = "models/dialog"
action_endpoint = EndpointConfig(url="https://url")
agent = Agent.load(MODEL_PATH, interpreter=interpreter)

input_chennal = FacebookInput(
    fb_verfiy = "FB_TOKEN",
    fb_secret = "FB_SECRET",

)
s = agent.handle_channels([input_chennal], int(os.environ.get('PORT', 5004)), serve_forever=True)



