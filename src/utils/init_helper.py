# Databricks notebook source
import sys

# COMMAND ----------

"""Adds the repository root to the system path based on the current notebook path."""
notebook_path: str = (
    dbutils.notebook.entry_point.getDbutils()  # noqa: F821
    .notebook()
    .getContext()
    .notebookPath()
    .get()
)  # noqa
repository_root: str = "/Workspace" + "/".join(notebook_path.split("/")[:4])
sys.path.append(repository_root)
