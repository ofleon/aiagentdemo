from customagent import MyAgent

def main():
    print("Welcome to the NBA Ai Agent!")

    name = input("1️⃣ What would you like to name your team? ").strip()
    while not name:
        name = input("Please enter a valid team name: ").strip()

    features = input("2️⃣ What feature would you like to focus on? ").strip()

    currentdatainput = input("3️⃣ Do you want to include current data from 2025 and future predictions? Plese enter yes or no ").strip()

    while currentdatainput.lower() not in ["yes", "no"]:
        currentdatainput = input("Please enter 'yes' or 'no': ").strip().lower()

    currentdata = currentdatainput == "yes"

    agent = MyAgent()

    prompt = f"Create the best NBA Team in the world that include or no the following features {features}"
    if currentdata:
        prompt += " and include current data from 2025 and future predictions."
    response = agent.chat(prompt, currentdata)
    print(f"Agent: {response}")


if __name__ == "__main__":
    main()