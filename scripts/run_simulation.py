from game import Game


def run_simulation() -> None:
    game = Game()

    game.play_until_end()


if __name__ == "__main__":
    run_simulation()
