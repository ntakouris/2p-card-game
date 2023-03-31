import contextlib

from io import StringIO


from game.card import Card
from game.game import Game


def test_game_play_round():
    game = Game()

    game.p1_cards = [Card(10), Card(2)]
    game.p2_cards = [Card(9), Card(5)]

    with contextlib.redirect_stdout(StringIO()) as stdout:
        game.play_round()

        stdout_content = stdout.getvalue().rstrip("\n")
        assert (
            stdout_content == "Player 1: 10 | Player 2: 9 --> Player 1 wins this round."
        )

    assert game.p1_score == 1
    assert game.p2_score == 0

    assert game.p1_cards == [Card(2)]
    assert game.p2_cards == [Card(5)]

    with contextlib.redirect_stdout(StringIO()) as stdout:
        game.play_round()

        stdout_content = stdout.getvalue().rstrip("\n")
        assert (
            stdout_content == "Player 1: 2 | Player 2: 5 --> Player 2 wins this round."
        )

    assert game.p1_score == 1
    assert game.p2_score == 1

    assert game.p1_cards == []
    assert game.p2_cards == []


def test_game_play_game():
    game = Game()

    game.p1_cards = [Card(10), Card(2)]
    game.p2_cards = [Card(9), Card(5)]

    game.play_game()

    assert game.p1_score == 1
    assert game.p2_score == 1


def test_play_game_print_results():
    game = Game()

    game.p1_cards = []
    game.p2_cards = []

    game.p1_score = 10
    game.p2_score = 10

    with contextlib.redirect_stdout(StringIO()) as stdout:
        game.play_game()

        stdout_content = stdout.getvalue().rstrip("\n").split("\n")
        assert stdout_content[0] == "Final Score - Player 1: 10 | Player 2: 10"
        assert stdout_content[1] == "The game is a draw!"

    game.p1_score = 11
    game.p2_score = 10

    with contextlib.redirect_stdout(StringIO()) as stdout:
        game.play_game()

        stdout_content = stdout.getvalue().rstrip("\n").split("\n")
        assert stdout_content[0] == "Final Score - Player 1: 11 | Player 2: 10"
        assert stdout_content[1] == "Player 1 wins the game!"

    game.p1_score = 10
    game.p2_score = 11

    with contextlib.redirect_stdout(StringIO()) as stdout:
        game.play_game()

        stdout_content = stdout.getvalue().rstrip("\n").split("\n")
        assert stdout_content[0] == "Final Score - Player 1: 10 | Player 2: 11"
        assert stdout_content[1] == "Player 2 wins the game!"


def test_smoke_game():
    game = Game()
    game.play_game()

    assert (game.p1_score + game.p2_score) == 26  # (52 // 2)
