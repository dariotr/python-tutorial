#--web true
import json

def main(arg):
    data = {
        "services": [
            ## 1c add the demo entry, an object with name Demo and url mastrogpt/demo
            {
                "name": "Demo",
                "url": "mastrogpt/demo"
            },
            {
                "name": "OpenAI",
                "url": "openai/chat"
            }
            ## 2c add the OpenAI entry, an object with name OpenAI and url openai/chat
        ]
    }
    return {"body": data}
