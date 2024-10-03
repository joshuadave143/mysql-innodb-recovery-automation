from facades import DBSakeFacade
from config import settings
import os
import stat
import subprocess

class DBSakeService:
    def __init__(self):
        print("Recovering table structure initialized.")
        self.facades = DBSakeFacade(settings.DBSAKE_EXECUTABLE_PATH)

    def recover(self):
        print("Table structure is being recovered...")

        # Create the directory if it doesn't exist
        os.makedirs(settings.SCHEMA_OUTPUT_PATH, exist_ok=True)
        # subprocess.run(['sudo', 'chown', 'joshua:users', settings.SCHEMA_OUTPUT_PATH])
        # # os.chmod(settings.SCHEMA_OUTPUT_PATH, stat.S_IRWXU | stat.S_IRWXG | stat.S_ISGID | stat.S_IRGRP | stat.S_IXGRP)
        # os.chmod(settings.SCHEMA_OUTPUT_PATH, stat.S_IRWXU | stat.S_IRWXG | stat.S_IXGRP | stat.S_ISGID)
        # # Verify permissions explicitly
        # subprocess.run(['sudo', 'chmod', 'g+s', settings.SCHEMA_OUTPUT_PATH])  # Ensures the SGID bit is set correctly
        # subprocess.run(['sudo', 'chmod', 'o+rx', settings.SCHEMA_OUTPUT_PATH]) 
        
        # Remove any existing ACLs
        # subprocess.run(['sudo', 'setfacl', '-b', settings.SCHEMA_OUTPUT_PATH])
        with open(settings.FULL_SCHEMA, "w") as full_schema:
            for file in os.listdir(settings.DATA_DIRECTORY_PATH):
                if file.endswith(".frm"):
                    # Extract the base name (without the .frm extension)
                    table_name = os.path.splitext(file)[0]
                    # Build the full path to the .frm file
                    frm_file = os.path.join(settings.DATA_DIRECTORY_PATH, file)
                    # Use dbsake to dump the structure and save to an individual .sql file
                    individual_file_path = settings.SCHEMA_OUTPUT_PATH + f"/{table_name}"+".sql"
                    with open( individual_file_path, "w" ) as output_file:
                        result = self.facades.extract_schema(frm_file)
                        output_file.write(result)
                        print(f"Table {table_name} successfully recovered")

                    # Append the contents of the individual file to the merged output file
                    with open(individual_file_path, "r") as output_file:
                        full_schema.write(output_file.read())
            print(f"All tables successfully recovered and merged into {settings.FULL_SCHEMA}")


