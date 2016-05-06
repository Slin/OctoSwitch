#coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class OctoSwitchPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("OctoSwitch!!!!111111")

__plugin_implementation__ = OctoSwitchPlugin()