import sys, time
write = sys.stdout.write

text = "Malik Junaid Fiaz"

for i, c in enumerate(text):  
	if i%2 == 0:
		print("Loading.. +", end="\r")
	else:
		print("Loading.. -", end="\r")
	time.sleep(.5)
	# print(i)
print("\n")
print("DONE")