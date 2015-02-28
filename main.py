__author__ = 'Julius'

# Alles aus TKinter importieren
from tkinter import *
import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from html.parser import HTMLParser
import time
import datetime

# Ordner zum speichern der Bilder anlegen
if not os.path.exists('bilder'):
            os.makedirs("bilder")


def get_date_string():
    unformatierte_zeit = time.time()
    formatierte_zeit = datetime.datetime.fromtimestamp(unformatierte_zeit).strftime('%Y-%m-%d-%H-%M-%S')
    return formatierte_zeit


counter = 0


def get_filename(ending):
    global counter
    filename = get_date_string() + "-" + str(counter) + ending
    counter += 1
    return str(filename)


# Eigener Parser für die Homepage
class MyParser(HTMLParser):

    m_url = ""

    def __init__(self, url):
        self.m_url = url
        super().__init__()

    def handle_starttag(self, tag, attrs):
        for index, value in attrs:
            if index == "href" or index == "src":
                if str(value).endswith(".jpg") or str(value).endswith(".gif") or str(value).endswith(".png"):

                    if str(value).startswith("/"):
                        bildname = str.format("{0}{1}", self.m_url, value)
                    else:
                        bildname = value

                    if bildname.endswith('.jpg'):
                        try:
                            jpg_name = 'bilder/' + get_filename(".jpg")
                            urlretrieve(bildname, jpg_name)
                            print("Bild gefunden jpg")
                        except:
                            print("Fehler jpg")

                    elif bildname.endswith('.gif'):
                        try:
                            gif_name = 'bilder/' + get_filename(".gif")
                            urlretrieve(bildname, gif_name)
                            print("Bild gefunden gif")
                        except:
                            print("Fehler gif")

                    elif bildname.endswith('.png'):
                        try:
                            png_name = 'bilder/' + get_filename(".png")
                            urlretrieve(bildname, png_name)
                            print("Bild gefunden png")
                        except:
                            print("Fehler png")


# Funktion des Buttons "durchsuchen"
def button_suchen_click():
    print("Zu oeffnende Homepage: %s" % urlEingabe.get())
    # versuche das html file herunterzuladen
    try:
        download = str(urlopen("http://%s" % urlEingabe.get()).read())
    except:
        print("Fehler beim download")
        return 0
    parser = MyParser(download)
    parser.feed(download)


# neues fenster erstellen
root = Tk()
root.title = "Homepage Parser"

# url eingabe
Label(root, text="URL").grid(row=1, column=0)
urlEingabe = Entry(root)
urlEingabe.insert(0, "www.wetter.com/deutschland/mannheim/DE0006670.html")
urlEingabe.grid(row=1, column=1)

# Button "durchsuchen"
buttonSucheStarten = Button(root, text="Durchsuchen", command=lambda: button_suchen_click())
buttonSucheStarten.grid(row=1, column=2)

# fenster anzeigen
root.mainloop()






