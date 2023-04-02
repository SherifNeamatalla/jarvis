from pathlib import Path

from loaders.base_loader import BaseLoader


class JSONLoader(BaseLoader) :
    def __init__(self, path: str, params: dict):
        super().__init__(path=path, params=params, data_loader_name="JSONReader", IndexClass=None, index=None)

    def load_data(self):
        if self.data_loader is None:
            raise ValueError("Data loader is not provided.")
        return self.data_loader.load_data(Path(self.params.path))

    def get_params_types(self):
        return {"path":'str'}