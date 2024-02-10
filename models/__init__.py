#!/usr/bin/python3
'''init.py file containing BaseModel class for package'''
import models
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
