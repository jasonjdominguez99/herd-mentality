from ..models.models import Player

def get_players(*_):
    return [player.to_dict() for player in Player.query.all()]