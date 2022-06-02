from models.models import Player
from ariadne import convert_kwargs_to_snake_case
import uuid

def create_player(*_, name):
    unique_id = uuid.uuid4()
    return Player(unique_id.int, name)

@convert_kwargs_to_snake_case
def update_player(_, info, score=None, has_cow=None, answer=None):
    current_player = info.context.player
    if score != None:
        current_player.add_to_score(score)
    if has_cow != None:
        current_player.update_has_cow(has_cow)
    if answer != None:
        current_player.update_answer(answer)
    
    return current_player