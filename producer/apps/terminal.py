#!/usr/bin/env python3
"""
iTerm2 App implementation
"""

from .base import BaseApp

class TerminalApp(BaseApp):
    """iTerm2 application handler"""
    
    def __init__(self, app_name="iTerm2"):
        super().__init__(app_name)
    
    def start(self, **kwargs):
        """Activate iTerm2 and create a new window"""
        # Try to activate iTerm2 first
        activate_script = f'tell application "{self.app_name}" to activate'
        result = self.run_applescript(activate_script)
        
        if result is None:
            print(f"    ⚠️  Could not activate {self.app_name}, trying to launch...")
            # Try to launch iTerm2 if activation failed
            launch_script = f'tell application "{self.app_name}" to launch'
            self.run_applescript(launch_script)
            self.wait(2.0)  # Wait longer for launch
        
        # Wait a moment for iTerm2 to be ready
        self.wait(1.0)
        
        # Create new window in iTerm2
        window_script = f'tell application "{self.app_name}" to create window with default profile'
        
        return self.run_applescript(window_script)
    
    def write(self, text, **kwargs):
        """Write text to the current active iTerm2 session"""
        # Use System Events to send keystrokes to the current active application
        script = f'''
        tell application "System Events"
            keystroke "{text}"
            key code 36
        end tell
        '''
        return self.run_applescript(script)
    
    def create_window(self, profile="default"):
        """Create a new iTerm2 window"""
        script = f'''
        tell application "{self.app_name}"
            create window with default profile
        end tell
        '''
        return self.run_applescript(script)
    
    def supports_action(self, action):
        """Check if this iTerm2 app supports a specific action"""
        iterm_actions = ['start', 'write', 'wait', 'create_window']
        return action in iterm_actions
