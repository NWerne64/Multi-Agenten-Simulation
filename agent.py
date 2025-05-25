from mesa import Agent
import random


class WorkerAgent(Agent):
    """Ein Agent, der Ressourcen sammelt (in späteren Iterationen)."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # In Iteration 0 sind keine speziellen Attribute notwendig.
        # Später: self.inventar = 0, etc.

    def move(self):
        """Bewegt den Agenten auf ein zufälliges Nachbarfeld."""
        # hole mögliche Nachbarfelder (Koordinaten)
        # self.pos ist die aktuelle Position des Agenten, die von Mesa's Grid verwaltet wird
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,  # Moore-Nachbarschaft (8 umgebende Zellen)
            include_center=False  # Die eigene Zelle nicht einschließen
        )

        # Wähle eine zufällige neue Position aus den möglichen Schritten
        # In Iteration 0 erlauben wir die Bewegung auf jedes Nachbarfeld,
        # MultiGrid erlaubt mehrere Agenten pro Zelle.
        if possible_steps:
            new_position = random.choice(possible_steps)
            self.model.grid.move_agent(self, new_position)

    def step(self):
        """Definiert die Aktion des Agenten in einem Simulationsschritt."""
        self.move()