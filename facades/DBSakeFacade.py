from adapters import DBSakeAdapter

class DBSakeFacade:
    def __init__(self, executable_path):
        self.adapter = DBSakeAdapter(executable_path)

    def extract_schema(self, frm_file):
        try:
            return self.adapter.extract(frm_file)
        except Exception as e:
            return f"Error occured: {e}"