import datetime
import random

def get_response(user_input):
    """
    Returns a response based on the user's message.
    Handles greetings, questions, commands, and small talk.
    """
    message = user_input.strip().lower()

    # --- Greetings ---
    if message in ("hello", "hi", "hey", "greetings"):
        return random.choice(["Hi there!", "Hello!", "Hey! How can I help?","wats up"])

    # --- How are you ---
    if message in ("how are you", "how are you doing", "how's it going"):
        return random.choice([
            "I'm doing great, thanks for asking!",
            "I'm just a bunch of code, but I'm feeling fantastic!",
            "All systems operational! How about you?"
        ])

    # --- Time ---
    if message in ("what time is it", "time", "current time"):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."

    # --- Date ---
    if message in ("what's the date", "date", "today's date"):
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {today}."

    # --- Joke ---
    if message in ("tell me a joke", "joke", "make me laugh"):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my computer I needed a break, and now it won't stop sending me KitKat ads.",
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "What do you call a fake noodle? An impasta!"
        ]
        return random.choice(jokes)

    # --- Fun fact ---
    if message in ("tell me a fact", "fact", "interesting fact"):
        facts = [
            "Honey never spoils. Archaeologists have found 3000-year-old honey in Egyptian tombs that was still edible.",
            "Octopuses have three hearts and blue blood.",
            "A group of flamingos is called a 'flamboyance'.",
            "Bananas are berries, but strawberries aren't!"
        ]
        return random.choice(facts)

    # --- Simple calculator ---
    if message.startswith("calculate") or message.startswith("what is"):
        # Try to extract a simple math expression like "2 + 2" or "10 * 5"
        expr = message.replace("calculate", "").replace("what is", "").strip()
        if expr:
            try:
                # Only allow safe characters: digits, operators, parentheses, decimal point
                allowed = set("0123456789+-*/(). ")
                if all(c in allowed for c in expr):
                    result = eval(expr)  # Caution: eval is used here for simplicity in a controlled environment
                    return f"The answer is {result}."
                else:
                    return "I can only do basic math with numbers and +, -, *, /."
            except Exception:
                return "Hmm, I couldn't calculate that. Try something like '2 + 2'."
        else:
            return "Please give me a math expression, e.g., 'calculate 5 * 3'."

    # --- Help ---
    if message in ("help", "what can you do", "commands"):
        return (
            "I can do the following:\n"
            "- Greet you (hello, hi)\n"
            "- Tell you how I'm doing\n"
            "- Give the current time or date\n"
            "- Tell a joke\n"
            "- Share a fun fact\n"
            "- Do simple math (e.g., 'calculate 12 / 4')\n"
            "- Say goodbye (bye)\n"
            "Just type naturally and I'll try my best!"
        )

    # --- Goodbye ---
    if message in ("bye", "goodbye", "see you", "exit", "quit"):
        return "Goodbye! Have a great day!"

    # --- Fallback ---
    return "I'm not sure I understand. Type 'help' to see what I can do."

def main():
    print(" Chatbot: Hello! I'm your friendly rule-based bot. Type 'help' For Further Details.")
    
    while True:
        user_input = input("You: ")
        if user_input.strip() == "":
            continue  # ignore empty input
        
        response = get_response(user_input)
        print(f" Chatbot: {response}")
        
        # Exit if the user says goodbye
        if user_input.strip().lower() in ("bye", "goodbye", "exit", "quit", "see you"):
            break

if __name__ == "__main__":
    main()