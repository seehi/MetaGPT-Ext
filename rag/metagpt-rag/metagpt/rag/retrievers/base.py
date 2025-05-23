"""Base retriever."""

from abc import abstractmethod

from llama_index.core.retrievers import BaseRetriever
from llama_index.core.schema import BaseNode, NodeWithScore, QueryType

from metagpt.rag.utils.reflection import check_methods

class RAGRetriever(BaseRetriever):
    """Inherit from llama_index"""

    @abstractmethod
    async def _aretrieve(self, query: QueryType) -> list[NodeWithScore]:
        """Retrieve nodes"""

    def _retrieve(self, query: QueryType) -> list[NodeWithScore]:
        """Retrieve nodes"""


class ModifiableRAGRetriever(RAGRetriever):
    """Support modification."""

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ModifiableRAGRetriever:
            return check_methods(C, "add_nodes")
        return NotImplemented

    @abstractmethod
    def add_nodes(self, nodes: list[BaseNode], **kwargs) -> None:
        """To support add docs, must inplement this func"""


class PersistableRAGRetriever(RAGRetriever):
    """Support persistent."""

    @classmethod
    def __subclasshook__(cls, C):
        if cls is PersistableRAGRetriever:
            return check_methods(C, "persist")
        return NotImplemented

    @abstractmethod
    def persist(self, persist_dir: str, **kwargs) -> None:
        """To support persist, must inplement this func"""


class QueryableRAGRetriever(RAGRetriever):
    """Support querying total count."""

    @classmethod
    def __subclasshook__(cls, C):
        if cls is QueryableRAGRetriever:
            return check_methods(C, "query_total_count")
        return NotImplemented

    @abstractmethod
    def query_total_count(self) -> int:
        """To support querying total count, must implement this func."""


class DeletableRAGRetriever(RAGRetriever):
    """Support deleting all nodes."""

    @classmethod
    def __subclasshook__(cls, C):
        if cls is DeletableRAGRetriever:
            return check_methods(C, "clear")
        return NotImplemented

    @abstractmethod
    def clear(self, **kwargs) -> int:
        """To support deleting all nodes, must implement this func."""
