import subprocess

class DBSakeAdapter:
    def __init__(self, executable_path):
        self.executable_path = executable_path
    
    def extract(self, frm_file):
        result = subprocess.run([self.executable_path,"frmdump", frm_file], capture_output=True,text=True)
        return result.stdout