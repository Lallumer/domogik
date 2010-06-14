#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This file is part of B{Domogik} project (U{http://www.domogik.org}).

License
=======

B{Domogik} is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

B{Domogik} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Domogik. If not, see U{http://www.gnu.org/licenses}.

Plugin purpose
==============

Load config from file

Implements
==========

- Loader

@author: Maxence Dunnewind <maxence@dunnewind.net>
@copyright: (C) 2007-2009 Domogik project
@license: GPL(v3)
@organization: Domogik
"""

global config_path

####################################################
#       DON'T CHANGE ANYTHING AFTER THIS LINE      #
####################################################
import os
import ConfigParser


class Loader():
    '''
    Parse Domogik config files
    '''

    def __init__(self, plugin_name=None):
        '''
        Load the configuration for a part of the Domogik system
        @param plugin_name name of the plugin to load config from
        '''
        self.main_conf_name = "domogik.cfg"
        self.plugin_name = plugin_name

    def load(self, custom_path = ""):
        '''
        Parse the config
        @param custom_path : Custom path to config file, will superseed others
        @return pair (main_config, plugin_config)
        '''
        main_result = {}
        config = ConfigParser.ConfigParser()
        config.read([custom_path, os.getenv("HOME") + "/." + self.main_conf_name,
            '/etc/' + self.main_conf_name,
            '/usr/local/etc/' + self.main_conf_name])
        result = config.items('domogik')
        main_result = {}
        for k, v in result:
            main_result[k] = v
        #Check the plugin conf file if defined
        if self.plugin_name == None:
            return (main_result, None)

        if self.plugin_name:
            return (main_result, config.items(self.plugin_name))
        else:
            #If we're here, there is no plugin config
            return (main_result, None)
