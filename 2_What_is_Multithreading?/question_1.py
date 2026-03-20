"""
# Question 1

We’ve talked about how multithreading applications can work in the context of browser applications. Now imagine a multiplayer game server hosting arenas with multiple players. Which tasks could run in separate threads? For example: player input processing, physics updates, matchmaking, and networking.

# Answer

You can imagine each arena in the game as a class, and each task as a function. When we start the game, an arena is created (i.e. a process), and threads are created to run tasks.

A code example (just for player input processing) can look like this:

"""

from threading import Thread

class Player:
    def __init__(self, name):
        self.name = name
        self.state = {}
    
    def accept_keyboard_input(self, input):
        # Code to accept player input
        self.update_state(input)

    def update_state(self, input):
        # Code to update player state based on input
        pass


class GameArena:
    def __init__(self):
        # Initialize the arena and its resources
        self.players = []
        self.threads = []

    def process_player_input(self, player: Player):
        # Code to process player input
        pass

    def add_player(self, player: Player):
        self.players.append(player)
        t = Thread(target=self.process_player_input, args=(player,))
        self.threads.append(t)
    
    def start(self):
        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()

fun_game = GameArena()
fun_game.add_player(Player("Alice"))
fun_game.add_player(Player("Bob"))
fun_game.start()

"""
# Question 1.5

A step further, how might multithreading occur with training a large language model (LLM) on a GPU with many cores? What parts of the LLM could we allocate to individual threads?

# Answer

An LLM typically contains several transformer blocks (Attention + MLP). We can allocate the different replicas of these transformer blocks to individual threads, effectively splitting the model into different layers (this is also known as model parallelism).

When we then train the model, we can aggregate the gradients across the different threads and update the model parameters accordingly. This allows us to efficiently utilize the GPU's resources and speed up the training process.

A code example (using PyTorch sequential models for simplicity) can look like this:

"""

import torch
import torch.nn as nn

# This code assumes you have at least 2 GPUs available; if not, swap 'cuda:0'/'cuda:1' with 'cpu' to illustrate the concept without the hardware requirement)

# Define two halves of a simple model, each on a different device 
class PipelinedModel(nn.Module):
    def __init__(self):
        super().__init__()
        # First half of the model on GPU 0
        self.block1 = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU()
        ).to('cuda:0')

        # Second half of the model on GPU 1
        self.block2 = nn.Sequential(
            nn.Linear(256, 128),
            nn.ReLU()
        ).to('cuda:1')

    def forward(self, x):
        # Pass through block1 on GPU 0, then move output to GPU 1
        x = self.block1(x)
        x = x.to('cuda:1')
        x = self.block2(x)
        return x

model = PipelinedModel()

# Dummy input on GPU 0
x = torch.randn(32, 512).to('cuda:0')
output = model(x)
