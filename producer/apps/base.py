#!/usr/bin/env python3
"""
Base App class for all Producer applications
"""

import subprocess
import time
from abc import ABC, abstractmethod

class BaseApp(ABC):
    """Base class for all Producer applications"""
    
    def __init__(self, app_name):
        self.app_name = app_name
    
    def run_applescript(self, script):
        """Execute AppleScript and return the result"""
        try:
            result = subprocess.run(
                ['osascript', '-e', script],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"AppleScript error: {e.stderr}")
            return None
    
    def wait(self, duration):
        """Wait for specified duration"""
        time.sleep(duration)
    
    @abstractmethod
    def start(self, **kwargs):
        """Start/activate the application"""
        pass
    
    @abstractmethod
    def write(self, text, **kwargs):
        """Write text to the application"""
        pass
    
    def supports_action(self, action):
        """Check if this app supports a specific action"""
        return action in ['start', 'write', 'wait']
