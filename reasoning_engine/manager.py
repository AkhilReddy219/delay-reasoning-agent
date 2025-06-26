from reasoning_engine.agent import RuleBasedAgent
from reasoning_engine.context_builder import ReasoningContextBuilder
from reasoning_engine.llm_reasoner import LLMReasoner

class ReasoningManager:
    """
    Orchestrates which reasoning engine to use based on the selected mode.
    """

    def __init__(self, mode="rule"):
        """
        Initialize the manager.

        Args:
            mode (str): 'rule' for rule-based reasoning, 'llm' for LLM-based agentic reasoning.
        """
        self.mode = mode
        self.rule_agent = RuleBasedAgent()
        self.context_builder = ReasoningContextBuilder()
        self.llm_reasoner = LLMReasoner()

    def analyze_shipment(self, shipment):
        """
        Perform delay reasoning based on the selected mode.

        Args:
            shipment_id (str): Unique identifier for the shipment.
            events (List[Dict]): List of events for this shipment.

        Returns:
            List[str]: List of explanations.
        """
        shipment_id = shipment.get("shipment_id", "Unknown")

        if self.mode == "rule":
            return self.rule_agent.analyze_shipment(shipment)

        elif self.mode == "llm":
            context = self.context_builder.build_context(shipment)
            return self.llm_reasoner.generate_explanation(shipment_id, context)

        else:
            raise ValueError(f"Unsupported mode: {self.mode}")