from fasthtml.common import *

app = FastHTML()

page = Html(
    Head(Title('Una página en especial')),
    Body(Div('Algo de texto de prueba, y vamos a ir a ', A('Google', href='https://google.com'), Img(src="https://placehold.co/200"), cls='myclass'), Div('Otro texto de prueba, y vamos a ir a ', A('Youtube', href='https://youtube.com'))))
print(to_xml(page))

@app.get("/")
def home():
    return page

serve()