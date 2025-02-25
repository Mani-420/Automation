import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
# Multan Rd Sabzazar Block H House 71 Street 4
#https://www.google.com/maps/search/Multan+Rd+Sabzazar+Block+H+House+71+Street+4
webbrowser.open('https://www.google.com/maps/search/' + address)