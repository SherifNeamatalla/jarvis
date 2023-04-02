from pathlib import Path

from .base_loader import BaseLoader


class HtmlLoader(BaseLoader):
    def __init__(self, path: str, params: dict, index=None):
        super().__init__(
            name="HtmlLoader",
            path=path,
            params=params,
            data_loader_name="SimpleWebPageReader",
            index=index,
        )

    def load_data(self):
        if self.data_loader is None:
            raise ValueError("Data loader is not provided.")
        return self.data_loader.load_data(urls=self.params["urls"])

    @staticmethod
    def get_params_types():
        return {"urls": "str_list"}
