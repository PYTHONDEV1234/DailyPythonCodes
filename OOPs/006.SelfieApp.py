class SelfieApp:
    def __init__(self):
        
        print("Internet connection successful.!!!!!!!")
        print("Camera enabled successfully.!!!!!!!")
    
    def ClickPhoto(self):
        print("Photo saved to Gallery.")
    
    def UploadPhoto(self):
        print("Upload successfull.!!!!!!!!!!!!!")

user1 = SelfieApp()
print(user1.ClickPhoto())
print(user1.UploadPhoto())

