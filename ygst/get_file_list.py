import os

def get_file_list(file_path):
    dir_list = os.listdir(file_path)
    for item in dir_list:
        if item.startswith('work'):
            print(item.startswith('work'))
            print(item)
            os.remove(file_path+item)
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list,key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        print(dir_list)
        #return dir_list

get_file_list(r'D:\1275757008\FileRecv\lctest-jar''\\')