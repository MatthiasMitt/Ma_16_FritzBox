Ma_16_FritzBox
==============

Zustand iPad mit Pythonista: in Arbeit
        iMac:                in Arbeit
        andere Platformen:   nicht begonnen


Vorbereitung
------------

Pad,iPhose:
Installiere "fritzboxconnection" in "site-packages-3".

( Wie ich dass vor einigen Jahren hinbekommen habe, habe ich vergessen. )

iMac:
Update python3 von 3.8.2 auf 3.12.3 .
Danach:
pip3 install fritzconnection 

Man muss aus "boxen_Muster.py" eine Datei "boxen.py" mit echten Daten herstellen.

Programme
---------

*** Ma_16_einfacheAnfragen ***

iPAD,IPhone:
Einfache Anfragen funktionieren auch mit dem damals installierten fritzboxconnection. Vorher muss aber aus "boxen_Muster.py" eine Datei "boxen.py" mit echten Daten hergestellt werden.

iMac:
Funktioniert auch, nur  FritzHosts  fehlt

*** Ma_16_Plattform.py ***

Hilfsprogramm, um platformabhängigen Code schreiben zu können.


*** Ma_16_ZeigeAlles.py ***

Versuche möglichst viel aus den Fritzboxen herauszulesen.

iPad,iPhone,iMac:
Lebenstüchtig, aber nicht alle Funktionen liefern tatsächlich.


