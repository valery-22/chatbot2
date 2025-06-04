import uuid
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Store all active chat sessions
chat_sessions = {}

# Define a common system prompt for all conversations
system_prompt = {
    "role": "system",
    "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}

# Create a new chat session with a unique identifier
def create_chat():
    chat_id = str(uuid.uuid4())  # Create unique session identifier
    chat_sessions[chat_id] = []  # Initialize empty conversation history
    chat_sessions[chat_id].append(system_prompt)  # Add system prompt to conversation history
    return chat_id

# Send a message in a specific chat session and get a response
def send_message(chat_id, user_message):
    # Ensure we're adding to a valid conversation
    if chat_id not in chat_sessions:
        raise ValueError("Chat session not found!")
    
    # Add the new message to conversation history
    chat_sessions[chat_id].append({"role": "user", "content": user_message})
    
    # Get AI's response while maintaining conversation context
    response = client.chat.completions.create(
        model="gpt-4",
        messages=chat_sessions[chat_id]  # Full history for context
    )
    
    # Process response and maintain conversation history
    answer = response.choices[0].message.content.strip()
    chat_sessions[chat_id].append({"role": "assistant", "content": answer})
    return answer

# TODO: Create the first chat session and store its id
# TODO: Send a first message in Chat 1 and print the response
# TODO: Send a follow-up message in Chat 1 and print the response
first_chat_session = create_chat()
print("Chat 1, First Message:", send_message(first_chat_session, "I'm having trouble with my most recent order. Can you help me track it?"))
print("Chat 1, Follow-up Message:", send_message(first_chat_session, "It was supposed to arrive yesterday but hasn't. What should I do next?"))
# TODO: Create the second chat session and store its id
# TODO: Send a first message in Chat 2 and print the response
# TODO: Send a follow-up message in Chat 2  and print the response
second_chat_session = create_chat()
print("Chat 2, First Message:", send_message(second_chat_session, "I'm interested in upgrading my membership. What are the benefits?"))
print("Chat 2, Follow-up Message:", send_message(second_chat_session, "Could you guide me through the upgrade process?"))
# TODO: Print both conversation histories to confirm they are separate
print("\nConversation History for Chat 1:")
for msg in chat_sessions[first_chat_session]:
    print(f"- {msg['role'].capitalize()}:{msg['content']}")
print("\nConversation History for Chat 2:")
for msg in chat_sessions[second_chat_session]:
    print(f"- {msg['role'].capitalize()}: {msg['content']}")