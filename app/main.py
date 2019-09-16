import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#00FF00"

    return start_response({'color': '#FF0000','head':'bendr','tail':'bolt'})


@bottle.post('/move')
def move():
data = bottle.request.json

	"""
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
	print(json.dumps(data))

	snakeDataJson = json.dumps(x)
	snakeData = json.loads(snakeDataJson)

	board_x = snakeData['board']['width'] - 1 
	board_y = snakeData['board']['height'] - 1

	snake_x = snakeData['you']['body'][0]['x']
	snake_y = snakeData['you']['body'][0]['y']
    
	possible_direction = ['down', 'left', 'up' 'right']

	if(snake_x == 0):
		possible_direction.remove('left')
    if (snake_x == board_x):
		possible_direction.remove('right')
    if (snake_y == 0):
		possible_direction.remove('up')
    if (snake_y == board_y):
		possible_direction.remove('left')
    
	direction = random.choice(possible_directions)
    
	return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
