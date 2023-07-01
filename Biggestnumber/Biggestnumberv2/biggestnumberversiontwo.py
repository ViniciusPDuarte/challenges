import languages
print("1-english\n2-portuguese")
opt = int(input("choose a language: "))
print()
if opt == 1:
    languages.ing()
if opt == 2:
    languages.port()
