#!/usr/bin/python3

import os

class CopyMySqlData():
    def __init__(self,db_service_path,db_source_path,db_destination_path):
        self.db_service_path = db_service_path
        self.db_source_path = db_source_path
        self.db_destination_path = db_destination_path
    #--.stop mysql service.
    def db_stop_command(self):
        os.system('sudo ' + self.db_service_path + ' stop')
    #--.start mysql service.            
    def db_start_command(self):
        os.system('sudo ' + self.db_service_path +' start')
    #--.copy file.
    def copy_file(self):
        os.system('sudo cp -p ' + self.db_source_path + ' * ' + self.db_destination_path)
    #-..read file meta-data.
    def get_file_metadata(self,file_path):
        return os.stat(file_path)
    #--.delete data folder.
    def delete_command(self):
        os.system('sudo rm ' + self.db_source_path + '*')