import connexion

from swagger_server import encoder

app = connexion.App(__name__, specification_dir="./swagger/")
application = app.app  # expose global WSGI application object
app.app.json_encoder = encoder.JSONEncoder
app.add_api("swagger.yaml", arguments={"title": "Concordance"}, pythonic_params=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
