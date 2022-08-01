from flask import jsonify, request, abort

heroes = [ {'name': 'elon musk', 'nationality': 'south african', 'occupation': 'entrepeneur'},
           {'name': 'iron man', 'nationality': 'usa', 'occupation': 'billionaire'},
           {'name': 'billy connolly', 'nationality': 'scotish', 'occupation': 'comedian'}]

def index ():
    return "Hello World"

def db ():
    return "Hello DB Grads"

def user_profile (id):
    return f"Profile page of user #{id}"

def hero ():
    return jsonify (heroes)

def hero_add():
    try:
        data = request.get_json (force = True)
        name = data['name']
        nationality = data['nationality']
        occupation = data ['occupation']

        if name and nationality and occupation:
            heroes.append({'name': name,
                           'nationality': nationality,
                           'occupation': occupation})
            return jsonify({'Hero ' + name: "added successfully"})

    except Exception as err:
        print (err)
        abort (408)

    return None

def hero_update():
    try:
        data = request.get_json (force = True)
        name = data['name']
        nationality = data['nationality']
        occupation = data ['occupation']

        hero_to_update = None

        if name and nationality and occupation:
            for index, hero in enumerate (heroes):
                print(hero)
                if heroes["name"] == name:
                    hero_to_update = hero

            if hero_to_update is not None:
                hero_to_update['nationality'] = nationality
                hero_to_update['occupation'] = occupation

                return jsonify({'Hero ' + name: "updated successfully"})

            else:
                return jsonify({"Hero " + name + " Not Found"}), 480

    except Exception as err:
        print (err)
        abort (408)

    return None