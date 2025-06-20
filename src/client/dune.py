import os
from abc import ABC
from typing import Optional

import requests
from dune_client.client import DuneClient as OfficialDuneClient

from core.definitions import DuneAllowedQueryTypes
from src.client.exceptions import QueryTypeError
from src.client.interface import DataClientInterface
from src.utils.logging_handler import LoggingHandler

logger = LoggingHandler.get_logger(__name__)


class DuneClient(DataClientInterface, ABC):
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("DUNE_API_KEY")
        if not self.api_key:
            raise ValueError("DUNE_API_KEY not set in environment or as argument.")
        self.client = OfficialDuneClient(self.api_key)

    def fetch_data(self, query_id, query_type="non_paginated", params=None, batch_size=None, limit=None, offset=None):
        if query_type not in DuneAllowedQueryTypes:
            raise QueryTypeError(f"Query Type '{query_type}' is not supported!")

        if query_type == "non_paginated":
            return self._run_non_paginated_query(query_id, params or {}, batch_size)
        else:
            return self._run_paginated_query(query_id, params or {}, limit, offset)

    def _run_non_paginated_query(self, query_id, params=None, batch_size=None):
        # Call the official SDK
        return self.client.run_query(query_id, params or {}, batch_size=batch_size)

    def _run_paginated_query(self, query_id, params=None, limit=1000, offset=0):
        # Call the official SDK paginated fetch
        return self.client.get_execution_results(query_id, params or {}, limit=limit, offset=offset)

    def execute_query(
        self,
        name: str,
        description: str,
        query_sql: str,
        params: Optional[object],
        is_private: Optional[str],
        archived: Optional[str],
        tags: Optional[str],
    ) -> requests.Response:
        pass
