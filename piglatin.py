def pig_latin():
    phrase = input("Enter the phrase: ")
    word_list = phrase.split()
    arrLength = len(word_list)
    for x in range(arrLength):
        singleword = word_list[x]
        pigword = singleword.lower()
        if(pigword[0] != 'a' and pigword[0] != 'e' and pigword[0] != 'i' and pigword[0] != 'o' and pigword[0] != 'u'):
            finalword = pigword[1:]+pigword[0]
            print(finalword + "ay",end=" ")
        #when it is not a vowel:
        else:
            print(pigword + "hay", end=" ")
        
        
#make the program interactive, such that it keeps
#translating phrases into pig latin until the user enters
#in the phrase "stop"
isrunning = True
while isrunning:
    pig_latin()
    keeprunning = input("\nIf you want to stop type \"stop\", otherwise press enter: ")
    if(keeprunning == 'stop'):
        print("Thanks for using pigLatin")
        isrunning = False

