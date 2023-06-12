import compileall
import os
import shutil
# step 1: make django project
# step 2: take input django project_name
input_src_dir_name="test1"
input_dest_dir_name="compiled_test2"
def create_and_copy_folder(source_folder,destination_folder):
    # Create the destination folder
    print("====================",destination_folder)
    # destination_folder=destination_folder+"\\"+input_src_dir_name
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder, exist_ok=True)
        
        # Copy the contents of the source folder to the destination folder
        shutil.copytree(source_folder, os.path.join(destination_folder, os.path.basename(source_folder)))
    else:

        print(os.path.join(destination_folder, os.path.basename(source_folder)))
        shutil.rmtree(destination_folder)
        shutil.copytree(source_folder, os.path.join(destination_folder, os.path.basename(source_folder))) 
        print("updated on same directory")
def remove_py_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                os.remove(file_path)

def remove_pyc_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.pyc'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
if __name__ == '__main__':
   
    current_Directory = os.getcwd() 
    source_folder_path=current_Directory+"\\"+input_src_dir_name
    destination_folder_path = current_Directory+"\\"+input_dest_dir_name 
    
    #step 3 : compiling process
    # compileall.compile_dir(source_folder_path, force=True, legacy=True)
    #step 4 : make a new directory and copy that compiled file into new directory 
    create_and_copy_folder(source_folder_path, destination_folder_path)
    #step 5: remove .py file
    remove_pyc_files(source_folder_path)
    remove_py_files(destination_folder_path)