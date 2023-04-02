import os
from pathlib import Path
from typing import List

from llama_index import (GPTSimpleVectorIndex, SimpleDirectoryReader,
                         SimpleWebPageReader, download_loader)

from loaders.base_loader import Index
from loaders.loader_factory import LoaderFactory


def prompt_for_index() -> Index:
    print("Do you want to create a new index or load an existing one?")
    print("1. Create new index")
    print("2. Load existing index")
    selected_option = input("Enter the number of the option you want to choose: ")
    if selected_option == "1":
        print("Available data loaders:")
        for loader_type in LoaderFactory.get_loader_types():
            print(f"- {loader_type}")
        loader_type = input("Enter the name of the data loader you want to use: ")
        

        params = {}
        for param_name, param_type in loader_class.get_params_types().items():
            if param_type == str:
                value = input(f"Enter a value for parameter {param_name}: ")
                params[param_name] = value
            elif param_type == list:
                values = []
                while True:
                    value = input(f"Enter a value for parameter {param_name} (or type /exit to finish): ")
                    if value == "/exit":
                        break
                    values.append(value)
                params[param_name] = values

        index_class = input("Enter the name of the index class you want to use: ")
        path = input("Enter a path to save the index: ")

        loader = LoaderFactory.create_loader(loader_type,path, params)
        index = Index(path, {}, loader.__class__.__name__, index_class, loader)
        index.save()
        print(f"Index created and saved to path: {path}")
        return index
    elif selected_option == "2":
        index_path = input("Enter a path to the existing index: ")
        index = Index.load_from_path(index_path, GPTSimpleVectorIndex, LoaderFactory.load_loader)
        print(f"Index loaded from path: {index_path}")
        return index
    else:
        raise ValueError("Invalid option selected")


def main():
    index = prompt_for_index()
    while True:
        query = input("Enter a query (or 'q' to quit, 'c' to change index): ")
        if query.lower() == "q":
            break

        if query.lower() == "c":
            index = prompt_for_index()
            continue
        response = index.query(query)
        print(response)


if __name__ == "__main__":
    main()



# import os
# from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader,download_loader
# from pathlib import Path

# SimpleWebPageReader = download_loader("SimpleWebPageReader")

# loader = SimpleWebPageReader()

# os.environ['OPENAI_API_KEY']='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'
# documents = loader.load_data(urls=['https://gpt-index.readthedocs.io/_/downloads/en/latest/htmlzip/'])
# index = GPTSimpleVectorIndex.from_documents(documents)
# response = index.query('Tell me about lama index.')
# print(response)