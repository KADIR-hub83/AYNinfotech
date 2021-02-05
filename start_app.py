# Run a test server.
from components import app

if __name__ == "__main__":
    app.run(host='localhost', port=8086, debug=True)
