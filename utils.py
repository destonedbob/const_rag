from langchain_core.embeddings import Embeddings


class ollamaEmbeddings(Embeddings):
    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts):
        """Embed search docs."""
        return [self.model.embed_query(text) for text in texts]

    def embed_query(self, text):
        """Embed query text."""
        return self.model.embed_query(text)