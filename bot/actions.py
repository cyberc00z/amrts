from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import requests
from rasa_core_sdk import Action 
from rasa_core_sdk.events import SlotSet 

class GetTodaysHoroscope(Action):
    
    def name(self):
        return "get todays horoscope"

    def run(self, dispatcher, tracker, domain):
        # type : (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        base_url = 'http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}'
        url = base_url.format(**{'day': "today", 'sign':user_horoscope_sign})

        #http://horoscope-api.herokuapp.com/horoscope/today/capricon
        res = requests.get(url)
        todays_horoscope = res.json()['horoscope']
        response = "Your today's horoscope:\n{}".format(todays_horoscope)

        dispatcher.utter_message(response)
        return [SlotSet("horoscope_sign", user_horoscope_sign)]



class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"

    def run(self, domain, dispatcher, tracker):
        # type : (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

        subscribe = tracker.get_slot('subscribe')
        if subscribe == "True":
            response = "You're successfully subscribed !"

        if subscribe == "False":
            response = "You're successfully unsubscribed !"

        dispatcher.utter_message(response)
        return [SlotSet('subscribe', subscribe)]



"""
class RemoveFoodItem(Action):
    def name(self):
        return "remove_item"

    def run(self, domain, dispatcher, tracker):
        

        remove_item = tracker.get_slot('remove_item')
        if remove_item == "True":
            res =  'Food Item removed'

        else:
            res = "Food Item Not Removed"

        dispatcher.utter_message(res)
        return [SlotSet('remove_item', remove_item)]

"""