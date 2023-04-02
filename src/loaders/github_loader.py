import os
from pathlib import Path

from llama_index import download_loader
from llama_index.readers.llamahub_modules.github_repo import (
    GithubClient, GithubRepositoryReader)

from loaders.base_loader import BaseLoader


class GithubLoader(BaseLoader) :
    def __init__(self, path: str, params: dict):
        super().__init__(path=path, params=params, data_loader_name="GithubRepositoryReader", IndexClass=None, index=None)

    def load_data(self):
        if self.data_loader is None:
            raise ValueError("Data loader is not provided.")
        return self.data_loader.load_data(branch=self.params.branch,commit=self.params.commit)
    
    def load_loader(self):
        download_loader(self.data_loader_name)
        github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
        self.data_loader = GithubRepositoryReader(
            github_client,
            owner =                  self.params.owner,
            repo =                   self.params.repo,
            filter_directories =     (self.params.filter_directories, GithubRepositoryReader.FilterType.INCLUDE),
            filter_file_extensions = (self.params.filter_file_extensions, GithubRepositoryReader.FilterType.INCLUDE),
            verbose =                True,
            concurrent_requests =    10,
        )

    def get_params_types(self):
        return {"branch":'str',"commit":'str','owner':'str','repo':'str','filter_directories':'str_list','filter_file_extensions':'str_list','verbose':'bool','concurrent_requests':'int'}