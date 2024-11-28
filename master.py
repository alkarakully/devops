
CRED = '\033[91m'
CEND = '\033[0m'
CGRN = '\033[92m'
CBLU = '\033[96m'
CYLW = '\033[93m'
CMGT = '\033[35m'
CORG = '\033[38;5;208m'

def print_allah():
    art1 = [
        f"\n\n\n{CGRN}    ###    ##       ##          ###    ##     ##   {CEND}{CYLW}##  ######## {CEND}{CBLU}   ##########  ##     ##  #######{CEND}",
        f"{CGRN}   ## ##   ##       ##         ## ##   ##     ##   {CEND}{CYLW}    ##       {CEND}{CBLU}       ##      ##     ##  ##     {CEND}",
        f"{CGRN}  ##   ##  ##       ##        ##   ##  ##     ##   {CEND}{CYLW}##  ##       {CEND}{CBLU}       ##      ##     ##  ##     {CEND}",
        f"{CGRN} ######### ##       ##       ######### #########   {CEND}{CYLW}##  ######## {CEND}{CBLU}       ##      #########  #######{CEND}",
        f"{CGRN} ##     ## ##       ##       ##     ## ##     ##   {CEND}{CYLW}##        ## {CEND}{CBLU}       ##      ##     ##  ##     {CEND}",
        f"{CGRN} ##     ## ##       ##       ##     ## ##     ##   {CEND}{CYLW}##        ## {CEND}{CBLU}       ##      ##     ##  ##     {CEND}",
        f"{CGRN} ##     ## ######## ######## ##     ## ##     ##   {CEND}{CYLW}##  ######## {CEND}{CBLU}       ##      ##     ##  #######{CEND}",
        "",
        f"{CRED}      #######    ########   #########     ###     ##########  #########  ########  ##########{CEND}",
        f"{CRED}     ##     ##   ##     ##  ##           ##  ##       ##      ##         ##            ##    {CEND}",
        f"{CRED}     ##          ##     ##  ##          ##    ##      ##      ##         ##            ##    {CEND}",
        f"{CRED}     ##   ####   ########   ########   ##########     ##      ########   ########      ##    {CEND}",
        f"{CRED}     ##     ##   ##   ##    ##         ##      ##     ##      ##               ##      ##    {CEND}",
        f"{CRED}     ##     ##   ##    ##   ##         ##      ##     ##      ##               ##      ##    {CEND}",
        f"{CRED}      #######    ##     ##  #########  ##      ##     ##      #########  ########      ##    {CEND}\n\n\n",
    ]

    art2 = [
           f" \n\n\n{CORG} ##########  ########  ########      #######       ###      ##########     ###{CEND}",
           f" {CORG}    ##      ##        ##            ##     ##    ##  ##        ##        ##  ##{CEND}",
           f" {CORG}    ##      ##        ##            ##     ##   ##    ##       ##       ##    ##{CEND}", 
           f" {CORG}    ##      ########  ########      ##     ##  ##########      ##      ##########{CEND}",
           f" {CORG}    ##            ##        ##      ##     ##  ##      ##      ##      ##      ##{CEND}",
           f" {CORG}    ##            ##        ##      ##     ##  ##      ##      ##      ##      ##{CEND}",
           f" {CORG}    ##      ########  ########      #######    ##      ##      ##      ##      ##{CEND}\n\n\n",
    ]

    for line in art2:
        print(line)

    print("\n\n                     Alsalamu Alaikum Wa Rahmatu Allah\n\n")
    while True:
        x = input("What is the first pillar of Islam: ")
        if x.lower() == "shahada":
            for line in art1:
                print(line)
            break
        else:
            continue


if __name__ == "__main__":
    print_allah()

