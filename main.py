__author__ = 'Julius'

# Alles aus TKinter importieren
from tkinter import *
import urllib
import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from html.parser import HTMLParser

# Ordner zum speichern der Bilder anlegen
if not os.path.exists('bilder'):
            os.makedirs("bilder")


# Eigener Parser für die Homepage
class MyParser(HTMLParser):
    zaehler = 0

    def handle_starttag(self, tag, attrs):
        for index, value in attrs:
            if index == "href" or index == "src":
                if str(value).endswith(".jpg") or str(value).endswith(".gif") or str(value).endswith(".png"):
                    if str(value).startswith("/"):
                        bildname = str.format("{0}{1}", "hallo", value)
                    else:
                        bildname = value
                    # print(bildname)
                    if bildname.endswith('.jpg'):
                        try:
                            urlretrieve(bildname, "bilder/%d.jpg" % MyParser.zaehler)
                            MyParser.zaehler += 1
                            print("Bild gefunden png")
                        except:
                            print("Fehler")
                    elif bildname.endswith('.gif'):
                        try:
                            urlretrieve(bildname, "bilder/%d.gif" % MyParser.zaehler)
                            MyParser.zaehler += 1
                            print("Bild gefunden png")
                        except:
                            print("Fehler")
                    elif bildname.endswith('.png'):
                        try:
                            urlretrieve(bildname, "bilder/%d.png" % MyParser.zaehler)
                            MyParser.zaehler += 1
                            print("Bild gefunden png")
                        except:
                            print("Fehler")


# Funktion des Buttons "durchsuchen"
def button_suchen_click():
    print("Zu oeffnende Homepage: %s" % urlEingabe.get())
    # versuche das html file herunterzuladen
    try:
        download = str(urlopen("http://%s" % urlEingabe.get()).read())
    except:
        print("Fehler beim download")
        return 0
    parser = MyParser()
    parser.feed(download)


# neues fenster erstellen
root = Tk()
root.title = "Homepage Parser"

# url eingabe
Label(root, text="URL").grid(row=1, column=0)
urlEingabe = Entry(root)
urlEingabe.grid(row=1, column=1)

# Button "durchsuchen"
buttonSucheStarten = Button(root, text="Durchsuchen", command=lambda: button_suchen_click())
buttonSucheStarten.grid(row=1, column=2)

# fenster anzeigen
root.mainloop()






