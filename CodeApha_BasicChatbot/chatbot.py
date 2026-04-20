def chatbot():
    print("Chatbot: Hello User!!! Type 'bye' to exit")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello" or user == "hi":
            print("Chatbot: Hi!!")

        elif user == "how are you":
            print("Chatbot: I am fine, Thanks!")

        elif user == "bye":
            print ("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: I dont Know. Please Try Again")

chatbot()
