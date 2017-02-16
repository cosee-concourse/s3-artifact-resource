# S3 Archiv Resource

Archiviert Versionsobjekte in einem S3 Bucket.

## Source Configuration

* `bucket`: *Benötigt.* Name des Buckets.

* `access_key`: *Benötigt.* Der AWS access key, welcher für den Zugriff auf den 
  Bucket benutzt werden soll.

* `secret_access_key`: *Benötigt.* Der AWS secret key, welcher für den 
  Zugriff auf den Bucket benutzt werden soll

* `region_name`: *Benötigt.* Die Region in dem sich der Bucket befindet. 
  Standardmäßig `us-east-1`, wenn nicht anders spezifiziert.

### Datei Namen

* `filename`: *Benötigt* Prefix des Dateinamen im spezifizierten S3 Bucket. 
  Ohne Version und Dateiendung. Zur Versionierung wird die `semver` Resource
  benötigt. Der endgültiger Dateiname in S3 setzt sich wie folgt zusammen: 
 `filename` `version`.tar.gz

## Verhalten

### `check`: Extrahiert Versionen aus S3.

* Dateien werden gefunden durch den spezifizierten `filename`. 
  Die Versionen werden benutzt um die Dateien zu sortieren 
  (mit [semver](http://semver.org/)). Der Dateiname jedes Objekts ist die
  resultierende Version.

### `in`: Lädt eine Datei aus S3 herunter.

* Entpackt und platziert die folgenden Dateien am Zielort. Benutzt gzip als
  Kompressionseinstellung.

#### Parameter

*None.*

### `out`: Lädt eine Datei nach S3 hoch.

* Komprimiert die Dateien welche sich am angegebenen Pfad befinden und lädt sie
  in den S3 hoch. 

#### Parameter

* `version`: *Benötigt.* Die Version der hochzuladenden Datei.
 
* `folderpath`: *Benötigt.* Der Dateipfad an dem sich der zu komprimierende
  Ordner bzw. die zu kompriemierende Datei befinden.
