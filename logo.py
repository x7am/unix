import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

logo = """
             .__        
 __ __  ____ |__|__  ___
|  |  \/    \|  \  \/  /
|  |  /   |  \  |>    < 
|____/|___|  /__/__/\_ \
           \/         \/

"""

def logoo():
    print(Fore.MAGENTA +logo)


