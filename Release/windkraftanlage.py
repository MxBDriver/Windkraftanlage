import pygame
import time
import threading
import sys

# Initialisiere Pygame
pygame.init()

# Fenstergroesse, Fensterbezeichnung und Fenstericon festlegen
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotierende Windkraftanlage")
img_icon = pygame.image.load("icon_windrad.png")

pygame.display.set_icon(img_icon)

# Geschwindigkeit der Windrad Rotation
speed = 5

# Funktion zum Einlesen der Geschwindigkeit aus der speed.txt-Datei
def read_speed():
    while True:
        try:
            with open("speed.txt", "r") as file:
                line = file.readline()
                if line:
                    # Konvertiere die gelesene Geschwindigkeit in eine Gleitkommazahl
                    new_speed = float(line.strip())
                    # Ueberpruefe, ob die neue Geschwindigkeit im gueltigen Bereich liegt
                    if 1 <= new_speed <= 10:
                        global speed
                        speed = new_speed
        except Exception as e:
            # Fehlerbehandlung fuer den Dateizugriff
            print("Fehler beim Lesen der Geschwindigkeit:", str(e))
            print("Bitte stellen Sie sicher, dass die Datei 'speed.txt' vorhanden ist.")
            print("In die Datei 'speed.txt' sollte eine Geschwindigkeit zwischen 1.0 und 10.0 angegeben werden.")
            print("Nach der Eingabe muss die 'speed.txt' Datei gespeichert werden, alternativ mit der Tastenkombination 'strg + s' .")

        # Konsolenausgabe der aktuellen Geschwindigkeit
        print("Die Windkraftanlage dreht sich mit Geschwindigkeit: ", speed)
        
        # Warte fuer 5-10 Sekunden, bevor die Geschwindigkeit erneut eingelesen wird
        time.sleep(5 + time.time() % 5)
        

# Funktion zum Zeichnen des rotierenden Windrads
def draw_windrad(rotation):
    # Fenster Mittelpunkt in x und y festlegen
    center_x = width // 2
    center_y = height // 2
    # Windrad laden und weissen Hintergrund entfernen
    img_blades = pygame.image.load("windmill-blades.jpg").convert()
    img_blades.set_colorkey((255,255,255))

    # Windrad Turm laden und zeichnen
    img_tower = pygame.image.load("windmill-tower.jpg").convert()
    #img_tower.set_colorkey((255,255,255))
    screen.blit(img_tower,(center_x - int(img_tower.get_width() / 2 ), center_y - 65 ))


    # Rotation des Windrads
    img_rotate = pygame.transform.rotate(img_blades, rotation)
    # Anzeigen des rotierenden Windrads in der Mitte vom Fenster
    screen.blit(img_rotate,(center_x - int(img_rotate.get_width() / 2 ), center_y - int(img_rotate.get_height() / 2)))


# Hintergrundthread zum Einlesen der Geschwindigkeit
speed_thread = threading.Thread(target=read_speed)
speed_thread.daemon = True  # Setze den Hintergrundthread als aktiven Hintergrundthread, dadurch kann der Hintergrundthread auch beendet werden, wenn das Hauptprogramm schliesst
speed_thread.start()


# Hauptschleife
running = True
clock = pygame.time.Clock() # Wird fuer die Aktualisierungsrate vom Programmfenster benoetigt
rotation = 0.0  # Anfangsrotation des Windrads
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Aktualisiere die Rotation basierend auf der aktuellen Geschwindigkeit
    rotation += speed
    
    # Zeichne den Hintergrund in weiss
    screen.fill((255, 255, 255))
    
    # Zeichne das Windrad
    draw_windrad(rotation)
    
    # Aktualisiere das Display
    pygame.display.flip()
    
    # Begrenze die Framerate auf 60 FPS
    clock.tick(60)

# Beende Pygame
pygame.quit()

# Beende den Hintergrundthread
sys.exit()