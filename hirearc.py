import os
import glob
import shutil
if __name__=="__main__":
    current_dir = os.getcwd()
    pdf_files = glob.glob(os.path.join(current_dir, '*.pdf'))
    prefixes=[]
    for pdf_file in pdf_files:
        print(pdf_file)
        filename=pdf_file.split("\\")[-1]
        fileprefix=filename.split("-")[0]
        fileprefix=fileprefix.strip("v")
        if fileprefix not in prefixes:
            prefixes.append(fileprefix)
    for prefix in prefixes:
        print(prefix)
        if not os.path.exists(prefix):
            os.makedirs(prefix)
    for pdf_file in pdf_files:
        print(pdf_file)
        filename=pdf_file.split("\\")[-1]
        fileprefix=filename.split("-")[0]
        fileprefix=fileprefix.strip("v")
        source=pdf_file
        dest=current_dir+"/"+fileprefix+"/"+filename
        print("move {} to {}".format(source,dest))
        shutil.move(source,dest)
