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

# TODO: Define a function named send_message that takes chat_id and user_message as parameters
    # TODO: Check if chat_id exists in chat_sessions dictionary, raise ValueError if not
    # TODO: Append a dictionary with 'role' as 'user' and 'content' as user_message to chat_sessions[chat_id]
    # TODO: Create a variable fixed_response with the string "Hi, how can I help you?"
    # TODO: Append a dictionary with 'role' as 'assistant' and 'content' as fixed_response to chat_sessions[chat_id]
    # TODO: Return the fixed_response string
def send_message(chat_id, user_message):
    if chat_id not in chat_sessions:
        raise ValueError("Chat session not found!")
        
    chat_sessions[chat_id].append({"role": "user","content": user_message})
    
    fixed_response = "Hi, how can I help you?"
    
    chat_sessions[chat_id].append({"role": "assistant", "content": fixed_response})
    
    return fixed_response
         
# Create a chat session
chat_id = create_chat()

# Send a message to the created chat session
print("Response:", send_message(chat_id, "I'm having trouble with my recent order. Can you help me track it?"))

# Print the entire conversation history for the chat session
print("\nConversation History:")
for message in chat_sessions[chat_id]:
    print(f"- {message['role'].capitalize()}: {message['content']}")
    