#!/usr/bin/python3
"""
initialize the model's package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
