#Question_To_Answer_setup.
question = {
    'hi':'hello!' , 'how are you':'Iam Fine' ,'what is your name?':'My Name Is Chatbot','who is your devloper?':'My Devloper is Rihanul islam.  '
}

while True:
    try:
        ques=input("Ready To Chat.....:")
        if ques=='quite':
          break
        else:
            print(question[ques])
    except:
        print("I don't Know . Remainder: Always Use small Letter.")

