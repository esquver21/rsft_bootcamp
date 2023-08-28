def get_hidden_card(card_id, ln_secret=4):
    return ln_secret * "*" + card_id[-4:]