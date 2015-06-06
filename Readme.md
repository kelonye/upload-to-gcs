
Enable CORS on bucket:

https://cloud.google.com/storage/docs/cross-origin#Configuring-CORS-on-a-Bucket

I.E.:

```
gsutil cors set cors-json-file.json gs://[bucket-name]
```

Where cors-json-file.json contains:

```
[
    {
      "origin": ["http://example.appspot.com", "http://localhost:3000"],
      "responseHeader": ["Content-Type"],
      "method": ["GET", "POST", "HEAD"],
      "maxAgeSeconds": 3600
    }
]
```

Set your bucket to public read and write:

```
gsutil acl set public-read-write gs://[bucket-name]
gsutil defacl set public-read gs://[bucket-name]
```

Install Google Appengine Python SDK.

Run:

```
make default run
```

Visit `http://localhost:3000`