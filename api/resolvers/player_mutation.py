from ..models.models import Player
from ariadne import convert_kwargs_to_snake_case

def create_player(*_, name):
    pass

@convert_kwargs_to_snake_case
def update_player(*_, score=None, has_cow=None, answer=None):
    pass