from adapters import StreamParserAdapter

class StreamParserFacade:
    def __init__(self, stream_parser_path, c_parser_path) :
        self.adapter = StreamParserAdapter(stream_parser_path, c_parser_path)

    def parse_ibd_file(self, ibd_file, working_dir):
        try:
            return self.adapter.parse(ibd_file, working_dir)
        except Exception as e:
            return f"Error occured: {e}"
        
    def extract_data(self, page_index_file, page_type_blob, schema_file, tableName, sqlFilename):
        try:
            self.adapter.read(page_index_file, page_type_blob, schema_file, tableName, sqlFilename)
        except Exception as e:
            return f"Error occured: {e}"