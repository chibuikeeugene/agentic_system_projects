# LLM powered agent using the llamaindex toolkit

## Llamaindex agentic application comprises three parts - 
1. Components
2. Agents and Tools
3. Workflows

## Project Title: 
* Party Event-based Agentic Retrieval Augmented Generative System

## Objective: 
* To equip our Agentic RAG System to answer queries about our guests

## Requirements:
1. Our agent needs to have knowledge in this domains - sport, culture and sciencve
2. To avoid topics (such as religion and politics) that could raise conflicts during the event
3. The agent should have knowledge of guests background
4. General knowledge about the weather to ensure we can find a real-time update to ensure perfect timing to launch the fireworks

## Tools to be built:
1. Invitees info tool - to help get an up to date info on guests
2. Web search tool - to get information on any data available on the web
3. Weather tool - retrieve current weather report in a location
4. Model stats tool - to retrieve models statistics

## How to setup and run the project:
1. Clone the repository
2. Setup your virtual environment
3. Navigate to the event_assistant_llama_agent folder
4. Run the command  - python -m src.core.app


## Sytem Implementation breakdown:
1. Identify and Define Data sources - via data manager 
2. Data layer:: Setup a data ingestion and indexing mechanism
3. Agent layer:: Define tools; Define agent logic; Add memory
4. Testing:: test ingestiong, chuncking and ingesting
5. Deployment:: Containerize; deploy to cloud; setup automation (deployment pipeline automation)
6. Monitoring:: log and monitor using prometheus and grafana