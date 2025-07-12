# model stats tool - 
# a tool to fetch model statistics from the Hugging Face Hub based on a username.
from huggingface_hub import list_models
from llama_index.core.tools import FunctionTool

# defining a get_model_stats funtion
def get_model_stats(author:str) -> str:
    """ fetch the most downloaded model from a specific author"""
    try:
        models = list(list_models(author=author, sort='downloads', direction=-1, limit=1))

        if models:
            model = models[0]
            return f'The most downloaded model by {author} is {model.id} with {model.downloads:,} downloads'
        else:
            return f'No model found for {author}'
        
    except Exception as e:
        return f'Could not fetch models for {author} due to {str(e)}'
    
# creating the tool
model_stats_tool = FunctionTool.from_defaults(fn=get_model_stats)