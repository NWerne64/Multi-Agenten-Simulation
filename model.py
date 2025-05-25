from mesa import Model
from mesa.space import MultiGrid
from agent import WorkerAgent
import pygame
import random


class AoELiteModel(Model):
    """Das Hauptmodell für die 'Age of Empires Lite'-Simulation."""

    def __init__(self, width, height, num_agents):
        super().__init__()
        self.num_agents = num_agents
        self.grid_width = width
        self.grid_height = height
        self.grid = MultiGrid(width, height, torus=False)

        self._next_id_counter = 0  # Manueller Zähler für Agenten-IDs

        # PyGame Initialisierung (bleibt gleich)
        pygame.init()
        self.screen_width_px = 800
        self.screen_height_px = 600
        self.cell_size = min(self.screen_width_px // self.grid_width,
                             self.screen_height_px // self.grid_height)
        if self.cell_size == 0: self.cell_size = 1
        self.screen_width_px = self.cell_size * self.grid_width
        self.screen_height_px = self.cell_size * self.grid_height
        self.screen = pygame.display.set_mode((self.screen_width_px, self.screen_height_px))
        pygame.display.set_caption("Age of Empires Lite (Mesa 3.2.0) - Iteration 0")
        self.pygame_running = True
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.AGENT_COLOR = (0, 0, 255)

        # Agenten erstellen und platzieren
        for i in range(self.num_agents):
            agent_id = self.get_new_id()  # Verwende die neue Methode
            agent = WorkerAgent(agent_id, self)

            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def get_new_id(self):
        """Gibt eine neue, einzigartige ID für einen Agenten zurück."""
        self._next_id_counter += 1
        return self._next_id_counter

    def _draw_grid_lines(self):
        # ... (bleibt unverändert) ...
        for x_pos in range(0, self.screen_width_px, self.cell_size):
            pygame.draw.line(self.screen, self.BLACK, (x_pos, 0), (x_pos, self.screen_height_px))
        for y_pos in range(0, self.screen_height_px, self.cell_size):
            pygame.draw.line(self.screen, self.BLACK, (0, y_pos), (self.screen_width_px, y_pos))

    def _draw_agents(self):
        # ... (bleibt unverändert) ...
        for cell_contents, (x, y) in self.grid.coord_iter():
            if cell_contents:
                for agent_in_cell in cell_contents:
                    if isinstance(agent_in_cell, WorkerAgent):
                        rect = pygame.Rect(
                            x * self.cell_size,
                            y * self.cell_size,
                            self.cell_size,
                            self.cell_size
                        )
                        pygame.draw.rect(self.screen, self.AGENT_COLOR, rect)

    def _handle_pygame_events(self):
        # ... (bleibt unverändert) ...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.pygame_running = False
                self.running = False

    def render_pygame(self):
        # ... (bleibt unverändert) ...
        if not self.pygame_running:
            return
        self.screen.fill(self.WHITE)
        self._draw_grid_lines()
        self._draw_agents()
        pygame.display.flip()

    def step(self):
        """Führt einen Simulationsschritt aus."""
        self._handle_pygame_events()
        if not self.running:
            return

        self.agents.shuffle_do("step")
        self.render_pygame()