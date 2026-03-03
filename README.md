#Simple API

A local API built with Python and Flask

## Endpoints

- '/' - Home, returns a welcome message
- '/hello/<name>' - Returns a greating for any name
- '/Joke' - Returns a joke
- '/number/<num>' - Returns stats about any number

## How it works
1. Flask receives a request at a defined route (in this case a local route or route on server)
2. The matching function runs and processes any input
3. Returns a JSON response

##Skills Used
- Python
- Flask
- REST API design
- Dynamic routing
- Local network hosting

## How to run
python3 -m flask --app.py run --host 0.0.0.0 --port 8080

