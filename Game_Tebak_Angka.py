import random

guessRange = 0

def randomize(start, stop):
    return random.randint(start, stop)

def setRange():
    print('Pilih tingkat kesulitan:\n' +
    '1. Sangat mudah\n' +
    '2. Mudah\n' +
    '3. Sedang\n' +
    '4. Sulit\n')
    choice = input('Masukkan pilihan Anda: ')

    global guessRange
    if choice == '1' or choice.lower() == 'sangat mudah':
        guessRange = 10
    elif choice == '2' or choice.lower() == 'mudah':
        guessRange = 50
    elif choice == '3' or choice.lower() == 'sedang':
        guessRange = 100
    elif choice == '4' or choice.lower() == 'sulit':
        guessRange = 200
    else:
        print('Pilihan tidak valid')
        setRange()
        
    return guessRange

def generateNumber():
    guessRange = setRange()
    number = randomize(1, guessRange)
    return number

def generateClue(n, lastLowRange, lastHighRange):
    generateSentence = [
        'Clue ke-{}: \n Bilangan ini LEBIH dari sama dengan {}'.format(n, lastLowRange),
        'Clue ke-{}: \n Bilangan ini KURANG dari sama dengan {}'.format(n, lastHighRange),
    ]
    # print('guessRange ', guessRange)
    if guessRange > 10:
        generateSentence.append('Clue ke-{}: \n Bilangan ini ada di ANTARA {} dan {}'.format(n, lastLowRange, lastHighRange))

    return generateSentence

def guessNumber():
    generatedNumber = generateNumber()
    clue = 1
    score = 100
    lastLowRange = randomize(0, generatedNumber)
    lastHighRange = randomize(generatedNumber + 1, guessRange)
    while True:
        print(generateClue(clue, lastLowRange, lastHighRange)[randomize(0, len(generateClue(clue, lastLowRange, lastHighRange)) - 1)])
        guess = int(input('Masukkan tebakan Anda: '))
        # print('\n\nGeneratedNumber', generatedNumber)
        if guess == generatedNumber:
            print('\n\n\nSelamat! Anda berhasil menebak dengan benar. Skor Anda adalah {}\n'.format(score))
            break
        else:
            clue += 1
            score = score -10 if guessRange <= 50 else score -5
            print('\nTebakan Anda Salah')
            print('skor ', score)
            print('Coba lagi!\n')
            if score < 1:
                print('\n\n\nSkor Anda sudah habis. Anda kalah')
                print('Bilangannya adalah {}'.format(generatedNumber))
                break
            if (guess <= generatedNumber + 10 and guess >= generatedNumber - 10 and guessRange >= 50) or (guess <= generatedNumber + 5 and guess >= generatedNumber - 5 and guessRange < 50):
                print('\nTebakan Anda sangat dekat dengan bilangan yang benar\n')
                lastLowRange = randomize(generatedNumber - (10 if guessRange <= 50 else 5), generatedNumber)
                lastHighRange = randomize(generatedNumber, generatedNumber + (10 if guessRange <= 50 else 5))
            else:
                lastLowRange = randomize(0, generatedNumber) if guess < generatedNumber else lastLowRange
                lastHighRange = randomize(generatedNumber + 1, guessRange) if guess > generatedNumber else lastHighRange


if __name__ == "__main__":
    guessNumber()