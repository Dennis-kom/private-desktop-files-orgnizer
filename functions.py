# ------------- IMPORTS ---------------
import os
import shutil
import getpass

# ----------- DATA ----- --------------
user_name = getpass.getuser()
desktop_path = "C:\\Users\\energ\\OneDrive\\שולחן העבודה"
path_pdf ="C:\\Users\\energ\\OneDrive\\שולחן העבודה\\pdf_files"
path_docx ="C:\\Users\\energ\\OneDrive\\שולחן העבודה\\word_files"
path_pptx ="C:\\Users\\energ\\OneDrive\\שולחן העבודה\\powerpoint_files"
path_image ="C:\\Users\\energ\\OneDrive\\שולחן העבודה\\pictures_files"
path_exel ="C:\\Users\\energ\\OneDrive\\שולחן העבודה\\exel_files"
path_text ="C:\\Users\\energ\\OneDrive\\שולחן העבודה\\text_files"
path_zip ="C:\\Users\\energ\\OneDrive\\שולחן העבודה\\zip_files"
path_data_ml_file = "C:\\Users\\energ\\OneDrive\\שולחן העבודה\\automation project\data_ml.txt"

paths = [path_text,path_exel,path_pptx,path_docx,path_image,path_pdf,path_zip]

file_suffix = [".pdf", ".docx", ".txt", ".pptx", ".png", ".jpeg",  ".zip", ".xlsx"]
# ------------ UTILITY FUNCTIONS -------

def fun_test():
    print(chvar1)

def extract_dict_from_map_file(path):

    sep_arr = []
    source = open(path,"r")

    for line in source.readlines():
        sep_arr.append(line)

    return sep_arr




def create_folers():
    for itm in paths:
        if not os.path.isdir(itm):
            os.mkdir(itm)

def orgnize_execute(chvars):
    dict = {".docx":0,".pptx":1,".xlsx":2,".pdf":3,".txt":4,".png":5,".jpeg":6,".zip":7,"select all":8}
    
    for file in os.listdir(desktop_path):
        if (chvars[dict[".pdf"]] or chvars[dict["select all"]]) and file.endswith(".pdf"):
            shutil.move(desktop_path+"\\"+file,path_pdf+"\\"+file)
        if (chvars[dict[".docx"]] or chvars[dict["select all"]]) and file.endswith(".docx") or file.endswith(".doc"):
            shutil.move(desktop_path + "\\" + file, path_docx + "\\" + file)
        if (chvars[dict[".pptx"]] or chvars[dict["select all"]]) and file.endswith(".pptx"):
            shutil.move(desktop_path + "\\" + file, path_pptx + "\\" + file)
        if (chvars[dict[".txt"]] or chvars[dict["select all"]]) and file.endswith(".txt"):
            shutil.move(desktop_path + "\\" + file, path_text + "\\" + file)
        if (chvars[dict[".zip"]] or chvars[dict["select all"]]) and file.endswith(".zip"):
            shutil.move(desktop_path + "\\" + file, path_zip + "\\" + file)
        if (chvars[dict[".png"]] or chvars[dict["select all"]]) and file.endswith(".png"):
            shutil.move(desktop_path + "\\" + file, path_image + "\\" + file)
        if (chvars[dict[".jpeg"]] or chvars[dict["select all"]]) and file.endswith(".jpeg"):
            shutil.move(desktop_path + "\\" + file, path_image + "\\" + file)
        
def create_named_folder(fname_path):
    if os.path.isdir(fname_path):
        os.mkdir(fname_path)


def sort_files_by_subject(subj):
        
    path = desktop_path+"\\"+subj
    create_named_folder(path)
    
    for file in os.listdir(desktop_path):
        if os.path.isfile(desktop_path+"\\"+file) and subj in file.title():
            shutil.move(desktop_path+"\\"+file,path+"\\"+file)

def sort_files_by_ml():

    # creation or opening data memory file
    data_file = open(path_data_ml_file,"w")

def organize_files_by_ml(path):

    local_dict = []

    try:
        map_file = open("main_data_dictionary.txt","r")
    except OSError:
        print("wrong map file destination or file not exists")




    for file in os.listdir(path):
        pass









            


