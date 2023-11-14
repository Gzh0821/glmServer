from waitress import serve
from glmServer.wsgi import application

serve(
    app=application,
    host='127.0.0.1',
    port=8000
)