import random

def simulate_zkp(trials=20):
    success_count = 0
    for _ in range(trials):
        path_entered = random.choice(['A', 'B'])
        challenge = random.choice(['A', 'B'])
        knows_password = True # Set to False to simulate an attacker

        if knows_password:
            success = True
        else:
            success = path_entered == challenge
        if success:
            success_count += 1

    print(f"Successful responses: {success_count}/{trials}")

simulate_zkp()