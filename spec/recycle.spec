{
  "files": [
    {
      "aql": {
        "items.find": {
        		"repo": {"$eq": "slash-maven-release-local"},
        		"created": {"$before": "1mo"},
        		"stat.downloads": {"$eq": null},
        		"name": {"$match": "*.jar"}
        	}
      }
    }
  ]
}