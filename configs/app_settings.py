#!/usr/bin/python

import os
import sys
import logging
import ConfigParser

CONFIG_FILE = '/usr/local/lib/mysql_file_copy/configs/app.conf'

config = ConfigParser.ConfigParser()
config.read(CONFIG_FILE)

source_folder = config.get("file_path","source_folder")
destination_folder = config.get("file_path","destination_folder")
service_path_command = config.get("service_path","service_path_command")