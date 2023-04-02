import os
from pathlib import Path
from typing import List

from llama_index import (
    GPTSimpleVectorIndex,
    SimpleDirectoryReader,
    SimpleWebPageReader,
    download_loader,
)

from loaders.base_loader import BaseLoader
from loaders.loader_factory import LoaderFactory


os.environ["OPENAI_API_KEY"] = "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"


def prompt_for_index():
    print("Do you want to create a new index or load an existing one?")
    print("1. Create new index")
    print("2. Load existing index")
    selected_option = input("Enter the number of the option you want to choose: ")
    if selected_option == "1":
        print("Available data loaders:")
        types = LoaderFactory.get_loader_types()
        for i, loader_type in enumerate(types):
            print(f"{i+1}- {loader_type}")
        loader_index = int(
            input("Enter the index of the data loader you want to use: ")
        )

        # print all
        print("Available data loaders:")
        print(str(loader_index))
        print(types)
        print(list(types.keys())[loader_index - 1])

        loader_type = list(types.keys())[loader_index - 1]

        LoaderClass = types[loader_type]

        params = {}
        for param_name, param_type in LoaderClass.get_params_types().items():
            if param_type == "str":
                value = input(f"Enter a value for parameter {param_name}: ")
                params[param_name] = value
            elif param_type == "str_list":
                values = []
                while True:
                    value = input(
                        f"Enter a value for parameter {param_name} (or type /exit to finish): "
                    )
                    if value == "/exit":
                        break
                    values.append(value)
                params[param_name] = values

        path = input("Enter a path to save the index: ")

        loader = LoaderFactory.create_loader(loader_type, path, params)
        loader.save()
        print(f"Index created and saved to path: {path}")
        return loader
    elif selected_option == "2":
        index_path = input("Enter a path to the existing index: ")
        index = BaseLoader.load_from_path(index_path, LoaderFactory.get_loader_types())
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

# documents = loader.load_data(urls=['https://gpt-index.readthedocs.io/_/downloads/en/latest/htmlzip/'])
# index = GPTSimpleVectorIndex.from_documents(documents)
# response = index.query('Tell me about lama index.')
# print(response)
