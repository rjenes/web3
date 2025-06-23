# Databricks notebook source
# MAGIC %run ../src/utils/init_helper


# COMMAND ----------

import os

from dune_client.query import QueryBase

from src.client.dune import DuneClient
from src.parameters.global_parameters import DuneAuthenticationParameters
from src.utils.logging_handler import get_logger

# COMMAND ----------

LOGGER = get_logger(__name__)

# COMMAND ----------

print(DuneAuthenticationParameters.DUNE_API_KEY)

# COMMAND ----------

# Set the DUNE_API_KEY in environment variables
os.environ["DUNE_API_KEY"] = DuneAuthenticationParameters.DUNE_API_KEY

# Create the DuneClient instance
client = DuneClient()

# COMMAND ----------

dune = DuneClient(
    api_key="93yrvfZ6MblrU7viVWMcL99UeGfaLaic",
    base_url="https://api.dune.com",
    request_timeout=300,  # request will time out after 300 seconds
)

# COMMAND ----------

query = QueryBase(
    query_id=5315676,
    # uncomment and change the parameter values if needed
    # params=[
    #     QueryParameter.text_type(name="contract", value="0x6B175474E89094C44Da98b954EedeAC495271d0F"), # default is DAI # noqa
    #     QueryParameter.text_type(name="owner", value="owner"), # default using vitalik.eth's wallet
    # ],
)

# COMMAND ----------

query_result = dune.run_query_dataframe(
    query=query,
    # , ping_frequency = 10 # uncomment to change the seconds between checking execution status, default is 1 second
    # , performance="large" # uncomment to run query on large engine, default is medium
    # , batch_size = 5_000 # uncomment to change the maximum number of rows to retrieve per batch of results, default is 32_000 # noqa
)
