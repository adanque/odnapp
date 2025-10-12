import redis
from redis.exceptions import ConnectionError, TimeoutError

def test_redis_connection(host='10.0.2.4', port=6379, password=None, db=0, timeout=5):
    """
    Tests connectivity to a Redis server.

    Args:
        host (str): The Redis server host.
        port (int): The Redis server port.
        password (str, optional): The Redis server password. Defaults to None.
        db (int): The Redis database number. Defaults to 0.
        timeout (int): The connection timeout in seconds. Defaults to 5.

    Returns:
        bool: True if connection and ping are successful, False otherwise.
    """
    try:
        # Create a Redis client instance with a connection timeout
        r = redis.Redis(
            host=host,
            port=port,
            password=password,
            db=db,
            socket_connect_timeout=timeout,
            socket_timeout=timeout  # Also set a socket timeout for operations
        )
        # Attempt to ping the Redis server
        if r.ping():
            print(f"Successfully connected to Redis at {host}:{port}")
            return True
        else:
            print(f"Failed to ping Redis at {host}:{port}")
            return False
    except (ConnectionError, TimeoutError) as e:
        print(f"Error connecting to Redis at {host}:{port}: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

#if __name__ == "__main__":
    # Example usage:
    # Test with default settings (localhost:6379, no password)
if test_redis_connection():
    print("Redis connection test passed.")
else:
    print("Redis connection test failed.")

    # Test with custom settings (e.g., a different host or password)
    # Be sure to replace 'your_redis_password' with the actual password if required
    # if test_redis_connection(host='your_redis_host', port=6379, password='your_redis_password'):
    #     print("Custom Redis connection test passed.")
    # else:
    #     print("Custom Redis connection test failed.")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
from app.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)

@app.head('/health')
@app.get('/health')
def health_check():
    return 'ok'