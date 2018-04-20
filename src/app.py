#from connexion.resolver import RestyResolver
import connexion


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='./')
    app.add_api('recipes.yaml')#, resolver=RestyResolver('api'))
    app.run(port=8080)
