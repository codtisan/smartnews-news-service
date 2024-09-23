import uvicorn
from server import app
import toml

def bootstrap() -> None:
    with open('config.toml') as file:
        config = toml.load(file)
    port = config['project']['port']
    uvicorn.run(app=app, port=port, host='0.0.0.0')

if __name__ == "__main__":
    bootstrap()