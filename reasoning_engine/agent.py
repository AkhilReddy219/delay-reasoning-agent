from datetime import datetime
from utils.helpers import parse_iso, time_diff_minutes

class DelayReasoningAgent:

    def analyze_shipment(self, shipment):
        explanations = []

        planned = shipment["planned_milestones"]
        actual = shipment["actual_milestones"]
        events = shipment["event_log"]

        # 1. Delay per milestone
        for location in planned:
            p_time = parse_iso(planned[location])
            a_time = parse_iso(actual[location])
            delay = time_diff_minutes(p_time, a_time)

            if delay > 15:
                explanations.append(
                    f"Delay of {delay} mins at {location} (Planned: {p_time.time()}, Actual: {a_time.time()})"
                )

        # 2. Dwell time per location (based on STOP_START and STOP_END)
        location_events = {}
        
        for e in events:
            loc = e["location"]
            location_events.setdefault(loc, []).append(e)

        for loc, logs in location_events.items():
            start_event = next((e for e in logs if e["event_type"] == "STOP_START"), None)
            end_event = next((e for e in logs if e["event_type"] == "STOP_END"), None)

            if start_event and end_event:
                start = parse_iso(start_event["timestamp"])
                end = parse_iso(end_event["timestamp"])
                dwell = time_diff_minutes(start, end)
                if dwell > 20:
                    explanations.append(
                        f"Unusual dwell time of {dwell} mins at {loc} (Expected < 20 mins)"
                    )

        return explanations