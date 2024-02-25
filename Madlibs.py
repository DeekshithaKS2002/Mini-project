def madlib_generator():
    # Get user input
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    # Fill in the Madlib template
    madlib = f"The {adjective} {noun} likes to {verb} {adverb}."

    # Display the completed Madlib
    print("\nYour Madlib:")
    print(madlib)

# Call the function to generate a Madlib
madlib_generator()
