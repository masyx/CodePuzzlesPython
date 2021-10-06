inputText = input("Type text: ")

lettersCounter, wordCounter, sentenceCounter  = 0, 0, 0

#words = len(inputText.split())
#print(f"Words: {words}")

for char in inputText:
    if char.isalpha():
        lettersCounter += 1
        isAWord = True
    if (isAWord and char.isspace()) or (isAWord and (char == '.' or char == '!' or char == '?')):
        wordCounter += 1
        isAWord = False
    if char == '.' or char == '!' or char == '?':
        sentenceCounter += 1

#print(f"{lettersCounter} letters\n{wordCounter} words\n{sentenceCounter} sentences")

L = (lettersCounter * 100) / wordCounter
S = (sentenceCounter * 100) / wordCounter

index = 0.0588 * L - 0.296 * S - 15.8

if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(index)}")