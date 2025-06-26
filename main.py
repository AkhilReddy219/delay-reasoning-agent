import json
from reasoning_engine.agent import DelayReasoningAgent

# Load dummy data
with open("data/dummy_shipment.json") as f:
    shipment_data = json.load(f)

# Initialize agent
agent = DelayReasoningAgent()

# Get delay explanations for each shipment
for shipment in shipment_data:
    
    shipment_id = shipment.get("shipment_id", "Unknown Shipment")
    print(f"\n📦 Shipment ID: {shipment_id}")
    print("-" * 40)

    explanations = agent.analyze_shipment(shipment)
    
    if explanations:
        for exp in explanations:
            print("•", exp)
    else:
        print("✅ No issues detected.")