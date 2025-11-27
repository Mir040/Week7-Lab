import random

def simulate_zkp(trials=20):
    success_count = 0

    for _ in range(trials):
        # Malicious Prover (Attacker) selects a path to enter/guess
        path_entered = random.choice(['A', 'B']) # [cite: 11]
        
        # Verifier (Bob) issues a random challenge
        challenge = random.choice(['A', 'B']) # [cite: 12]
        
        # *** Simulating a Malicious Prover (Attacker) ***
        knows_password = False # [cite: 13, 15]
        
        if knows_password:
            # A genuine prover would always succeed (by using the password)
            success = True # [cite: 16]
        else:
            # A malicious prover must have guessed the path Bob asks for
            success = path_entered == challenge # 
        
        if success:
            success_count += 1 # [cite: 19]

    # Calculate and print the results
    probability = success_count / trials
    
    print(f"Successful responses (Malicious Prover): {success_count}/{trials}") # [cite: 20]
    print(f"Success Probability: {probability:.2f} ({probability*100:.0f}%)")

simulate_zkp(trials=20) # [cite: 21]