from facades import StreamParserFacade
from config import settings
import os

class StreamParserService:
    def __init__(self):
        print("Table data recovery initialized.")
        self.facade = StreamParserFacade(settings.STREAM_PARSER_EXECUTABLE_PATH, settings.C_PARSER_EXECUTABLE_PATH)
    
    def extract_pages_in_ibd(self):
        print("Extracting pages from the IBD file...")
        for file in os.listdir(settings.DATA_DIRECTORY_PATH):
            if file.endswith(".ibd"):
                table_name = os.path.splitext(file)[0]

                result = self.facade.parse_ibd_file(settings.DATA_DIRECTORY_PATH+ f"/{file}", settings.PAGES_OUTPUT_PATH)
                print(result)
                print(f"Pages from the {table_name} table have been successfully extracted.")

        print("Page extraction completed.")