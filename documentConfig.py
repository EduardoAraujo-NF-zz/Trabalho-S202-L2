validation = {"$jsonSchema": {
    "bsonType": "object",
    "required": ["type", "title", "info.genres", "info.image_url", "info.trailer_url", "info.duration", "info.directors",
                 "info.actors", "info.release_date"],
    "properties": {
        "type": {
            "bsonType": "string",
        },
        "title": {
            "bsonType": "string",
        },
        "info": {
            "bsonType": "object",
        },
        "info.genres": {
            "bsonType": "array",
        },
        "info.image_url": {
            "bsonType": "string",
        },
        "info.trailer_url": {
            "bsonType": "string",
        },
        "info.duration": {
            "bsonType": "string",
        },
        "info.directors": {
            "bsonType": "array",
        },
        "info.actors": {
            "bsonType": "array",
        },
        "info.release_date": {
            "bsonType": "string",
        },
    }
}
}
