# Jassen

## Properties
- One round is finished after 36 cards --> trajectory finished fast, no continuous action space
- lots of variance due to randomly dealt cards. But the more cards have been played, the more cards we can guess
- Unsure about effectiveness of planning

## Simplification
- only obeabe
- only two players
- only stichs give points

## Notes



Exploration not needed maybe (because of randomness in dealt cards)

Start with only two players

Smooth value function in backgammon due to randomness


Assume binary tree for jassen: 2^(k+1)-1 nodes to visit --> Because of randomness, unfeasible to lookup entire tree

Maybe adapt loss function to push network into specific direction

Use Smooth UCT

Card embedding analogous to word embedding (word2vec)

Pondering (Thinking during opponent's time)

Group card combinations like Libratus
Bet combinations not necessary


Create Open Computer Jassen Competition analogous to ACPC (Annual Computer Poker Competition)


Learning Rules should be easily possible:
- No planning necessary
- Can be trained in a supervised way
- Instant reward



Number of possibilities to distribute 36 cards to 4 players:
9 cards to first stack: 36 choose 9 = 94143280
9 cards to second stack: 27 choose 9 = 4686825
9 cards to third stack: 18 choose 9 = 48620
9 cards to fourth stack: 9 choose 9 = 1
Possibilities to assign stacks to players: 4! = 24
Final result: 94143280 * 4686825 * 48620 * 1 * 24 = 5.1486605e+20

first round:
1st move: 9 possibilities
2nd move: on average 9 / 4 possibilities
3rd move: on average 9 / 4 possibilities
4th move: on average 9 / 4 possibilities
9 * 2 * 2 * 2

second round:
1st move: 8 possibilities
2nd move: on average 8 / 4 possibilities
3rd move: on average 8 / 4 possibilities
4th move: on average 8 / 4 possibilities

8 * 2 * 2 * 2

etc. 
possibilities of 2nd, 3rd and 4th move difficult to guess --> simplicity: always 2 possibilities

Playout approximately: 9! * 9 * 2 * 2 * 2 = 26127360


Total: 94143280 * 4686825 * 48620 * 1 * 24 * 26127360 = 1.3452091e+28




