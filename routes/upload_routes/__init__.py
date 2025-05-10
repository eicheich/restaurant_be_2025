from fastapi import APIRouter, UploadFile, File
from utils.image import save_upload_file

upload_router = APIRouter(
    prefix="/upload",
    tags=["upload"],
)

@upload_router.post("/image")
async def upload_image(file: UploadFile = File(...)):
    """
    Upload an image file.
    Returns the relative path to the uploaded file.

    - Supports: JPG, JPEG, PNG, GIF, WEBP
    - Maximum file size: 5MB
    """
    file_path = await save_upload_file(file)
    return {"image_url": file_path}
