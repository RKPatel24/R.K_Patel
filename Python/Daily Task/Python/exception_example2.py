import sys
try:
    print(a)
except:
    print(f"{sys.exc_info()[0]}  - {sys.exc_info()[1]}")