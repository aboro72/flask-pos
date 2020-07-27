# flask-pos

für Datenbank mal ruhig in das Wiki schauen

<b> Ein Hinweis </b>
  
  Bitte im produktive Bereich später (noch) mit gunicorn start:app auf Raspian starten.
  Sollte Mathias in der zwischen Zeit eine andere Lösung gefunden/geschrieben haben ....
  
<h3>Folgenes muss für Python3 nachgeladen werden</h3>

<p><b>flask-login: </b> pip3 install flask-login</p>
<p><b>flask-Appbuilder: </b>pip3 install flask-appbuilder</p>

<h4>Optional:</h4>

<p><b> flask-admin: </b> pip3 install flask-admin</p>

<h4>Flask Starten: </h4>

im git Ordner ./start.sh ausführen und im Browser deiner Wahl
 http://localhost:5000/ eingeben.
 
 #### Umgebung ändern:
 
 In der Shell Variablen setzen
 
 `export FLASK_ENV=production` -> Produktionsumgebung
 
 `export FLASK_ENV=testing`    -> Testumgebung
 
 `export FLASK_ENV=development`-> Entwicklungsumgebung
 
