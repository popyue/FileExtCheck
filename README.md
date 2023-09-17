# FileExtCheck

## Description 

1. Batch change File name
- File name Format 
```
[IMG]<FileName>
```
2. Batch add File extension


## Reference
1. [Working With Files in Python](https://realpython.com/working-with-files-in-python/)
2. [Keep Files in Order with this Python Method](https://medium.com/@BetterEverything/keep-files-in-order-with-this-python-method-873305bedf0)
3. [How to Iterate Over Files in a Directory Using Python: Guide for Beginners](https://pieriantraining.com/iterate-over-files-in-directory-using-python/)
    - Iterate file in directory with 'while' loop
    ```
    import os

    directory = '/my_directory'
    files = os.listdir(directory)
    index = 0
    while index < len(files):
        filename = files[index]
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename)) as f:
                print(f.read())
        index += 1
    ```

### Pathlib 
4. [How to Get File Extension in Python](https://www.digitalocean.com/community/tutorials/get-file-extension-in-python)
    - Get File Extension with pathlib
    ```
    import pathlib
    pathlib.Path("<TargetFile Path>").suffix
    ```
5. [Python路径操作模块pathlib，看这篇就够了！](https://zhuanlan.zhihu.com/p/475661402)
6. [How to change the path extension with Python code?](https://kodify.net/python/change-file-path-extension/)
7. [How to Rename a File in Python: 4 Easy Ways](https://blog.enterprisedna.co/how-to-rename-a-file-in-python-4-easy-ways/)
8. [pathlib之文件操作rename()方法](https://zhuanlan.zhihu.com/p/344896622)# FileExtCheck
