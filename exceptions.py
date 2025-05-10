from fastapi import HTTPException

class DatabaseError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=f"Database error: {detail}")

class ValidationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=f"Validation error: {detail}")

class ResourceNotFoundError(HTTPException):
    def __init__(self, resource: str, resource_id: int = None):
        detail = f"{resource} not found"
        if resource_id:
            detail = f"{resource} with id {resource_id} not found"
        super().__init__(status_code=404, detail=detail)

class DuplicateResourceError(HTTPException):
    def __init__(self, resource: str, field: str, value: str):
        super().__init__(status_code=409, detail=f"{resource} with {field} '{value}' already exists")
