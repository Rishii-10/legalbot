import json

#Load existing responses from a JSON file (if available)
try:
    with open('responses.json', 'r') as file:
        responses = json.load(file)
except FileNotFoundError:
    responses = {}

def save_responses():
    # Save the responses back to the JSON file
    with open('responses.json', 'w') as file:
        json.dump(responses, file, indent=4)

def chatbot():
    print("Chatbot: Hello! I'm your chatbot.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        if user_input in responses:
            print(f"Chatbot: {responses[user_input]}")
        else:
            print("Chatbot: I don't know the answer to that question. Please provide an answer:")
            new_response = input("You (to teach the chatbot): ")
            responses[user_input] = new_response
            save_responses()
            print("Chatbot: Thank you! I've learned something new.")

if __name__ == "__main__":
    chatbot()
