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
    
    # TODO: Request a response from the OpenAI model using the full conversation history for context
    response = client.chat.completions.create(
        model="gpt-4",
        messages=chat_sessions[chat_id]
    )
    # TODO: Extract the model's response and append it to the conversation history under the 'assistant' role
    assistant_message = response.choices[0].message.content
    
    chat_sessions[chat_id].append({"role": "assistant","content": assistant_message})
    
    # TODO: Return the processed response from the assistant
    return assistant_message

# Create a chat session
chat_id = create_chat()

# Send a message to the created chat session
print("Response:", send_message(chat_id, "I'm having trouble with my recent order. Can you help me track it?"))

# Print the entire conversation history for the chat session
print("\nConversation History:")
for message in chat_sessions[chat_id]:
    print(f"- {message['role'].capitalize()}: {message['content']}")