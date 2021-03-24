from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core import utils 
from rasa_core.agent import Agnet 
from rasa_core.policies.keras_policy import kerasPolicy
from rasa_core.policies.memorization import MemorizationPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy

if __name__ == "__main__":
    utils.configure_colored_logging(loglevel="DEBUG")

    training_data_file = './data/stories.md'
    model_path = './models/dialogue'

    agent = Agnet("horoscope_domain.yml", policies=[MemorizationPolicy(), kerasPolicy()])
    training_data = agent.load_data(training_data_file)

    agent.train(
        training_data,
        augmentation_factor=50,
        epoches=500,
        batch_size=10,
        validation_split=0.2
    )
    agent.presist(model_path)