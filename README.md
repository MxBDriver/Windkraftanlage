# Windkraftanlage 

Hier wurde ein einfaches Programm geschrieben, um eine rotierende Windkraftanlage darzustellen.
Im Release Ordner ist das fertige Python Programm als ausführbare EXE-Datei.
* windkraftanlage.exe

Der Code wurde überarbeitet, da Umlaute in den Kommentaren zu finden waren und diese Probleme beim Umwandeln gemacht haben.
Zudem wurde ein passendes Fenstericon wurde eingepflegt.

Aktuell wird ein Konsolen Fenster mit geöffnet, um die Geschwindigkeit anzuzeigen und Fehler auszugeben.
Möchte man das Konsolen Fenster nicht haben beim Programmablauf, kann man die EXE-Datei neu kompilieren mit pyinstaller. 
Das geht wie folgt:
* Repository herunterladen.
* Dann im ".\Scripts" Ordner die CMD aufrufen und mit dem Befehl $"activate.bat" wird dann die Virtuelle Umgebung aktivirt.
* Danach muss man in den ".\Release" Ordner navigieren und hier auch wieder die CMD aufrufen.
* Hier muss nun zunächst die "windkraftanlage.spec" bearbeitet werden.
* In Zeile 38 muss man "console=True" in "console=False" ändern und die Datei danach abspeichern.
* Nun kann man in der CMD im ".\Release" Ordner den Befehl $"pyinstaller windkraftanlage.spec --distpath "./" " ausführen und warten bis es abgeschlossen ist.

Wenn man jetzt die windkraftanlage.exe ausführt, dürfte das Konsolen Fenster nicht mehr erscheinen.

Viel Spaß mit dem Programm.
