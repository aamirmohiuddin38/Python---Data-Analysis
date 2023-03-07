import sys

try:
    print(1/0)
except:
    _, _, tb = sys.exc_info()
    print(tb.tb_frame)
    print(tb.tb_frame.f_code)
    print(tb.tb_frame.f_code.co_filename)
finally:
    print("System exc_info() function returns tuple")
