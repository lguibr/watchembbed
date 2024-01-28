import logging

def setup_logger(debug_mode):
    """Setup logger configuration."""
    log_level = logging.DEBUG if debug_mode else logging.INFO
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=log_level)

    # Control Watchdog logging level
    watchdog_logger = logging.getLogger('watchdog')
    watchdog_logger.setLevel(logging.WARNING)

    logger = logging.getLogger(__name__)
    
    return logger
