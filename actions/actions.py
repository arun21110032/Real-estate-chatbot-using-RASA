from typing import Any, Text, Dict, List
import mysql.connector
from rasa_sdk import FormValidationAction, Tracker,Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
import re
loc=''
type=''
price=''
features=''

class ValidateDetailsForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_details_form"
    
    def validate_details_GPE(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'GPE' value"""
        dispatcher.utter_message(text=" Location: {GPE} ")
        loc= slot_value
        return {"GPE": slot_value}

        
    def validate_details_proptype(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'proptype' value"""
        allowed_proptype = ['residential','commercial','plot']
        if slot_value.lower() not in allowed_proptype:
            dispatcher.utter_message(text=" Choose one from 'residential','commercial','plot' ")
            return {"proptype": None}
        else:
            dispatcher.utter_message(text=" property type: {proptype} ")
            type = slot_value
            return {"proptype": slot_value}
    
    def validate_details_cost(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'cost' value"""
        dispatcher.utter_message(text=" Budget: {cost} ")
        price = slot_value
        return {"cost": slot_value}

    def validate_details_amenity(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'amenity' value"""
        dispatcher.utter_message(text=" Amenities: {amenity} ")
        features = slot_value 
        return {"amenity": slot_value}
    

    
    
class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hi! How can I assist you today?")
        return []
    



class ActionAcknowledgeFeedback(Action):
    def name(self) -> Text:
        return "action_acknowledge_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get('entities', [])

        # Extract the email value if the 'email' entity is present
        feed_entity = next((entity.get('value') for entity in entities if entity.get('entity') == 'feedback'), None)
        dispatcher.utter_message(f"Thank you for the feedback. Bye!")
        return [SlotSet("feedback", feed_entity)]



    
    

class ValidateAppointForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_appoint_form"
    
    def validate_details_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'email' value"""
        dispatcher.utter_message(text=" email: {email} ")
        return {"email": slot_value}

        
    def validate_details_PERSON(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'PERSON' value"""
        dispatcher.utter_message(text=" PERSON: {PERSON} ")
        return {"PERSON": slot_value}
    
    def validate_details_usrphone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'usrphone' value"""
        dispatcher.utter_message(text=" usrphone: {usrphone} ")
        return {"usrphone": slot_value}


