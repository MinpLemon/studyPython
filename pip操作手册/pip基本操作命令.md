# pip基本使用    

## 单独升级某个库
```
pip3 list                        列出所有安装的库
pip3 list --outdated             列出所有过期的库
pip3 install --upgrade + 库名    升级该python库
```

## 批量升级python 方法一
>可用，慎用，很花时间，而且很多不用的库全给你更新一遍
```
from subprocess import call
import pkg_resources

for dist in pkg_resources.working_set:
    call("pip3 install --upgrade " + dist.project_name, shell=True)
```

        
## 批量升级python 方法二
>通过 pip-review 升级
```
    pip3 install pip-review             先安装pip-review
    pip-review --local --interactive
```

    
## 生成requirements.txt文件
    pip3 freeze > requirements.txt
## 安装requirements.txt依赖
    pip3 install -r requirements.txt

