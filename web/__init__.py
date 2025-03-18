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
    ans = input("<input> <RUN PYTHON> ")
    exec(str(ans))
    print("</input> </RUN PYTHON>")
class GoogleDrive:
  os.makedirs("googleDrive PyBrowse3", exist_ok=True
  def createFile(name: str, content: str) -> None:
    folder_path = r"C:\Users\AppData\Local\Programs\Python\Python314"
    file_path = os.path.join(folder_path, name)
    with open(file_path, "w") as f:
      f.write(content) # It will Edit the file if it exists
  def delFile(file_path):
	  os.remove(file_path)
	  
      


    
