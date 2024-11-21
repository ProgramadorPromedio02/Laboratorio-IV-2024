# Importamos las clases necesarias de fasthtml
from fasthtml.common import *
from starlette.testclient import TestClient

# Creamos la aplicación FastHTML
app = FastHTML()

# Definimos la ruta principal
@app.get("/")
def home():
    # Estructura de la página en FastHTML
    page = Html(
        Head(
            Title("Bienvenido a FastHTML"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1")
        ),
        Body(
            Div(
                H1("Bienvenido a FastHTML"),
                P("Esta es una página de prueba para entender cómo usar FastHTML."),
                A("Visita OpenAI", href="https://openai.com", cls="enlace"),
                Img(src="https://placehold.co/150x100", alt="Imagen de ejemplo"),
                cls="contenido"
            )
        )
    )
    return page

# Creamos un cliente de pruebas
client = TestClient(app)

# Hacemos una solicitud a la ruta principal y mostramos el HTML generado
response = client.get("/")
print(response.text)
