Ma_16_FritzBox
==============

Zustand iPad mit Pythonista: in Arbeit
        iMac:                in Arbeit
        andere Platformen:   nicht begonnen


Vorbereitung
------------

*** fritzconnection ***

"fritzconnection" ist von Klaus Bremer (und vielleicht Helfern) und
wurde auf https://github.com/kbr/fritzconnection
gefunden.

*** iPad,iPhone: ***
installierte App "Pythonista" Version 3.4 benutzt Python 3.10

Installiere "fritzboxconnection" in "site-packages-3".

( Wie ich das vor einigen Jahren hinbekommen habe, habe ich vergessen. )
gelandet in
Pythonista/This iPad/site-packages-3/fritzconnection
Version scheinbar: 1.3.4

*** iMac: ***
Update python3 von 3.8.2 auf 3.12.3 .
Danach:
pip3 install fritzconnection 
gelandet in
/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/fritzconnection
Version scheinbar: 1.13.2

*** boxen ***
Man muss aus "boxen_Muster.py" eine Datei "boxen.py" mit echten Daten herstellen.

Programme
---------

*** Ma_16_einfacheAnfragen ***

iPAD,IPhone:
Einfache Anfragen funktionieren auch mit dem damals installierten fritzboxconnection.

iMac:
Funktioniert auch, nur  FritzHosts  fehlt (Kann nicht importiert werden,)

*** Ma_16_Plattform.py ***

Hilfsprogramm, um platformabhängigen Code schreiben zu können. Die sind
jetzt aber nach ../Ma_Util umgezogen und heissen nur noch
'Ma_Plattform.py'.


*** Ma_16_ZeigeAlles.py ***

Versuche möglichst viel aus den Fritzboxen herauszulesen.

iPad,iPhone,iMac:
Lebenstüchtig, aber nicht alle Funktionen liefern tatsächlich.
Details in 
Ma_16_ZeigeAlles.Testergebnis.txt

'import' so umgebaut, dass es funktioniert, egal von wo und wie
das Programm aufgerufen wurde.

