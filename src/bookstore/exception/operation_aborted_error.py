"""
Raised whenever an operation is being aborted inside the book store
"""
class OperationAbortedError(Exception):
    pass