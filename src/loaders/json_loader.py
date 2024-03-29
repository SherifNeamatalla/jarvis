from pathlib import Path

from util.util import get_data_path

from .base_loader import BaseLoader


class JSONLoader(BaseLoader):
    def __init__(self, path: str, params: dict, index=None):
        super().__init__(
            name="JSONLoader",
            path=path,
            params=params,
            data_loader_name="JSONReader",
            index=index,
        )

    def load_data(self):
        if self.data_loader is None:
            raise ValueError("Data loader is not provided.")
        return self.data_loader.load_data(Path(get_data_path(self.params["path"])))

    @staticmethod
    def get_params_types():
        return {"path": "str"}
