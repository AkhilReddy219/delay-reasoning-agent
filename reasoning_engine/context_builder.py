from utils.helpers import parse_iso, time_diff_minutes

class ReasoningContextBuilder:
    """
    Converts raw shipment data into structured reasoning context for the agent.
    """

    def build_context(self, shipment):
        context = {
            "shipment_id": shipment.get("shipment_id"),
            "delays": [],
            "events": shipment.get("event_log", []),
            "planned": shipment.get("planned_milestones", {}),
            "actual": shipment.get("actual_milestones", {}),
        }

        for location, planned_time in context["planned"].items():
            actual_time = context["actual"].get(location)
            if actual_time:
                planned_dt = parse_iso(planned_time)
                actual_dt = parse_iso(actual_time)
                delay_min = time_diff_minutes(planned_dt, actual_dt)
                if delay_min > 15:
                    context["delays"].append({
                        "location": location,
                        "delay": delay_min,
                        "planned": planned_time,
                        "actual": actual_time
                    })

        return context