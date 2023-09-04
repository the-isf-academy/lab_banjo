from banjo.urls import route_get, route_post
from .models import Riddle


@route_get('riddles/all')
def list_riddles(params):
    riddles = []

    if len(Riddle.objects.all())  > 0:

        for riddle in Riddle.objects.all():
            riddles.append(riddle.to_dict_answerless())

        return {'riddles':riddles}
    
    else:
        return {'error': 'no riddles exist'}


@route_post('riddles/new', args={'question': str, 'answer': str})
def create_riddle(params):    
    riddle = Riddle.from_dict(params)

    riddle.save()
    return {'riddle':riddle.to_dict()}
