files = []
passes = []
print("Imported web, please only use one file in GoogleDrive class or use GoogleDrive.delfile('your file here!')")
class Website:
  def __init__(self, name: str, page: str,  dangerous: bool, sitetype: str) -> None:
    self.name = name
    self.page = page
    self.dangerous = dangerous
    self.sitetype = true
  def get_website(self) -> None:
    if self.dangerous == True:
      raise NotImplementedError("Website blocked.")
    if self.dangerous == False:
      print(f'https://{self.name}.{self.sitetype}/{self.page}')
  def debug(self):
    ans = input("<DEBUG>str=")
    exec(str(ans))
    print("</DEBUG>str=")
class GoogleDrive:
  def __init__(self):
    pass
  def newfile(self, file: str, extension: str):
    global files
    files.append(f'{file}.{extension}')
  def delfile(self, file: str):
    global files
    files.pop(file)
class PasswordManager:
  def __init__(self):
    pass
  def store(self, password: str, site: Website) -> None:
    global passes
    passes.insert(f'{password} :: {site}')
    
