import datasets
from llama_index.core.schema import Document
from pathlib import Path
from config.config import model_dir
import os


def load_data_and_convert_to_doc():
    """this function handles dataset conversion to Document object"""

    # load data
    guest_data = datasets.load_dataset("agents-course/unit3-invitees", split="train")

    # convert dataset object into a list of document object
    docs = [
        Document(
            text = '\n'.join(
                [
                    f"Name: {guest_data[i]['name']}",
                    f"Relation: {guest_data[i]['relation']}",
                    f"Description: {guest_data[i]['description']}",
                    f"Email: {guest_data[i]['email']}"
                ]
            ),
            metadata = {'Name': f"{guest_data[i]['name']}"}
        )
        for i in range(len(guest_data))
    ]

    return docs


def load_model() -> str:
    """load the quantized generative model """
    for file in os.listdir(model_dir):
        if file.endswith('.gguf'):
            model_path_str = os.path.join(model_dir, file)
            return model_path_str