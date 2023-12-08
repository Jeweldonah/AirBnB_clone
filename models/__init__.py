"""Initialize the models package.

This module creates a unique instance of the `FileStorage` class from the
`models.engine.file_storage` module.
It also calls the `reload()` method on the `storage` instance to load objects
from the JSON file if it exists.
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
