import webbrowser as wb

def workauto():
    chrome_path ='c:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS =(
        "gmail.com",
        "github.com/haile12michael12",
        "youtube.com",
        "google.com"
    )
    for url in URLS:
        wb.get(chrome_path).open(url)
        
        workauto()
        