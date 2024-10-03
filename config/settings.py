import os

# Get the absolute path to the current file
CURRENT_FILE = os.path.abspath(__file__)

# Traverse up the directory to the project root
# Assuming the structure like: project_root/your_module/some_file.py
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_FILE))

# You can alternatively go up more levels by chaining `dirname`
# project_root = os.path.abspath(os.path.join(current_file, "../..")) 


############ executable location settings ##################

#Location of dbsake
DBSAKE_EXECUTABLE_PATH          = PROJECT_ROOT+'/drivers/dbsake'

STREAM_PARSER_EXECUTABLE_PATH   = PROJECT_ROOT+'/drivers/stream_parser'

C_PARSER_EXECUTABLE_PATH        = PROJECT_ROOT+'/drivers/c_parser'

############ location of Data Directory ##################
DATA_DIRECTORY_PATH             = PROJECT_ROOT+'/dataDirectory'

############ location of Output file ##################
OUTPUT_PATH                     = PROJECT_ROOT+'/output'

SCHEMA_OUTPUT_PATH              = OUTPUT_PATH+'/schemas'

DATA_OUTPUT_PATH                = OUTPUT_PATH+'/data'

PAGES_OUTPUT_PATH               = OUTPUT_PATH+'/pages'

############ FILE NAME OF THE MERGE SQL SCHEMA ################## CHECK THE GRAMMAR LETTER

FULL_SCHEMA                     = SCHEMA_OUTPUT_PATH+'/FULL_SCHEMA.sql'