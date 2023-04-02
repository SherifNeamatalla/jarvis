from .html_loader import HtmlLoader
from .json_loader import JSONLoader


class LoaderFactory:
    loaders = {"HtmlLoader": HtmlLoader, "JSONLoader": JSONLoader}

    @staticmethod
    def create_loader(loader_type: str, path: str, params: dict):
        if loader_type not in LoaderFactory.loaders:
            raise ValueError(f"Invalid loader type: {loader_type}")

        loader_class = LoaderFactory.loaders[loader_type]
        return loader_class(path, params)

    @staticmethod
    def get_loader_types():
        return LoaderFactory.loaders
