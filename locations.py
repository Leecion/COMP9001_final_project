locations = {
    "forest": {
        "name": "Forest Entrance",
        "description": "You stand at the entrance of a green forest. There's a path ahead.",
        "options": {
            "1": {"text": "Follow the path", "location": "path"},
            "2": {"text": "Search around", "action": "search_forest"}
        }
    },

    "path": {
        "name": "Forest Path",
        "description": "You're walking on a forest path. There's a stream to the left and a cave to the right.",
        "options": {
            "1": {"text": "Go to the stream", "location": "stream"},
            "2": {"text": "Enter the cave", "location": "cave"},
            "3": {"text": "Return to forest entrance", "location": "forest"}
        }
    },

    "stream": {
        "name": "Stream",
        "description": "A clear stream flows before you. You can rest here.",
        "options": {
            "1": {"text": "Drink water and rest", "action": "drink_water"},
            "2": {"text": "Search for items", "action": "search_stream"},
            "3": {"text": "Return to path", "location": "path"}
        }
    },

    "cave": {
        "name": "Mysterious Cave",
        "description": "The cave is dark, but you can vaguely see something glowing in the depths.",
        "options": {
            "1": {"text": "Go deeper into cave", "action": "explore_cave"},
            "2": {"text": "Return to path", "location": "path"}
        }
    },

    "treasure_room": {
        "name": "Treasure Room",
        "description": "Wow! There's a shining treasure chest here!",
        "options": {
            "1": {"text": "Open the chest", "action": "open_treasure"},
            "2": {"text": "Leave the room", "location": "cave"}
        }
    }
}