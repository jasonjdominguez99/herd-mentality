from ..models.models import Card
import random

def get_card(*_):
    available_card_ids = [card.id for card
                          in Card.query.filter_by(has_been_picked=False).all()]

    random.seed()
    rand_idx = random.randint(0, len(available_card_ids) - 1)
    rand_card_id = available_card_ids[rand_idx]

    return Card.query.filter_by(id=rand_card_id)
    