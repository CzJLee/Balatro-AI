import mini_balatro

game = mini_balatro.Game(seed=0)
game.new_round()

print(game.hand)
game.discard_cards([4, 5, 6, 7])
game.discard_cards([2, 4, 6, 7])
game.discard_cards([0, 5, 6, 7])
game.play_hand([3, 5, 6, 7])
game.play_hand([0, 1, 3, 4, 5])
