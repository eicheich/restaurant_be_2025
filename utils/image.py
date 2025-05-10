import os
from fastapi import UploadFile, HTTPException
from pathlib import Path

UPLOAD_DIR = "static/images"
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

async def save_upload_file(file: UploadFile) -> str:
    """
    Save an uploaded file to the images directory.
    Returns the relative path to the saved file.
    """
    # Create upload directory if it doesn't exist
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Validate file size
    file_size = 0
    contents = await file.read()
    file_size = len(contents)
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File size {file_size} exceeds maximum allowed size of {MAX_FILE_SIZE}"
        )

    # Reset file pointer
    await file.seek(0)

    # Validate file extension
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type {file_ext} not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    # Generate unique filename
    filename = f"{Path(file.filename).stem}_{os.urandom(8).hex()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Save the file
    with open(file_path, "wb") as f:
        f.write(contents)

    # Return relative path
    return f"/{file_path.replace(os.sep, '/')}"
