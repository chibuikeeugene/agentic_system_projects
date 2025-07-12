from llama_index.core.tools import BaseTool
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.llama_cpp import LlamaCPP


def agent(tools: list[BaseTool], llm: LlamaCPP,):
    """Event Agent that handles queries about guests """

    party_agent = AgentWorkflow.from_tools_or_functions(
        tools_or_functions= tools,
        llm=llm,
    )
    return party_agent