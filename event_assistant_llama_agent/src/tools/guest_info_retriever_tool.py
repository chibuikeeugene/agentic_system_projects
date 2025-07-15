from llama_index.core.tools import FunctionTool
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.schema import Document
from loguru import logger
from src.core import data_manager

# get Document
docs = data_manager.load_data_and_convert_to_doc()

def get_guest_info_retriever(query:str, document: Document = docs) -> str:
    """retrieve detailed information on guests based on their name or relation"""

    # create the retriever
    bm25_retriever = BM25Retriever.from_defaults(nodes=document)

    # pass a query to the retriever to get the desired results
    result = bm25_retriever.retrieve(query)
    logger.info(result)

    if result:
        return '\n\n'.join([
            value.text for value in result[:3]
        ])
    else:
        return 'No matching guest information'

# create the tool
guest_info_tool = FunctionTool.from_defaults(fn=get_guest_info_retriever)