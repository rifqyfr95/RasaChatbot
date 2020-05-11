# # PART 3: Start the Bot
from rasa.core.agent import Agent
from rasa.nlu.model import Trainer, Metadata
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig

import asyncio


nlu_interpreter = RasaNLUInterpreter('./models/nlu/chatter')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter=nlu_interpreter, action_endpoint=action_endpoint)

# # Part 4:Talk to Bot

# from clint.textui import colored, puts
print("Start the conversation")
print()
print("Hi! How Can I help you today?")
while True:
    a = input()
    if a == 'stop':
        break
    responses = asyncio.run(agent.handle_message(a))
    for response in responses:
        print(response['text'])

# interactive learning:
# python -m rasa_core.train --online -d config/domain.yml -s data/stories.md -o models/dialogue -u models/nlu/default/chatter --epochs 250 --endpoints endpoints.yml



