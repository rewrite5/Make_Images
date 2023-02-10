from fastapi import APIRouter
from PIL import Image, ImageChops, ImageOps

router = APIRouter()
img = Image.open('original.jpg')


@router.get('/')
async def abrir():
    img.show()

    return {
        "step": "Abrir Imagen Original",
        "status": "SUCCESS"
    }

@router.get('/invertir_color')
async def invertir():
    new_image = ImageChops.invert(img)
    new_image.save("colorInvertido.jpg")

    return {
        "step": "Escala de Grises",
        "status": "SUCCESS"
    }

@router.get('/black_white')
async def negro():
    new_image = ImageOps.grayscale(img)
    new_image.save("blackWhite.jpg")

    return {
        "step": "black & white",
        "status": "SUCCESS"
    }

@router.get('/rotar_90')
async def girar():
    new_image = img.transpose(Image.ROTATE_90)
    new_image.save("rotar90.jpg")

    return {
        "step": "rotar90",
        "status": "SUCCESS"
    }
