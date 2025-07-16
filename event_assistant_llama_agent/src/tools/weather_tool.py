# weather tool 
from llama_index.tools.weather import OpenWeatherMapToolSpec
from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv()
open_weather_key = os.getenv('OPEN_WEATHER_API_KEY')

# create an instance of the weathermaptoolspec
weather_tool_spec = OpenWeatherMapToolSpec(key=open_weather_key)

# convert toolspec to toollist to access the available tools and one which is need for out use-case
# tools = weather_tool_spec.to_tool_list()
# for tool in tools:
#     logger.info(tool.metadata)
   
# create the tool
weather_tool = weather_tool_spec.to_tool_list()[0]
