{
  "files": [
    {
      "aql": {
        "items.find": {
          "$and": [
            { "name": { "$match": "*.jar" } },
            { "@released" : {"$match": "true"}}
          ]
        }
      }
    }
  ]
}
