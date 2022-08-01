from middleware import db, index, user_profile, hero, hero_add, hero_update

from flask import jsonify

#app.add_url_rule('/api/hello/', 'index', index)
#app.add_url_rule('/api/db/', 'db', db)

def initialise_routes(app):
    if app:
        app.add_url_rule ('/api/hello/', 'index', index)
        app.add_url_rule ('/api/db', 'db', db) # URL endpoint, func name as string, function
        app.add_url_rule ('/api/', 'list_routes', list_routes, methods=['GET'], default={'app: app'})
        app.add_url_rule ('/api/profile/<id>/', 'user_profile', user_profile)
        app.add_url_rule ('/api/hero', 'hero', hero, methods=['GET'])
        app.add_url_rule ('/api/hero', 'hero_add', hero_add, methods=['POST'])
        app.add_url_rule ('/api/hero', 'hero_update', hero_update, methods=['POST'])
    return None

def list_routes (app):
    for route in app.url.map.iter_rules ():
        #print (route)
        #print (route.endpoint)
        #print (route.methods)
        routes.append({'Route': str(route),
                       'Endpoint': route.endpoint,
                       'Methods': list(route.methods)})
    #return  "Routes Info"
    return jsonify ({"Routes": routes, "Total": len(routes)})