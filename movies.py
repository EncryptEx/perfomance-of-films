skips = [False, False, False, False]
print("Assuming N as not Y.")
for i in range(4):
    skips[i]
skip = input(f"Skip Step {i+1}? (Y/N)")
if skip.lower() in ['y', 'n']:
    skip[i] = (skip == "Y" or skip == "y")