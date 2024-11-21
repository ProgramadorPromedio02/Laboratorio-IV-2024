from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def home():
    return "<h1>Hola mundo, y bieviendo a FastHTML.</h1> <p>Esto es un parrafo</p>"

serve()