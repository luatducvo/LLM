from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader

loader = DirectoryLoader(
    path="./data",
    glob="**/*.pdf",
    loader_cls=UnstructuredFileLoader,
    show_progress=True,
    use_multithreading=True,
)

docs=loader.load()

print(docs)

