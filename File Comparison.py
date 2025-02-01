import hashlib

class Compare:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        
        
    def hash1(self): #determining the sha256 hash for the first file
        
        #fixed buffer
        #65536 bytes = 64 kilobytes
        buf_size = 65536
        
        #starting the sha256 
        sha256_A = hashlib.sha256()
        
        #opening the file in binary for reading
        with open(self.file1, 'rb') as f:
            
            while True:
                data = f.read(buf_size)
                
                if not data:
                    break
            
            #readable data = buffer from the file
            #saved in a new variable
            sha256_A.update(data)
            
            
            # *.hexidigest hashes the input from the file based on sha256_A.update(data) using hexidecimal formatting
        return sha256_A.hexdigest()
        
        
    def hash2(self): #determining the hash for the second file
        
        #using the same buffer for both files
        buf_size = 65536
        
        sha256_B = hashlib.sha256()
        
        #opening the second file in binary
        with open(self.file2, 'rb') as f:
            
            while True:
                data = f.read(buf_size)
                
                if not data:
                    break
            
            #readable data = buffer from the file
            #saved in a new variable
            sha256_B.update(data)
            
            #same hashing method as above, instead using a new variable
        return sha256_B.hexdigest()

#Enabling the use of the Compare class by giving it an object
hashes = Compare("C:\\Users\\Sam\\Desktop\\Coding\\Testing Resources\\Hash.1.txt", "C:\\Users\\Sam\\Desktop\\Coding\\Testing Resources\\Hash.2")


#comparing the files based on the final hashes from the Compare class
if hashes.hash1 != hashes.hash2:
        print("both files are unique")
else:
        print("the files are the same")
            


