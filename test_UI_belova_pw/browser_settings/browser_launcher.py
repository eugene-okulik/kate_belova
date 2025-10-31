import json
import os

import yaml
from playwright.sync_api import sync_playwright, BrowserContext, Page


class BrowserLauncher:
    def __init__(self, local_browser_config_path: str = None):
        self.config = None
        self._load_config(local_browser_config_path)
        self.browser = None
        self.playwright = sync_playwright().start()
        self._launch()

    def _load_config(self, config_path: str):
        """Load config from .yaml-file"""
        try:
            with open(config_path) as config_file:
                self.config = yaml.safe_load(config_file)
        except Exception as e:
            raise RuntimeError(f'Error loading config file {e}')

    def _launch(self):
        """Set up browser with a given .yaml-file configuration"""
        browser_type_name = self.config.get('browserType')
        launch_options = self.config.get('launch', {}).copy()
        use_system_browser = self.config.get('useSystemBrowser', False)

        if not use_system_browser:
            launch_options.pop('channel', None)

        if browser_type_name == 'chromium':
            browser_type = self.playwright.chromium
        elif browser_type_name == 'firefox':
            browser_type = self.playwright.firefox
        else:
            raise ValueError(f'Unknown browser type {browser_type_name}')

        self.browser = browser_type.launch(**launch_options)

    def _create_context(self, **kwargs) -> BrowserContext:
        """Create context object"""
        context_params = {'ignore_https_errors': True}
        if self.config.get('context'):
            context_params.update(self.config['context'])

        if os.path.exists('state.json'):
            with open('state.json') as state_file:
                context_params['storage_state'] = json.load(state_file)

        all_context_params = {**context_params, **kwargs}
        context = self.browser.new_context(**all_context_params)
        return context

    def create_page(self, **kwargs) -> Page:
        """Create page object"""
        context = self._create_context(**kwargs)
        return context.new_page()

    def close(self):
        """Close browser and stop Playwright"""
        if self.browser:
            self.browser.close()
        self.playwright.stop()
