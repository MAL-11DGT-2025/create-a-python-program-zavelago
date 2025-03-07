bible = input("What is the first chapter in the Bible?\na) Genesis\nb Exodus\nc Numbers\nd Leviticus\n>>")

correct = ["a", "a)", "genesis", "a) genesis"]
incorrect = ["b", "b)", "exodus", "b) exodus", "c",  "c)", "numbers", "c) numbers", "d", "d)", "leviticus", "d) leviticus"]

if bible.lower().strip() in correct:
    print("Correct")
elif bible.lower().strip() in incorrect:
    print("Incorrect")
else:
    print("Invalid")