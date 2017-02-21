# S3 Artifact Resource

[![Build Status](https://travis-ci.org/cosee-concourse/s3-artifact-resource.svg?branch=master)](https://travis-ci.org/cosee-concourse/s3-artifact-resource) [![Docker Repository on Quay](https://quay.io/repository/cosee-concourse/s3-artifact-resource/status "Docker Repository on Quay")](https://quay.io/repository/cosee-concourse/s3-artifact-resource)

Compresses artifacts and archives them compressed in an S3 bucket

## Source Configuration

* `bucket`: *Required.* The name of the S3 bucket.

* `access_key_id`: *Required.* The AWS access key to use when accessing the
  bucket.

* `secret_access_key`: *Required.* The AWS secret key to use when accessing
  the bucket.

* `region_name`: *Required.* The region the bucket is in.

* `filename`: *Required* Prefix of the filename to be used for the compressed file in the S3 bucket. 
  At the moment folders are not supported.
  It should be without version and data extension because they are added at `out`. To version the files, the `semver` resource
  is required. The final filename (key) in the S3 bucket is: 
 `filename` `version`.tar.gz

## Behavior

### `check`: Extract versions of the archives from the bucket.

The compressed files are found with the `filename`. The versions in the file names
will be used to order them (using [semver](http://semver.org/)). Each
object's filename is the resulting version of the resource.

### `in`: Fetches artifacts from the bucket.

* Uncompresses and places files to destination. Uses gzip as compression.

#### Parameters

*None.*

### `out`: Upload artifacts as archive to the bucket.

Given a folder specified by `folderpath` (this must be available to the resource - for example created by a task that is run before the
put request), compresses folder contents and uploads compressed archive to the S3 bucket.
Reads semantic version created by the `semver` resource specified as filepath `version` to generate the versioned name.


#### Parameters
 
* `version`: *Required* File path to `semver` version file
 
* `folderpath`: *Required* Path to folder that contains artifacts


## Example Configuration

### Resource Type
``` yaml
- name: s3-artifact
  type: docker-image
  source:
    repository: quay.io/cosee-concourse/s3-artifact-resource
```
### Resource

``` yaml
- name: artifacts
  type: s3-artifact
  source:
    bucket: artifacts
    filename: release-
    access_key_id: ACCESS-KEY
    secret_access_key: SECRET
    region_name: eu-west-1
```

### Plan

``` yaml
- get: artifacts
```

``` yaml
- put: artifacts
  params:
    version: version/number
    folderpath: artifacts/
```

## Required IAM Permissions

* `s3:PutObject`
* `s3:GetObject`
* `s3:ListBucket`
* `s3:ListAllMyBuckets`