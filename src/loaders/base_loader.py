import os

from llama_index import download_loader
import yaml


class BaseLoader:
    def __init__(self, path: str, params: dict, data_loader_name:str, IndexClass:any, index:any=None):
        self.path = path
        self.params = params
        self._IndexClass = IndexClass
        self.data_loader_name = data_loader_name
        self.index = index
        if self.index is None:
            self.load_loader()
            self.index = self._IndexClass.from_documents(self.load_data())
    
    def load_data(self):
        raise NotImplementedError("Not implemented for base class.")
    
    def get_params_types(self):
        raise NotImplementedError("Not implemented for base class.")
    
    def load_loader(self):
        self.data_loader = download_loader(self.data_loader_name)

    def save(self):
        # Create directory for index
        os.makedirs(self.path, exist_ok=True)

        # Write config.txt file with data loader and params
        with open(os.path.join(self.path, 'config.txt'), 'w') as f:
            yaml.dump({
                'data_loader': self.data_loader_name,
                'params': self.params
            }, f)


        # Save index to file
        index_file_path = os.path.join(self.path, 'index')
        self._IndexClass.save_to_disk(index_file_path)

    def query(self, query: str):
        return self.index.query(query)
    
    @staticmethod
    def load_from_path(path: str, IndexClass: any,LoaderClass):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Index file not found: {path}")
        
        data_loader = None
        params = {}
        # Load config.txt file
        with open(os.path.join(path, 'config.txt'), 'r') as f:
            config = f.read()
            config = yaml.safe_load(f.read())
            data_loader = download_loader(config['data_loader'])
            params = config['params']

        # Load index from file
        index_file_path = os.path.join(path, 'index')
        index = IndexClass.load_from_disk(index_file_path)

        return LoaderClass(path, params, data_loader, IndexClass, index)

        
        
