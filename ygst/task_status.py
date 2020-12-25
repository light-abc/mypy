from urllib import request
import re
import string

app_info=request.urlopen('http://58.222.239.245:1111/eureka/apps')

info=app_info.readlines()
line=str(info)
pattern = r"app"
result = re.findall(pattern,line)
print(result)
# a=str(status)

# if "UP" in a:
#     print("task-center status is UP")
# else:
#     print("task-center status is Down")
