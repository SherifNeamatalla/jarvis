from pathlib import Path

from util.util import get_data_path

from .base_loader import BaseLoader


class PdfLoader(BaseLoader):
    def __init__(self, path: str, params: dict, index=None):
        super().__init__(
            name="HtmlLoader",
            path=path,
            params=params,
            data_loader_name="PDFReader",
            index=index,
        )

    def load_data(self):
        if self.data_loader is None:
            raise ValueError("Data loader is not provided.")
        return self.data_loader.load_data(file=Path(get_data_path(self.params["file"])))

    @staticmethod
    def get_params_types():
        return {"file": "str"}
