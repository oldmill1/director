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
    
    def run_script(self, script_data):
        """Execute a parsed script by running each step"""
        steps = script_data.get('steps', [])
        
        for i, step in enumerate(steps, 1):
            action = step.get('action')
            print(f"  Step {i}: {action}")
            
            if action == 'activate_app':
                self._activate_app(step.get('app', self.app_name))
            elif action == 'create_window':
                self._create_window(step.get('profile', 'default'))
            elif action == 'wait':
                self._wait(step.get('duration', 0.5))
            elif action == 'write_text':
                self._write_text(step.get('text', ''), step.get('target', 'current_session'))
            else:
                print(f"    ⚠️  Unknown action: {action}")
    
    def _activate_app(self, app_name):
        """Activate the specified application"""
        script = f'tell application "{app_name}" to activate'
        self.run_applescript(script)
    
    def _create_window(self, profile):
        """Create a new window with specified profile"""
        script = f'''
        tell application "{self.app_name}"
            create window with default profile
        end tell
        '''
        self.run_applescript(script)
    
    def _wait(self, duration):
        """Wait for specified duration"""
        import time
        time.sleep(duration)
    
    def _write_text(self, text, target):
        """Write text to the specified target"""
        if target == 'current_session':
            script = f'''
            tell application "{self.app_name}"
                tell current session of current window
                    write text "{text}"
                end tell
            end tell
            '''
        else:
            print(f"    ⚠️  Unknown target: {target}")
            return
        
        self.run_applescript(script)

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