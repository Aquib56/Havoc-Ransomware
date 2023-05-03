import struct,glob,os
import conf
import cryp

injected_s = 3556020

def restore_all():    
    for filename in glob.iglob(conf.test_folder + '**', recursive=True):
            print(filename)
            if os.path.isfile(filename):
                orig_file, orig_filename = eject(filename)
                orig = cryp.decrypt(orig_file)
                with open(filename, 'wb') as enc_file:
                    enc_file.write(orig)
                os.rename(filename,orig_filename)
                

def eject(filename):
    with open(filename,'rb') as file:
        file.seek(injected_s)
        s_len = struct.unpack('i',file.read(4))[0]
        orig_name = file.read(s_len)
        orig_file = file.read()
        return orig_file, orig_name

restore_all()
print("All the files have been restored")