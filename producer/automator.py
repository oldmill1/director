#!/usr/bin/env python3
"""
Terminal and Vim Automator
Handles automation of terminal applications using AppleScript
"""

import subprocess
import time

class TerminalAutomator:
    def __init__(self):
        self.app_name = "iTerm2"
    
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
    
    def run_iterm_test(self):
        """Simple test - open iTerm, create new window, run clear command"""
        script = f'''
        tell application "{self.app_name}"
            activate
            
            -- Create new window
            create window with default profile
            
            -- Wait a moment for window to be ready
            delay 0.5
            
            -- Get the current session and run clear command
            tell current session of current window
                write text "clear"
            end tell
            
        end tell
        '''
        
        print(f"Opening {self.app_name} and running clear command...")
        result = self.run_applescript(script)
        
        if result is not None:
            print("✅ iTerm automation successful!")
        else:
            print("❌ iTerm automation failed!")
        
        return result