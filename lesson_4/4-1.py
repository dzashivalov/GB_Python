import sys
from sys import argv


def z_func():
    try:
        script_name, h_param, ph_param, b_param = argv
        return (float(h_param) * float(ph_param)) + float(b_param)
    except ValueError:
        return 0


print(z_func())
