checkSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "source": {
      "type": "object",
      "properties": {
        "secret_access_key": {
          "type": "string"
        },
        "filename": {
          "type": "string"
        },
        "access_key_id": {
          "type": "string"
        },
        "bucket": {
          "type": "string"
        },
        "region_name": {
          "type": "string"
        }
      },
      "required": [
        "secret_access_key",
        "filename",
        "access_key_id",
        "bucket",
        "region_name"
      ]
    },
    "version": {
      "type": "object",
      "properties": {
        "version": {
          "type": "string"
        }
      },
      "required": [
        "version"
      ]
    }
  },
  "required": [
    "source"
  ]
}

inoutSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "source": {
      "type": "object",
      "properties": {
        "secret_access_key": {
          "type": "string"
        },
        "filename": {
          "type": "string"
        },
        "access_key_id": {
          "type": "string"
        },
        "bucket": {
          "type": "string"
        },
        "region_name": {
          "type": "string"
        }
      },
      "required": [
        "secret_access_key",
        "filename",
        "access_key_id",
        "bucket",
        "region_name"
      ]
    },
    "version": {
      "type": "object",
      "properties": {
        "version": {
          "type": "string"
        }
      },
      "required": [
        "version"
      ]
    },
    "params": {
      "type": "object",
      "properties": {
        "version": {
          "type": "string"
        },
        "folderpath": {
          "type": "string"
        }
      },
      "required": [
        "version",
        "folderpath"
      ]
    }
  },
  "required": [
    "source",
    "params"
  ]
}
