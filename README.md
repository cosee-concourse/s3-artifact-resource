# S3 Archive Resource

[![Build Status](https://travis-ci.org/cosee-concourse/s3-artifact-resource.svg?branch=master)](https://travis-ci.org/cosee-concourse/s3-artifact-resource) [![Docker Repository on Quay](https://quay.io/repository/cosee-concourse/s3-artifact-resource/status "Docker Repository on Quay")](https://quay.io/repository/cosee-concourse/s3-artifact-resource)

Compresses artifacts and archives the compressed file in an S3 bucket

## Source Configuration

* `bucket`: *Required.* The name of the bucket.

* `access_key_id`: *Required.* The AWS access key to use when accessing the
  bucket.

* `secret_access_key`: *Required.* The AWS secret key to use when accessing
  the bucket.

* `region_name`: *Required.* The region the bucket is in. Defaults to
  `us-east-1`.

### File Names

* `filename`: *Required* Prefix of the data name to be used for the compressed file in S3 bucket. 
  It should be without version and data extension because they are added at `out`. To version the files, the `semver` resource
  is required. The final filename in the S3 bucket is: 
 `filename` `version`.tar.gz

## Behavior

### `check`: Extract versions from the bucket.

The compressed files are found with the `filename`. The versions in the file names
will be used to order them (using [semver](http://semver.org/)). Each
object's filename is the resulting version.

### `in`: Fetches artifacts from the bucket.

* Uncompresses and places files to destination. Uses gzip as compression.

#### Parameters

*None.*

### `out`: Upload artifacts as archive to the bucket.

Given a folder specified by `folderpath`, compresses folder contents and uploads compressed fly it to the S3 bucket.
Reads semver version from specified file `version` to generate the versioned name.

#### Parameters
 
* `version`: *Required* Filepath to `semver` version file
 
* `folderpath`: *Required* Path to folder that contains artifacts
