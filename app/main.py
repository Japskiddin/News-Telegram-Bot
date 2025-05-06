from bot import start_bot
from logger import get_logger

logger = get_logger(__name__)

if __name__ == '__main__':
    logger.info("🚀 Starting...")
    start_bot()
