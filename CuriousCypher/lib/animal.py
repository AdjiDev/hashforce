class AnimalList:
    def __init__(self):
        self.animals = {
            "mammals": [
                "lion", "tiger", "elephant", "bear", "wolf", "giraffe",
                "zebra", "kangaroo", "whale", "dolphin", "monkey", 
                "rabbit", "cat", "dog", "hamster", "bat"
            ],
            "birds": [
                "sparrow", "eagle", "parrot", "penguin", "owl", 
                "flamingo", "hummingbird", "peacock", "canary", 
                "vulture", "seagull", "crow", "finch", "swallow"
            ],
            "reptiles": [
                "snake", "lizard", "crocodile", "turtle", "gecko", 
                "chameleon", "iguana", "monitor lizard", "alligator"
            ],
            "amphibians": [
                "frog", "toad", "salamander", "newt", "axolotl"
            ],
            "fish": [
                "shark", "salmon", "tuna", "goldfish", "catfish", 
                "trout", "bass", "herring", "carp", "mackerel"
            ],
            "insects": [
                "butterfly", "bee", "ant", "beetle", "mosquito", 
                "dragonfly", "grasshopper", "moth", "ladybug", 
                "cockroach"
            ]
        }

    def get_animals(self, category=None):
        """Return a list of animals, optionally filtered by category."""
        if category:
            return self.animals.get(category, [])
        return {k: v for k, v in self.animals.items()}