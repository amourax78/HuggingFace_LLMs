import os
os.system("cls")

from smolagents import CodeAgent, DuckDuckGoSearchTool, ToolCallingAgent
from smolagents.models import LiteLLMModel
# Initialize the search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the model
model = LiteLLMModel(model_id="ollama/qwen2.5:7b", api_base="http://localhost:11434");

agent = ToolCallingAgent(
    model=model,
    tools=[search_tool], 
)

# Example usage
response = agent.run(
    "Search for luxury superhero-themed party ideas, including decorations, entertainment, and catering."
)

os.system("cls")

print(response)