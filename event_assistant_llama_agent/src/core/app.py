from src.tools import guest_info_retriever_tool, hf_model_stats_tool, weather_tool, web_search_tool
from src.agents import event_anchor_agent
from src.prompts import system_prompt
from loguru import logger


from llama_index.llms.llama_cpp import LlamaCPP

# initiate the model
llm = LlamaCPP(
    model_path="../models/Meta-Llama-3.1-8B-Instruct-Q6_K.gguf",
    temperature=0.7,
    context_window=2048,
    model_kwargs={"n_gpu_layers": 4, "n_ctx": 2048}
)

# create the list of base tools
tools = [guest_info_retriever_tool.guest_info_tool, 
         hf_model_stats_tool.model_stats_tool,
         weather_tool.weather_tool,
         web_search_tool.search_tool,
         ]

sys_prompt = system_prompt.system_prompt

async def main(input_query:str) -> str:
    """application base"""

    agent = event_anchor_agent.agent(tools=tools, llm=llm)

    output = await agent.run(input_query)

    return output

continue_conversation =  True

if __name__ == "__main__":
    while continue_conversation:
        user_input = input('listening... ')
        result = main(user_input)
        logger.info(result)
        if user_input == 'thanks':
            continue_conversation = False
            logger.info('Thanks for conversing today.')
