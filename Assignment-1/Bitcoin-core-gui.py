import PySimpleGUI as sg
import os, random, string, json

dir = "C:\Program Files\Bitcoin\daemon"
os.chdir(dir)

sg.theme("DarkBlue")

layout = [
        [sg.Button("Generate Wallet"), sg.Button("Generate Target Address"), sg.Multiline(disabled=True, key="-target_address-")],
        [sg.Text("Amount to send"), sg.Input(key="-send_amount-"), sg.Button("Send")],
        [sg.Text("Target Address"), sg.Input(key="-TargetAddress-")],
        [sg.Button("Show Balance"), sg.Text("Balance Remaining: " ,key="-outputbox-")],
        [sg.Button("List Unspent", key="-unspent-button-"), sg.Text(" " ,key="-unspentbox-")],
        [sg.Button("Hide Unspent", visible=False, key="-hide-unspent-")],
        [sg.Button("Wallet Name"), sg.Text("", key="-wallet-info-")],
        [sg.Text("Current Wallet: None", key="-currentwallet-")],
        [sg.Button("Load Main Wallet"), sg.Button("Load Target Wallet")],
        [sg.Button("Unload Main Wallet"), sg.Button("Unload Target Wallet")]
       
]

window = sg.Window("Blockchain Assignment 1 - Mads Møller Hansen", layout)

letters = string.ascii_lowercase
main_wallet = ''.join(random.choice(letters) for i in range(10))
target_wallet = ''.join(random.choice(letters) for i in range(10))

while True:
    event, values = window.read()

    if event == "Generate Wallet":
        print("Creating Wallet...")
        os.system("bitcoin-cli createwallet {} ".format(main_wallet))
        print("Wallet Created!")

        print("Loading Wallet...")
        os.system("bitcoin-cli loadwallet {} ".format(main_wallet))
        print("Wallet Loaded!")

        wallet_address = os.popen("bitcoin-cli getnewaddress").read()
        print("Wallet Address: " + str(wallet_address))

        #print("Generating 101 Blocks...")

        os.system("bitcoin-cli generatetoaddress 101 {}".format(wallet_address))
        print("Generated 101 Blocks!")

        window["-currentwallet-"].update("Current Wallet: {}".format("Main Wallet"))

        #  print("Receiving Block Count...")
        #os.system("bitcoin-cli getblockcount")
        # print("Block Count Received!")

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Show Balance":
        print("Checking Balance")
        balance = os.popen("bitcoin-cli getbalance").read() 
        print("Balance Received")
        window["-outputbox-"].update("Balance Remaining: " + balance)

    if event == "Send":
        target = values["-TargetAddress-"]
        amount = values["-send_amount-"]
        os.system("bitcoin-cli sendtoaddress {} {}".format(target, amount)) 
        sg.popup("Successfully sent {} BTC to {}".format(amount, target))

    if event == "-unspent-button-":
        unspent = os.popen("bitcoin-cli listunspent 0").read()
        window["-unspentbox-"].update("{}".format(unspent))
        window["-hide-unspent-"].update(visible=True)
        window["-unspent-button-"].update(visible=False)

    if event == "-hide-unspent-":
        window["-unspentbox-"].update("")
        window["-unspent-button-"].update(visible=True) 
        window["-hide-unspent-"].update(visible=False)

    if event == "Generate Target Address":

        print("Creating Wallet...")
        os.system("bitcoin-cli createwallet {} ".format(target_wallet))
        print("Wallet Created!")

        print("Loading Wallet...")
        os.system("bitcoin-cli loadwallet {} ".format(target_wallet))
        print("Wallet Loaded!")

        wallet_address = os.popen("bitcoin-cli getnewaddress").read()
        print("Wallet Address: " + str(target_wallet))
        window["-target_address-"].update("{}".format(wallet_address))

        window["-currentwallet-"].update("Current Wallet: {}".format("Target Wallet"))

    if event == "Wallet Name":
        wallet_info = os.popen("bitcoin-cli getwalletinfo").read()
        if wallet_info != None:
            x = json.loads(wallet_info)
            name = x["walletname"]
            window["-wallet-info-"].update("{}".format(name))
        else:
            print("No wallet loaded!")

    if event == "Unload Main Wallet":
        os.system("bitcoin-cli unloadwallet {}".format(main_wallet))
        window["-currentwallet-"].update("Current Wallet: {}".format("None"))
    if event == "Unload Target Wallet":
        os.system("bitcoin-cli unloadwallet {}".format(target_wallet))
        window["-currentwallet-"].update("Current Wallet: {}".format("None"))
    if event == "Load Main Wallet":
        os.system("bitcoin-cli loadwallet {}".format(main_wallet))
        window["-currentwallet-"].update("Current Wallet: {}".format("Main Wallet"))
    if event == "Load Target Wallet":
        os.system("bitcoin-cli loadwallet {}".format(target_wallet))
        window["-currentwallet-"].update("Current Wallet: {}".format("Target Wallet"))

window.close()
