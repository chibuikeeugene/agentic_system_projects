# search tool
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from llama_index.core.tools import FunctionTool

# instantiate the DuckduckGo search tool
search_tool_spec = DuckDuckGoSearchToolSpec()

# create function tool 
search_tool = FunctionTool.from_defaults(fn=search_tool_spec.duckduckgo_full_search)

