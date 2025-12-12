from sortedcontainers import SortedList
from typing import List, Optional
from dataclasses import dataclass
from enum import Enum

## CONSTANTS
OFFLINE_TIMEOUT = 60
## ENUMS
class EventType(Enum):
    MESSAGE = "MESSAGE"
    OFFLINE = "OFFLINE"

## Data Models
@dataclass
class Event:
    type: EventType
    timestamp: int
    payload: str

class UserStateManager:
    def __init__(self, numberOfUsers: int):
        self.online_users = list(range(numberOfUsers))
        self.offline_users = SortedList(key = lambda tp: -tp[1])
    
    def _update_to_online(self, timestamp: int):
        while self.offline_users and timestamp >= self.offline_users[-1][1]:
            user_id, _timestamp = self.offline_users.pop()
            self.online_users.append(user_id)

    def set_offline(self, timestamp: int, user_id: int):
        self._update_to_online(timestamp)
        self.online_users.remove(user_id)
        self.offline_users.add((user_id, timestamp + OFFLINE_TIMEOUT))
    
    def get_online_users(self) -> List[int]:
        return self.online_users

class EventProcessor:
    def __init__(self, numberOfUsers: int):
        self.TOTAL_USERS = numberOfUsers
        self.user_state_manager = UserStateManager(numberOfUsers)
        self.mentions_by_id = [0]*numberOfUsers
    
    def process_event(self, event: Event):
        if event.type == EventType.MESSAGE:
            self._process_message_event(event)
        elif event.type == EventType.OFFLINE:
            self._process_offline_event(event)
        else:
            raise ValueError("Invalid event type")
    
    def _process_message_event(self, event: Event):
        timestamp = event.timestamp
        self.user_state_manager._update_to_online(timestamp)

        mentions_str = event.payload
        if mentions_str == "ALL":
            mentions = list(range(self.TOTAL_USERS))
        elif mentions_str == "HERE":
            mentions = self.user_state_manager.get_online_users()
        else:
            USER_ID = slice(2, None)
            mentions = [int(mention[USER_ID]) for mention in mentions_str.split()]
        self.user_state_manager._update_to_online(timestamp)    

        for user_id in mentions:
            self.mentions_by_id[user_id] += 1
    
    def _process_offline_event(self, event: Event):
        timestamp = event.timestamp
        self.user_state_manager._update_to_online(timestamp)
        user_id = int(event.payload)
        self.user_state_manager.set_offline(timestamp, user_id)

class Solution:
    TYPE_RANK = {
        EventType.OFFLINE: 0,
        EventType.MESSAGE: 1
    }

    def _parse_events(self, events: List[List[str]]) -> List[Event]:
        parsed_events = []
        for event in events:
            event_typ, timestamp, payload = event
            try:
                event_type = EventType(event_typ)
            except ValueError:
                raise ValueError(f"Invalid event type: {event_typ}")
            event = Event(event_type, int(timestamp), payload)
            parsed_events.append(event)
        
        parsed_events.sort(key = lambda event: (event.timestamp, self.TYPE_RANK[event.type]))
        return parsed_events
    
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        eventProcessor = EventProcessor(numberOfUsers)
        parsed_events = self._parse_events(events)

        for event in parsed_events:
            eventProcessor.process_event(event)
        
        return eventProcessor.mentions_by_id