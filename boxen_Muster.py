# boxen_Muster.py

# Eine Liste aller Fritzboxen, an die ich mich vielleicht anmelden kann.
#
# Diese Datei sollte nach 'boxen.py' kopiert werden,
# und dann die echten IP-Adressen, Benuzernamen und Passworte eingetragen
# werden.

#            mein Name für eine FritzBox ,
#            :                 IP-Adresse im eigenen Netz ,
#            :                 :                  Teil des Modellnamens ,
#            :                 :                  :  Benutzer-Id auf der Fritzbox ,
#            :                 :                  :      :        Passwort 
#            :                 :                  :      :        :
boxen = [ [ 'Fritz_am_Ort1' , '192.168.184.1'  , '7530','user1' ,'Passwort1'  ]
        , [ 'Fritz_am_Ort2' , '192.168.178.1'  , '7360','user21','Passwort21' ]
        , [ 'Hilfsbox_Ort2' , '192.168.178.22' , '7270','user22','Passwort22' ]
        ]
