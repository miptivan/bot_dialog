from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
PARSE_MODE = env("PARSE_MODE", default="HTML")
REDIS_HOST = env("REDIS_HOST", default="localhost")
REDIS_PORT = env.int("REDIS_PORT", default=6379)
REDIS_PASSWORD = env("REDIS_PASSWORD", default=None)
