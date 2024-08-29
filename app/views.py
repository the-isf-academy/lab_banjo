from banjo.urls import route_get, route_post
from .models import Riddle
from settings import BASE_URL

@route_get(BASE_URL + 'all')
def list_riddles(args):
    riddles = []

    if len(Riddle.objects.all())  > 0:

        for riddle in Riddle.objects.all():
            riddles.append(riddle.json_response_answerless())

        return {'riddles':riddles}
    
    else:
        return {'error': 'no riddles exist'}


@route_post(BASE_URL + 'new', args={'question': str, 'answer': str})
def new_riddle(args):    

    new_riddle = Riddle(
        question = args['question'],
        answer = args['answer'],
        guesses = 0,
        correct = 0
    )

    new_riddle.save()

    return {'riddle': new_riddle.json_response()}
