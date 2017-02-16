# S3 Archive Resource

[![Build Status](https://travis-ci.org/cosee-concourse/s3-artifact-resource.svg?branch=master)](https://travis-ci.org/cosee-concourse/s3-artifact-resource)

[![Docker Repository on Quay](https://quay.io/repository/cosee-concourse/s3-artifact-resource/status "Docker Repository on Quay")](https://quay.io/repository/cosee-concourse/s3-artifact-resource)

Archives versions objects in an S3 bucket

## Source Configuration

* `bucket`: *Required.* The name of the bucket.

* `access_key_id`: *Required.* The AWS access key to use when accessing the
  bucket.

* `secret_access_key`: *Required.* The AWS secret key to use when accessing
  the bucket.

* `region_name`: *Optional.* The region the bucket is in. Defaults to
  `us-east-1`.

### File Names

One of the following two options must be specified:

* `regexp`: *Optional.* The pattern to match filenames against within S3. The first
  grouped match is used to extract the version, or if a group is explicitly
  named `version`, that group is used. At least one capture group must be
  specified, with parentheses.

  The version extracted from this pattern is used to version the resource.
  Semantic versions, or just numbers, are supported. Accordingly, full regular
  expressions are supported, to specify the capture groups.

## Behavior

### `check`: Extract versions from the bucket.

Objects will be found via the pattern configured by `regexp`. The versions
will be used to order them (using [semver](http://semver.org/)). Each
object's filename is the resulting version.

### `in`: Fetch an object from the bucket.

Places the following files in the destination:

* `(filename)`: Unpacked .

#### Parameters

*None.*

### `out`: Upload an object to the bucket.

Given a file specified by `file`, upload it to the S3 bucket.

#### Parameters
 
* `version`: 
 
* `folderpath`: 


## Deutsch

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
