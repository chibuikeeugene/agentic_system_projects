from src.tools import guest_info_retriever_tool, hf_model_stats_tool, weather_tool, web_search_tool
from src.agents import event_anchor_agent
from src.prompts import system_prompt
from loguru import logger
from . import data_manager as dm
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.core.workflow import Context
import asyncio
from transformers import AutoTokenizer
from dotenv import load_dotenv
import os
from huggingface_hub import login
from llama_index.llms.ollama import Ollama
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
# load_dotenv() # load env variables

# hf_token = os.getenv('HF_TOKEN') # load the hf token

# #create our tokenizer object
# login(token=hf_token)
# tokenizer_obj =  AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B", use_auth_token=True)


# load the model path
model =  dm.load_model()

sys_prompt = system_prompt.system_prompt

# selecting and instantiating a llm model
llm = Ollama(
    model='llama3.1:latest',
    temperature=0.7,
    context_window=8000,
    request_timeout=120.0,
)


# # initiate the model object
# llm = LlamaCPP(
#     model_path=model,
#     system_prompt=sys_prompt,
#     temperature=0.7,
#     max_new_tokens= 512,
#     context_window=2048,
#     model_kwargs={"n_gpu_layers": 4,} # "n_ctx": 2048,
# )

# create the list of base tools
tools = [guest_info_retriever_tool.guest_info_tool,
         hf_model_stats_tool.model_stats_tool,
         weather_tool.weather_tool,
         web_search_tool.search_tool,
         ]



async def app(input_query:str) -> str:
    """application base"""

    agent = event_anchor_agent.agent(tools=tools, llm=llm)

    #wrap the agent with the context class so as to maintain relevance of historic chat
    ctx = Context(agent)

    output = await agent.run(input_query, ctx=ctx,)

    return output

async def main():
    continue_conversation = True
    while continue_conversation:
        user_input = input("listening... ")
        if user_input.lower() == "thanks":
            logger.info("Thanks for conversing today.")
            continue_conversation = False
        else:
            try:
                result = await app(user_input)
                logger.info(result)
            except Exception as e:
                logger.error(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())

