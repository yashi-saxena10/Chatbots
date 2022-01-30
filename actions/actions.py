# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from translate import Translator
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionTranslateToLang(Action):
    #
    def name(self) -> Text:
        return "action_translate_to_lang"
        #
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            sentence=next(tracker.get_latest_entity_values("sentence"),None)
            print('sentence entity taken',sentence)
            to_langg=next(tracker.get_latest_entity_values("to_langg"),None)
            print('to_langg entity taken',to_langg)

            if not sentence:
                print('inside if of sentence')
                msg=f"Give me a sentence to translate"
                dispatcher.utter_message(text=msg)
                sentence=next(tracker.get_latest_entity_values("sentence"),None)
                print('inside if of sentence, sentence taken',sentence)
                return []

            if not to_langg:
                print('inside if of to_langg')
                msg=f"Give me a target language"
                dispatcher.utter_message(text=msg)
                to_lang=next(tracker.get_latest_entity_values("to_langg"),None)
                print('inside if of to_langg, to_langg taken',to_langg)
                return []

            translator= Translator(from_lang="english", to_lang=to_langg)
            print('translator var set')
            translation=translator.translate(sentence)
            print('translation var set',translation)

            msg=f"translated sentence: {translation}"
            dispatcher.utter_message(text=msg)

            return []
