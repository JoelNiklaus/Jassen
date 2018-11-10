import pytest

from pyschieber.player.challenge_player.challenge_player import ChallengePlayer
from pyschieber.player.greedy_player.greedy_player import GreedyPlayer
from pyschieber.player.ppo_player.ppo_player import PPOPlayer
from pyschieber.player.random_player import RandomPlayer
from tests.example.statistical_helper import run_statistics


@pytest.mark.statistical
def test_against_random():
    players = [PPOPlayer(name='PPO1'), RandomPlayer(name='Random1'), PPOPlayer(name='PPO2'),
               RandomPlayer(name='Random2')]
    run_statistics(players=players)


@pytest.mark.statistical
def test_against_greedy():
    players = [PPOPlayer(name='PPO1'), GreedyPlayer(name='Greedy1'), PPOPlayer(name='PPO2'),
               GreedyPlayer(name='Greedy2')]
    run_statistics(players=players)


@pytest.mark.statistical
def test_against_challenge():
    players = [PPOPlayer(name='PPO1'), ChallengePlayer(name='Challenge1'), PPOPlayer(name='PPO2'),
               ChallengePlayer(name='Challenge2')]
    run_statistics(players=players)
