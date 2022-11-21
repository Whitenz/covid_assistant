from rasa_sdk import Action
from rasa_sdk.events import ActionExecuted, AllSlotsReset


class CheckDegrees1(Action):
    def name(self):
        return 'action_check_degrees_rule'

    def run(self, dispatcher, tracker, domain):
        x = tracker.get_slot('degrees')
        if x:
            temp = float(x.replace(',', '.'))
            if temp < 35 or temp > 42:
                dispatcher.utter_message(
                    text="Очень сомневаюсь, что у Вас такая температура."
                )
                return [AllSlotsReset()]
            else:
                dispatcher.utter_message(response="utter_more")
        else:
            dispatcher.utter_message(response="utter_more")
        return []


class CheckDegrees2(Action):
    def name(self):
        return 'action_check_degrees_stories'

    def run(self, dispatcher, tracker, domain):
        x = tracker.get_slot('degrees')
        if x:
            temp = float(x.replace(',', '.'))
            if temp < 35 or temp > 42:
                dispatcher.utter_message(
                    text='Очень сомневаюсь, что у Вас такая температура.'
                )
                return [AllSlotsReset(), ActionExecuted('action_back')]
        return []
