#!/usr/bin/python3

import os
import sys
import logging
import configparser 

CONFIG_FILE = '/usr/local/lib/mysql_file_copy/configs/app.conf'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

source_folder = config.get("file_path","source_folder")
destination_folder = config.get("file_path","destination_folder")
compressed_file_source_folder = config.get("file_path","compressed_file_source_folder")
service_path_command = config.get("service_path","service_path_command")

user = config.get("mysql","db_user")
password = config.get("mysql","db_password")