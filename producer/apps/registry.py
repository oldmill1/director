#!/usr/bin/env python3
"""
App registry for managing different application types
"""

from .terminal import TerminalApp

class AppRegistry:
    """Registry for managing different application types"""
    
    def __init__(self):
        self.apps = {}
        self._register_default_apps()
    
    def _register_default_apps(self):
        """Register default application types"""
        # Terminal apps
        self.apps['iTerm'] = TerminalApp('iTerm')
        
        # Future apps can be added here:
        # self.apps['VSCode'] = VSCodeApp()
        # self.apps['Vim'] = VimApp()
    
    def get_app(self, app_name):
        """Get an app instance by name"""
        if app_name in self.apps:
            return self.apps[app_name]
        
        # Default fallback - assume it's iTerm
        return TerminalApp('iTerm')
    
    def register_app(self, name, app_instance):
        """Register a new app type"""
        self.apps[name] = app_instance
    
    def list_apps(self):
        """List all registered apps"""
        return list(self.apps.keys())
