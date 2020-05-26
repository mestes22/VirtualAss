import webbrowser

def search(command):
    search_command = command.split(" ")[1:]
    search_command = " ".join(search_command)
    url = "https://www.google.com.tr/search?q={}".format(search_command)
    webbrowser.open_new_tab(url)