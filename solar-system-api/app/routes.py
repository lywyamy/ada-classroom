from flask import Blueprint, jsonify, abort, make_response, request
from . import db
from .models.planets import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=['POST'])
def add_one_planet():
    '''
    POST method - add one planet to table
    '''
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"planet {new_planet.id} has been successfully created.", 201)


def validate_model(cls, model_id):
    '''
    helper function - validates model_id before routing
    returns error code if the model id is not correct format or is not present in table
    '''
    if model_id.upper() == "PLUTO":
        abort(make_response({"msg": "Pluto is cute. #justiceforpluto"}, 200))
    
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"msg": f"The object {cls.__name__}, with ID: {model_id} is invalid"}, 400))
    planet = cls.query.get(model_id)
    
    if not planet:
        abort(make_response({"msg": f"The object {cls.__name__}, with ID: {model_id} was not found"}, 404))
    return planet


@planets_bp.route("", methods=['GET'])
def get_all_planets():
    '''
    GET method - view all planet records from table
    '''
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()
    
    response = []
    for planet in planets:
        response.append(planet.to_dict())
    
    return jsonify(response), 200


@planets_bp.route("/<planet_id>", methods=['GET'])
def get_one_planet(planet_id):
    '''
    GET method - view one planet record from table
    '''
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()


@planets_bp.route("/<planet_id>", methods=['PUT'])
def update_planet(planet_id):
    '''
    PUT method - update one planet record in table
    '''
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    try:
        planet.name = request_body["name"]
        planet.description = request_body["description"]
    except:
        raise KeyError("Either planet name or description is missing from your input")
    db.session.commit()
    return make_response(f"Planet {planet.id} has been successfully updated"), 200


@planets_bp.route("/<planet_id>", methods=['DELETE'])
def delete_planet(planet_id):
    '''
    DELETE method - delete one planet's record from table
    '''
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(f"Planet {planet.id} has been deleted successfully"), 200









# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description
    
# planets = [
#     Planet(1, "Mercury", "first planet"),
#     Planet(2, "Venus", "second planet"),
#     Planet(3, "Earth", "third planet"),
#     Planet(4, "Mars", "fourth palnet"),
#     Planet(5, "Jupiter", "fifth planet"),
#     Planet(6, "Saturn", "sixth planet"),
#     Planet(7, "Uranus", "seventh planet"),
#     Planet(8, "Neptune", "eighth planet"),
#     Planet(9, "Pluto", "ninth planet")
# ]

# @planets_bp.route("", methods=["GET"])
# def get_planets():
#     planet_list = []
#     for planet in planets:
#         planet_list.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description
#             }
#         )

#     return jsonify(planet_list), 200

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description
#     }
    
    
#     for planet in planets:
#         if planet_id == planet.id:
#             return planet
#     abort(make_response({"msg": f"Planet {planet_id} not found"}, 404))