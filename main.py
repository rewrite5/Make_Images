from fastapi import FastAPI
from routes import router
import uvicorn

app = FastAPI(title= 'Editor de Imagenes',
              description= 'API de prueba para la modificacion de una imagen a partir de una URL',
              version= '0.1')

app.include_router(router)
if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
