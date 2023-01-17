import os
import shutil
import logging

import configs.app_settings as CONFIGS
from copy_mysql_data import CopyMySqlData

logging.basicConfig(level=logging.DEBUG)

try:
    _copy_mysql_data = CopyMySqlData(CONFIGS.service_path_command,CONFIGS.source_folder,CONFIGS.destination_folder)
    _copy_mysql_data.delete_command()
    #_copy_mysql_data.db_stop_command();
    logging.debug("METADATA BEFORE COPY: {} (${})".format(__file__,_copy_mysql_data.get_file_metadata(CONFIGS.source_folder)))
    _copy_mysql_data.copy_file()
    _copy_mysql_data.get_file_metadata(CONFIGS.destination_folder)
    logging.debug("METADATA AFTER COPY: {} (${})".format(__file__,_copy_mysql_data.get_file_metadata(CONFIGS.destination_folder)))
    #_copy_mysql_data.db_stop_command();
except shutil.SameFileError:
    logging.debug("ERROR: {} (${})".format(__file__,"FILE EXISTS"))
except PermissionError:
    logging.debug("ERROR: {} (${})".format(__file__,"PERMISSION DENIED"))
except:
    logging.debug("ERROR: {} (${})".format(__file__,"COPYING FILE FAILED"))