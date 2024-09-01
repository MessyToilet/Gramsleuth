import shutil                       
from colorama import Fore, Style
import os

def printLogo(color:str = 'white'):
    supportedColors = ["BLACK", 
                       "RED", 
                       "GREEN", 
                       "YELLOW", 
                       "BLUE", 
                       "MAGENTA", 
                       "CYAN", 
                       "WHITE", 
                       "RESET", 
                       "LIGHTBLACK_EX", 
                       "LIGHTRED_EX", 
                       "LIGHTGREEN_EX", 
                       "LIGHTYELLOW_EX", 
                       "LIGHTBLUE_EX", 
                       "LIGHTMAGENTA_EX", 
                       "LIGHTCYAN_EX", 
                       "LIGHTWHITE_EX"]

    if color.upper() not in supportedColors:
        print(f"ERROR: unsupported color given, supported colors:\n{supportedColors}")
        

    text_color = getattr(Fore, color.upper())
    logo = f"""         
        {text_color} ██████╗ ██████╗  █████╗ ███╗   ███╗███████╗██╗     ███████╗██╗   ██╗████████╗██╗  ██╗{Style.RESET_ALL}
        {text_color}██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔════╝██║     ██╔════╝██║   ██║╚══██╔══╝██║  ██║{Style.RESET_ALL}
        {text_color}██║  ███╗██████╔╝███████║██╔████╔██║███████╗██║     █████╗  ██║   ██║   ██║   ███████║{Style.RESET_ALL}
        {text_color}██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║╚════██║██║     ██╔══╝  ██║   ██║   ██║   ██╔══██║{Style.RESET_ALL}
        {text_color}╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║███████║███████╗███████╗╚██████╔╝   ██║   ██║  ██║{Style.RESET_ALL}
        {text_color} ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝{Style.RESET_ALL}
        {text_color}By: MessyToilet{Style.RESET_ALL}""" 
                                                                                     
    terminal_size = shutil.get_terminal_size()
    lines = logo.split('\n')
    max_length = max(len(line) for line in lines)
    centered_lines = [(line.center(terminal_size.columns, ' ') if len(line.strip()) > 0 else ' ' * terminal_size.columns) for line in lines]
    os.system("cls")
    print('\n'.join(centered_lines))
    

def numberBoarder(num: str) -> str:
    return f'{Fore.YELLOW}[{Fore.GREEN}{num}{Fore.YELLOW}]{Fore.RESET}'

def systemBoarder(sys:str, msg:str) -> str: #MAY CAUSE PROBLEMS!! (COULD CAUSE PRINT NONE)
    if sys.upper() == 'ERROR':
        print(f'{Fore.YELLOW}[{Fore.RED}{sys.upper()}{Fore.YELLOW}]{Fore.RESET}  {msg}')
    
    elif sys.upper() == 'SYSTEM':
        print(f'{Fore.YELLOW}[{Fore.BLUE}{sys.upper()}{Fore.YELLOW}]{Fore.RESET} {msg}')
   
    elif sys.upper() == "USER":
        return(f'\n{Fore.YELLOW}[{Fore.CYAN}{sys.upper()}{Fore.YELLOW}]{Fore.RESET} {msg}')
        

MENU = f"""
[    ] {numberBoarder(1)}  Get user info         {numberBoarder(6)}  Get target info         {numberBoarder(11)}  Load file
[    ] {numberBoarder(2)}  Get user network      {numberBoarder(7)}  Get target network      {numberBoarder(12)}  Save to file
[    ] {numberBoarder(3)}  Get user follows      {numberBoarder(8)}  Get target follows      {numberBoarder(13)}  Settings
[    ] {numberBoarder(4)}  Get user likes        {numberBoarder(9)}  Get target likes        {numberBoarder(14)}  Help
[    ] {numberBoarder(5)}  Get user comments     {numberBoarder(10)} Get target comments     {numberBoarder(15)}  Quit (10)
 """

def options() -> str:
    while True:
        # print(MENU)

        print(f'\n{numberBoarder(1)} Get user info', end='\t\t')
        print(f'{numberBoarder(4)} Get target info', end='\t\t')
        print(f'{numberBoarder(7)} Save to file', end='\t')
        print(f'{numberBoarder(10)} Quit')

        print(f'{numberBoarder(2)} Get user posts likes', end='\t\t')
        print(f'{numberBoarder(5)} Get target followers', end='\t')
        print(f'{numberBoarder(8)} Settings') #clear history, color, windowed/window-less

        print(f'{numberBoarder(3)} Get user following', end="\t\t")
        print(f'{numberBoarder(6)} Get target following', end='\t')
        print(f'{numberBoarder(9)} Help') 

        

        try:
            print(f'{systemBoarder(sys="user", msg=">>>")}', end="")
            if (output := int(input(f' '))) in [x for x in range(1,11)]:
                return str(output)
            else:
                systemBoarder(sys='ERORR', msg='Bad Args')  #Do i need this?
        except:
            systemBoarder(sys='ERORR', msg='Bad Args')