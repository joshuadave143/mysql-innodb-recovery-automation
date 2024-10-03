import os
import subprocess

class recoverTableSchema:
    # Directory containing the .frm files
    dataDirectory = "dataDirectory"
    mergedOutputPath = "output/merged_output.sql"

    def __init__(self):
        print("Recovering table structure initialized")
    def recover(self):
        print("Table structure is being recovered...")

        with open(self.mergedOutputPath, "w") as merged_output_file:

            # Iterate over all .frm files in the directory
            for file in os.listdir(self.dataDirectory):
                if file.endswith(".frm"):
                    # Extract the base name (without the .frm extension)
                    table_name = os.path.splitext(file)[0]
                    
                    # Build the full path to the .frm file
                    frm_file = os.path.join(self.dataDirectory, file)
                    
                    # Use dbsake to dump the structure and save to an individual .sql file
                    individual_file_path = f"output/{table_name}.sql"
                    with open(individual_file_path, "w") as output_file:
                        subprocess.run(["./drivers/dbsake", "frmdump", frm_file], stdout=output_file)
                        print(f"Table {table_name} successfully recovered")

                    # Append the contents of the individual file to the merged output file
                    with open(individual_file_path, "r") as output_file:
                        merged_output_file.write(output_file.read())
            print(f"All tables successfully recovered and merged into {self.mergedOutputPath}")