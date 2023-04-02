import os

import yaml
from llama_index import GPTSimpleVectorIndex, download_loader

save_path = os.path.join(os.path.dirname(__file__), "..", "..", "saved")


class BaseLoader:
    def __init__(
        self,
        name: str,
        path: str,
        params: dict,
        data_loader_name: str,
        index: any = None,
    ):
        self.name = name
        self.path = os.path.join(save_path, path)
        self.params = params
        self.data_loader_name = data_loader_name
        self.index = index
        if self.index is None:
            self.load_loader()
            self.index = GPTSimpleVectorIndex.from_documents(self.load_data())

    def load_data(self):
        raise NotImplementedError("Not implemented for base class.")

    def load_loader(self):
        self.data_loader = download_loader(self.data_loader_name)()

    def save(self):
        # Create directory for index
        os.makedirs(self.path, exist_ok=True)

        # Write config.txt file with data loader and params
        with open(os.path.join(self.path, "config.yaml"), "w") as f:
            yaml.dump(
                {
                    "name": self.name,
                    "data_loader": self.data_loader_name,
                    "params": self.params,
                },
                f,
            )

        # Save index to file
        index_file_path = os.path.join(self.path, "index")
        self.index.save_to_disk(index_file_path)

    def query(self, query: str):
        return self.index.query(query)

    @staticmethod
    def load_from_path(path: str, loaderTypes):
        path = os.path.join(save_path, path)

        if not os.path.exists(path):
            raise ValueError("Path does not exist.")

        params = {}
        # Load config.txt file
        with open(os.path.join(path, "config.yaml"), "r") as f:
            config = yaml.safe_load(f.read())
            name = config["name"]
            params = config["params"]
        # Load index from file
        index_file_path = os.path.join(path, "index")
        index = GPTSimpleVectorIndex.load_from_disk(index_file_path)

        LoaderClass = loaderTypes[name]

        return LoaderClass(path, params, index)
