#!/usr/bin/python3
"""
initialize the model package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
