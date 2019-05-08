import subprocess
from PIL import Image
def make_matelials_list():
    source_directory = "source/"
    resource=subprocess.run(["ls",source_directory],stdout=subprocess.PIPE)
    resource = resource.stdout.decode().split("\n")
    resource = resource[:len(resource)-1]
    resource_list = [Image.open(source_directory+i) for i in resource]
    return resource_list
    
if __name__ == "__main__":
    source_directory = "source/"
    resource=subprocess.run(["ls",source_directory],stdout=subprocess.PIPE)
    resource = resource.stdout.decode().split("\n")
    resource = resource[:len(resource)-1]
    resource_list = [Image.open(source_directory+i) for i in resource]