import os
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
    ans = input("<input> <RUN PYTHON ")
    exec(str(ans))
    print("</input> </RUN PYTHON>")
class GoogleDrive:
  os.makedirs("python package pybrowse3 googledrive", exist_ok=True)
  
