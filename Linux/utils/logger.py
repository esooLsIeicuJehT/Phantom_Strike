"""
Logging utility for BloodStrike Python Cheat
Provides colored console output and file logging.
"""

import os
import sys
import logging
from datetime import datetime
from typing import Optional
from pathlib import Path


class ColoredFormatter(logging.Formatter):
    """Custom formatter with color support for console output"""
    
    # ANSI color codes
    COLORS = {
        'DEBUG': '\033[36m',     # Cyan
        'INFO': '\033[32m',      # Green
        'WARNING': '\033[33m',   # Yellow
        'ERROR': '\033[31m',     # Red
        'CRITICAL': '\033[35m',  # Magenta
    }
    RESET = '\033[0m'
    
    def format(self, record):
        # Add color to level name
        if record.levelname in self.COLORS:
            record.levelname = f"{self.COLORS[record.levelname]}{record.levelname}{self.RESET}"
        
        return super().format(record)


class Logger:
    """
    Main logger class with console and file output.
    Supports color output and different log levels.
    """
    
    _instance = None
    _initialized = False
    
    def __new__(cls, name: str = "BloodStrikeCheat", log_dir: str = "logs"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name: str = "BloodStrikeCheat", log_dir: str = "logs"):
        if Logger._initialized:
            return
            
        self.name = name
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Remove existing handlers
        self.logger.handlers.clear()
        
        # Setup console handler
        self._setup_console_handler()
        
        # Setup file handler
        self._setup_file_handler()
        
        Logger._initialized = True
        
    def _setup_console_handler(self):
        """Setup colored console output"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        
        # Colored format
        console_format = ColoredFormatter(
            '[%(asctime)s] [%(levelname)s] %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)
        
    def _setup_file_handler(self):
        """Setup file logging"""
        log_file = self.log_dir / f"cheat_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # Plain format for file
        file_format = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(file_format)
        self.logger.addHandler(file_handler)
        
    def debug(self, msg: str):
        """Log debug message"""
        self.logger.debug(msg)
        
    def info(self, msg: str):
        """Log info message"""
        self.logger.info(msg)
        
    def warning(self, msg: str):
        """Log warning message"""
        self.logger.warning(msg)
        
    def error(self, msg: str):
        """Log error message"""
        self.logger.error(msg)
        
    def critical(self, msg: str):
        """Log critical message"""
        self.logger.critical(msg)
        
    def success(self, msg: str):
        """Log success message (info with green color)"""
        self.logger.info(f"\033[92m[SUCCESS]\033[0m {msg}")
        
    def cheat(self, msg: str):
        """Log cheat-related message with custom formatting"""
        self.logger.info(f"\033[95m[CHEAT]\033[0m {msg}")
        
    def esp(self, msg: str):
        """Log ESP-related message"""
        self.logger.debug(f"\033[96m[ESP]\033[0m {msg}")
        
    def aimbot(self, msg: str):
        """Log aimbot-related message"""
        self.logger.debug(f"\033[93m[AIMBOT]\033[0m {msg}")


def get_logger(name: str = "BloodStrikeCheat") -> Logger:
    """Get or create a logger instance"""
    return Logger(name)


# Pre-configured loggers
main_logger = get_logger("BloodStrikeCheat")
esp_logger = get_logger("ESP")
aimbot_logger = get_logger("Aimbot")
sdk_logger = get_logger("SDK")