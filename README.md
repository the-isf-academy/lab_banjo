# Riddle server

Riddle server is a simple HTTP server for learning about how computers
communicate over the Internet. 

## Setup


Start the banjo server with: `banjo`

```
$ banjo
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

You can now access the riddle server at 127.0.0.1 from your own machine, or from
your public IP address if you know what it is. 


## Usage

If you already know the IP address and port of a running Riddle server, you can
interact with it using HTTP requests. In these examples, we will use the
`HTTPie` library to send HTTP requests from Terminal.

We are connecting to `127.0.0.1:5000`, which is the address of the Riddle server
when it is running locally.

### List the riddles
```
$ http GET 127.0.0.1:5000/riddles/all

{
    "riddles": [
        {
            "correct": 0,
            "guesses": 0,
            "id": 1,
            "question": "What is orange and sounds like a parrot?"
        }
    ]
}
```

### Get one riddle by id
```
$ http GET 127.0.0.1:5000/riddles/one id=1

{
    "correct": 0,
    "guesses": 0,
    "id": 1,
    "question": "What is orange and sounds like a parrot?"
}
```

### Add a riddle

```
$ http POST 127.0.0.1:5000/riddles/new question="What is black and white and red all over?" answer="A newspaper"

{
    "answer": "A newspaper",
    "correct": 0,
    "guesses": 0,
    "id": 2,
    "question": "What is black and white and red all over?"
}
```

### Guess the answer to a riddle

```
$ http POST 127.0.0.1:5000/riddles/guess id=1 guess="Carrot"

{
    "correct": {
        "answer": "A carrot",
        "correct": 1,
        "guesses": 1,
        "id": 1,
        "question": "What is orange and sounds like a parrot?"
    }
}
```
