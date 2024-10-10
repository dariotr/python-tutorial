#--web true
#--param OPENAI_API_HOST $OPENAI_API_HOST
#--param OPENAI_API_KEY $OPENAI_API_KEY
#--kind python:default

from openai import AzureOpenAI

ROLE = "You are an helpful assistant."
MODEL = "gpt-35-turbo"

def request(input, role=ROLE):
    ## 3a generate the role as shown in test3.test_request
    return [{"role": "system", "content": role},
            {"role": "user", "content": input}]
    

def ask(ai, input, role=ROLE):
    ## 3b invoke the chat completion API
    comp = ai.chat.completions.create(
        model=MODEL,
        messages=request(input,role)
    )
    
    ## 3c read the first message content if any
    if len(comp.choices) >0:
        res = comp.choices[0].message.content
        
    return res

def connect(args):
    ver = "2023-12-01-preview"
    key = args.get("OPENAI_API_KEY")
    host = args.get("OPENAI_API_HOST")
    ## 2a connect ai with Azure OpenAI and return the api object
    return AzureOpenAI(
        api_version=ver,
        api_key=key,
        azure_endpoint=host
    )
    

def main(args):
    # connect to the AI
    ai = connect(args)

    # read input and produce output
    input = args.get("input", "")

    output = "Connection Error."
    ## 2b retrieve the model we use, check the status and return 'Welcome.' if is 'succeeded'
    model = ai.models.retrieve(MODEL)

    if model.status == 'succeeded':
        output = "Welcome."
    # if the input is not empty, ask to the AI
    if input != "":
        output = ask(ai, input)

    # return the result
    return {
        "body": { "output": output }
    }
