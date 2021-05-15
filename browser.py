import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style


def print_user_view(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.find_all(["p", "a", "h1", "h2", "ul", "ol", "li"])
    output = []
    for line in text:
        output.append(line.text)
        if line.name == "a":
            print(Fore.BLUE + line.text + Style.RESET_ALL)
        else:
            print(line.text)
    return output


last = []
while True:
    user = input().lower()
    if user == "exit":
        break
    elif user == "back":
        if len(last) > 1:
            last.pop()
            print(last.pop())
        continue
    else:
        if "." in user:
            if not user.startswith("https://"):
                user = "https://" + user
            request = requests.get(user)
            final = print_user_view(request)
            last.append("\n".join(final))
        else:
            print("Incorrect URL")
