class LLMReasoner:
    """
    Mocked LLM Reasoner to generate human-like explanations from context.
    This simulates what an actual LLM (like GPT) would output based on delay context.
    """

    def __init__(self):
        pass

    def generate_explanation(self, shipment_id, context):
        """
        Given a shipment's context, return human-readable delay reasoning.

        Args:
            shipment_id (str): ID of the shipment.
            context (dict): Dictionary containing delay data (from context_builder).

        Returns:
            List[str]: List of human-readable reasoning strings.
        """
        explanations = []

        delays = context.get("delays", [])
        if not delays:
            return [f"On time or ahead of schedule at all locations."]

        for delay in delays:
            loc = delay["location"]
            planned = delay["planned"]
            actual = delay["actual"]
            mins = delay["delay"]

            explanation = (
                f"(delay of {mins} mins at location {loc}, planned: {planned}, actual: {actual}, delay: {mins} mins). "
                f"This may have been caused by traffic, weather, or unloading issues."
            )
            explanations.append(explanation)

        return explanations