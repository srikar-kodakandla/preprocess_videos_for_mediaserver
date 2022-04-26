root='/home/ubuntu/Googledrive/videos' #directory in which videos are present
import subprocess
import os
#####################################renaming files (it removes website names from the file name ) ######################
#This step makes jellyfin to recognize the movie names correctly 
a=[os.path.join(path, name) for path, subdirs, files in os.walk(root) for name in files]
import re
regex="www.+?- "
for i in a:
    if len(re.findall(regex,i.lower()))>0:
        index=re.search(regex,i.lower()).span()
        print(re.search(regex,i.lower()))
        uu=i[:index[0]]+i[index[1]:]
        print(uu)
        os.system(f'mv "{i}" "{uu}"')
print("Done renaming files...")
########################################converting all videos in that directory and sub directory##################
d=subprocess.run('screen -ls',shell=True,  capture_output=True)
if str(d).count("jellyfin_convert")>1:
    print('Exiting , there is already jellyfin_convert is running....')
    import sys
    sys.exit()
from tqdm import tqdm
videos=['mkv','avi','m4v','mp4']
a=[os.path.join(path, name) for path, subdirs, files in os.walk(root) for name in files]
for formating in tqdm(videos):   
    for i in tqdm(a):
        if i[-3:]==formating:
            source=i
            if source[-13:-4]=='converted':
                continue
            destination=i[:-4]+' - converted'+'.m4v'
            #print(source)
            #print(destination)
            video_dir="/home/ubuntu/Videos/"
            os.system(f'cp "{source}"  "/home/ubuntu/Videos/"')
            u=source.split('/')
            new_source=video_dir+u[-1]
            new_destination=new_source[:-4]+' - converted'+'.m4v'
            print(f"HandBrakeCLI --preset='Amazon Fire 1080p30 Surround' --optimize -i '{new_source}' -o '{new_destination}'")
            returned=subprocess.call(f"HandBrakeCLI --preset='Amazon Fire 1080p30 Surround' --optimize -i '{new_source}' -o '{new_destination}'",shell=True)
            print(returned)
            destination_address='/'.join(destination.split('/')[:-1])
            r=os.system(f'cp "{new_destination}" "{destination_address}"')
            os.system(f'rm "{new_source}"')
            os.system(f'rm "{new_destination}"')
            if returned!=0 or r!=0:
                continue
            else:
                print(f'removing file as it subcall process returned : {returned}')
                os.system(f"rm '{source}'")
#renaming again after converting videos 
a=[os.path.join(path, name) for path, subdirs, files in os.walk(root) for name in files]
import re
#regex = "www.*(in|movierulz.*[-]|in|com|mx|org|net|int)"
regex="www.+?- "
for i in a:
    if len(re.findall(regex,i.lower()))>0:
        index=re.search(regex,i.lower()).span()
        print(re.search(regex,i.lower()))
        uu=i[:index[0]]+i[index[1]:]
        print(uu)
        os.system(f'mv "{i}" "{uu}"')
