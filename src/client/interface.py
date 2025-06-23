from abc import ABC, abstractmethod


class DataClientInterface(ABC):
    @abstractmethod
    def fetch_data(self, **kwargs):
        """Fetch all data for a query (may use pagination internally)."""
        pass

    @abstractmethod
    def execute_query(self, **kwargs):
        """Create a Query"""
        pass
