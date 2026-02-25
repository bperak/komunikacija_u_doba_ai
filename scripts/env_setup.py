"""Environment setup module for agent scripts.

This module handles loading environment variables from .env files.
Import this at the beginning of your agent scripts to ensure API keys are properly loaded.
"""

import os
import logging
from dotenv import load_dotenv

def setup_environment():
    """Load environment variables from .env file.
    
    Returns:
        bool: True if OPENAI_API_KEY was successfully loaded, False otherwise
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Check if OPENAI_API_KEY is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        logging.warning("OPENAI_API_KEY not found in environment variables")
        return False
    
    return True

# Auto-run setup when this module is imported
success = setup_environment()
if success:
    logging.info("Environment setup successful - API keys loaded") 