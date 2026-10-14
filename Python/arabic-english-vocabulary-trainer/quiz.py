from time import sleep

def save_words(line):
    with open("savedwords.txt", "a", encoding="utf-8") as saveWordsFile:
        saveWordsFile.write(line)
def update_wordlist(line,lines):
    lines.remove(line)
    with open("2500.txt", "w", encoding="utf-8") as wordListFileUpdate:
        wordListFileUpdate.writelines(lines)
def ask_question(arabic):
    return input(f"What does {arabic} stand for in en : ").lower().strip()
def congrats():
    return "Congrats u finish the quiz 🧑‍🎓"


with open("2500.txt", "r", encoding="utf-8") as wordListFile:
    lines = wordListFile.readlines()
    if not lines:
        print(congrats())
    else:
        for line in lines[:]:
            challenge = line.strip().split(" ",maxsplit=1)
            if len(challenge) < 2:
                continue
           
            english,arabic = challenge[0],challenge[1]
            answer = ask_question(arabic)
            
            while answer != english:
                print("Wrong answer ! ❌")
                sleep(0.2)
                answer = ask_question(arabic)
            print(f"correct answer ! {english} 📗")
            save_words(line)
            update_wordlist(line,lines)



