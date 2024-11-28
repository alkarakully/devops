import os

CRED = '\033[91m'
CEND = '\033[0m'
CGRN = '\033[92m'
CBLU = '\033[96m'
CYLW = '\033[93m'
CMGT = '\033[35m'
CORG = '\033[38;5;208m'

t_width = os.get_terminal_size().columns
def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_allah():
    art1 = [
        "\n\n\n\n\n",
        f"{CGRN}--------------------###     ##        ##           ###     ##     ##   {CEND}{CYLW}##  ######## {CEND}{CBLU}  ##########  ##     ##  #######{CEND}",
        f"{CGRN}-------------------## ##    ##        ##          ## ##    ##     ##   {CEND}{CYLW}    ##       {CEND}{CBLU}      ##      ##     ##  ##     {CEND}",
        f"{CGRN}------------------##   ##   ##        ##         ##   ##   ##     ##   {CEND}{CYLW}##  ##       {CEND}{CBLU}      ##      ##     ##  ##     {CEND}",
        f"{CGRN}-----------------#########  ##        ##        #########  #########   {CEND}{CYLW}##  ######## {CEND}{CBLU}      ##      #########  #######{CEND}",
        f"{CGRN}-----------------##     ##  ##        ##        ##     ##  ##     ##   {CEND}{CYLW}##        ## {CEND}{CBLU}      ##      ##     ##  ##     {CEND}",
        f"{CGRN}-----------------##     ##  ##        ##        ##     ##  ##     ##   {CEND}{CYLW}##        ## {CEND}{CBLU}      ##      ##     ##  ##     {CEND}",
        f"{CGRN}-----------------##     ##  ########  ########  ##     ##  ##     ##   {CEND}{CYLW}##  ######## {CEND}{CBLU}      ##      ##     ##  #######{CEND}",
        "",
        f"{CRED}  #######    ########   #########     ###     ##########  #########  ########  ##########{CEND}",
        f"{CRED} ##     ##   ##     ##  ##           ##  ##       ##      ##         ##            ##    {CEND}",
        f"{CRED} ##          ##     ##  ##          ##    ##      ##      ##         ##            ##    {CEND}",
        f"{CRED} ##   ####   ########   ########   ##########     ##      ########   ########      ##    {CEND}",
        f"{CRED} ##     ##   ##   ##    ##         ##      ##     ##      ##               ##      ##    {CEND}",
        f"{CRED} ##     ##   ##    ##   ##         ##      ##     ##      ##               ##      ##    {CEND}",
        f"{CRED}  #######    ##     ##  #########  ##      ##     ##      #########  ########      ##    {CEND}",
    ]

    art2 = [
        f"{CORG} ##########  ########  ########      #######       ###      ##########     ###    {CEND}",
        f"{CORG}     ##      ##        ##            ##     ##    ##  ##        ##        ##  ##  {CEND}",
        f"{CORG}     ##      ##        ##            ##     ##   ##    ##       ##       ##    ## {CEND}", 
        f"{CORG}     ##      ########  ########      ##     ##  ##########      ##      ##########{CEND}",
        f"{CORG}     ##            ##        ##      ##     ##  ##      ##      ##      ##      ##{CEND}",
        f"{CORG}     ##            ##        ##      ##     ##  ##      ##      ##      ##      ##{CEND}",
        f"{CORG}     ##      ########  ########      #######    ##      ##      ##      ##      ##{CEND}",
    ]
    clear_terminal()
    for line in art2:
        padding = (t_width - len(line)) // 2
        print(" " * padding + line)

    print("\n\n                     Alsalamu Alaikum Wa Rahmatu Allah\n\n")
    while True:
        x = input("What is the first pillar of Islam: ")
        if x.lower() == "shahada":
            clear_terminal()
            for line in art1:
                padding = (t_width - len(line)) // 2
                print(" " * padding + line)
            break
        else:
            continue


if __name__ == "__main__":
    print_allah()

