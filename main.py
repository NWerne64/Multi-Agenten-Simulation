from model import AoELiteModel  # Importieren der Modellklasse
import pygame  # Importieren von pygame für die Clock

# Simulationsparameter
GRID_WIDTH = 100
GRID_HEIGHT = 100
NUM_AGENTS = 10
SIMULATION_STEPS = 300  # Anzahl der Schritte
FPS = 10  # Bilder pro Sekunde für die Visualisierung

if __name__ == '__main__':
    # Modell initialisieren
    model = AoELiteModel(GRID_WIDTH, GRID_HEIGHT, NUM_AGENTS)

    print(
        f"Starte Simulation mit {NUM_AGENTS} Agenten auf einem {GRID_WIDTH}x{GRID_HEIGHT} Grid für {SIMULATION_STEPS} Schritte.")

    # Haupt-Simulationsschleife
    # Mesa's eingebaute `model.run_model()` ist nicht ideal für benutzerdefinierte PyGame-Integration.
    # Daher steuern wir die Schleife und das Rendering manuell.

    clock = pygame.time.Clock()  # PyGame Clock für FPS-Steuerung

    for i in range(SIMULATION_STEPS):
        if not model.running:  # Prüfen, ob das Modell (z.B. durch Schließen des Fensters) gestoppt wurde
            break

        model.step()  # Führt einen Schritt im Modell aus (Agenten-Aktionen + Rendering)

        clock.tick(FPS)  # Begrenzt die Schleife auf die angegebene FPS

    print("Simulation beendet.")
    pygame.quit()  # PyGame sauber beenden