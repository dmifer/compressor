import math, os

dir_with_files = "C:\\Users\\DFedorov\\calgarycorpus"

for path, subdirs, files in os.walk(dir_with_files): 
    average = 0

    for f in files:
        file_path = os.path.join(path, f)  
        f = open(file_path, 'rb')
        bytes = bytearray(f.read())     
        f.close()

        f_size = len(bytes)             

        freq = [0] * 256
        for by in bytes:
            freq[by] += 1              

        entropy = 0.0
        for fq in freq:
            if fq > 0:                      
                fq = float(fq) / f_size
                entropy += fq * math.log(fq, 2)

        res = 0 if entropy == 0 else -entropy
        average += res

    average = average / len(files)
    print(average)
