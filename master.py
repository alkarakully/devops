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

    art3 = [
        f"{CGRN} _______   _____    _____   _____           _______          {CEND}{CBLU}                _                        _   _             {CEND}",
        f"{CGRN}|__   __| / ____|  / ____| |  __ \     /\  |__   __|  /\     {CEND}{CBLU}     /\        | |                      | | (_)            {CEND}", 
        f"{CGRN}   | |   | (___   | (___   | |  | |   /  \    | |    /  \    {CEND}{CBLU}    /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __  {CEND}",
        f"{CGRN}   | |    \___ \   \___ \  | |  | |  / /\ \   | |   / /\ \   {CEND}{CBLU}   / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ {CEND}",
        f"{CGRN}   | |    ____) |  ____) | | |__| | / ____ \  | |  / ____ \  {CEND}{CBLU}  / ____ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | |{CEND}",
        f"{CGRN}   |_|   |_____/  |_____/  |_____/ /_/    \_\ |_| /_/    \_\ {CEND}{CBLU} /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|{CEND}"
    ] 

    clear_terminal()
    for line in art2:
        padding = (t_width - len(line)) // 2
        print(" " * padding + line)

    for line in art3:
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

