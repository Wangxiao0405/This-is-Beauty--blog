import time
# def zsq(aa):
#     def newaa():
#         start=time.time()
#         print("程序开始")
#         aa()
#         print("程序结束")
#         end=time.time()
#         print("运行总时间为：%s"%(end-start))
#     return newaa
# @zsq
# def aa():
#     time.sleep(1)
# aa()

# 带参数的装饰器
def zsq(name):
    def newzsq(fn):
        def newfn():
            start=time.time()
            print("程序开始")
            fn()
            print("程序结束")
            end=time.time()
            print("运行总时间为：%s"%(end-start))
        return newfn
    return newzsq
