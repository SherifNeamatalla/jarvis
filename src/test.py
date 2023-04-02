import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, download_loader
from pathlib import Path

os.environ["OPENAI_API_KEY"] = "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"

SimpleWebPageReader = download_loader("SimpleWebPageReader")

loader = SimpleWebPageReader()

# open file from path
path = "/Users/sherifneamatalla/Desktop/projects/indexing/jarvis/src/loaders/../../saved/wik_ub"


# load data from path

with open(os.path.join(path, "config.yaml"), "r") as f:
    # log data
    print(f.read())

documents = loader.load_data(urls=["https://wiki.ubuntu.com/"])
index = GPTSimpleVectorIndex.from_documents(documents)
response = index.query("what does the teams section in the given document say?")
print(response)
