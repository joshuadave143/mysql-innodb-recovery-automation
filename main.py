from services import DBSakeService
from services import StreamParserService
# recover = DBSakeService();
# recover.recover()
extract = StreamParserService()
# extract.extract_pages_in_ibd()
extract.recover_data()