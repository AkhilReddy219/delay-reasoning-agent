import json
from reasoning_engine.manager import ReasoningManager
from reasoning_engine.agent import RuleBasedAgent

# Load dummy data
with open("data/dummy_shipment.json") as f:
    shipment_data = json.load(f)

# Initialize agent
#agent = DelayReasoningAgent()

#Reasoning Manager to decide the type of approach (rule or llm based)
manager = ReasoningManager(mode="llm")

# Get delay explanations for each shipment
for shipment in shipment_data:

    print(f"\n📦 Shipment ID: {shipment.get('shipment_id', 'Unknown')}")
    print("-" * 40)

    #Old - only rule based calculation
    #explanations = agent.analyze_shipment(shipment)

    #New - manager to decide the approach
    explanations = manager.analyze_shipment(shipment)
    
    if explanations:
        for exp in explanations:
            print("•", exp)
    else:
        print("✅ No issues detected.")