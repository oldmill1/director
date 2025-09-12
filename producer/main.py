#!/usr/bin/env python3
"""
Coding Video Automator
Main application entry point
"""

import subprocess
import time
from .automator import TerminalAutomator

def main():
    print("🎬 Coding Video Automator")
    print("========================")
    
    # Create automator instance
    automator = TerminalAutomator()
    
    # Simple test - open iTerm and run clear command
    print("Running iTerm test...")
    automator.run_iterm_test()
    
    print("✅ Test completed!")

if __name__ == "__main__":
    main()
