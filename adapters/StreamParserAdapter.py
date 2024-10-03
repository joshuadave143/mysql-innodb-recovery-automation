import subprocess

class StreamParserAdapter:
    def __init__(self, stream_parser_path, c_parser_path):
        self.stream_parser_path = stream_parser_path
        self.c_parser_path      = c_parser_path

    def parse(self, ibd_file, working_dir):
        result = subprocess.run([self.stream_parser_path,"-f", ibd_file], capture_output=True,text=True,cwd=working_dir)
        return result.stdout
    
    def read(self, page_index_file, page_type_blob, schema_file, tableName,sqlFilename):
        subprocess.run([self.c_parser_path,"-f", page_index_file,"-t",schema_file,"-b",page_type_blob,">",tableName,"2>",sqlFilename], capture_output=True,text=True)