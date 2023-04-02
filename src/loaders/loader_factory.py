from llama_index.loaders import HtmlLoader, JSONLoader, GithubRepoLoader

# path: str, params: dict, data_loader_name:str, IndexClass:any, index:any=None
class LoaderFactory:
    loaders = {
        "html": HtmlLoader,
        "json": JSONLoader,
        "github": GithubRepoLoader
    }

    @staticmethod
    def create_loader(loader_type: str, path: str, params: dict):
        if loader_type not in LoaderFactory.loaders:
            raise ValueError(f"Invalid loader type: {loader_type}")
        
        loader_class = LoaderFactory.loaders[loader_type]
        return loader_class(path, params)
    
    @staticmethod
    def get_loader_types():
        return list(LoaderFactory.loaders.keys())
