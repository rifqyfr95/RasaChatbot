# # Part 2:Adding dialogue capabilities 
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
import tensorflow
import rasa.core
import asyncio
from rasa.core.agent import Agent
from rasa.core.policies.fallback import FallbackPolicy
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.events import BotUttered
from rasa.core.run import serve_application
from rasa.core.utils import EndpointConfig

logger = logging.getLogger(__name__)


def train_dialogue(domain_file='domain.yml',
                   model_path='./models/dialogue',
                   training_data_file='./data/stories.md'):
    fallback = FallbackPolicy(fallback_action_name="utter_unclear", core_threshold=0.3, nlu_threshold=0.75)
    agent = Agent(domain_file, policies=[MemoizationPolicy(max_history=7), KerasPolicy(current_epoch=100,max_history=7), fallback])
    data = asyncio.run(agent.load_data(training_data_file))
    agent.train(data)
    # agent.train(
    #     data,
    #     epochs=500,
    #     batch_size=50,
    #     validation_split=0.2)
    agent.persist(model_path)
    return agent


def run_dialogue(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/chatter')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    rasa.core.run.serve_application(agent, channel='cmdline')
    return agent


if __name__ == '__main__':
    train_dialogue()