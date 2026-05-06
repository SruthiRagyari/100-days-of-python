# Day 8 - Caesar Cipher

## What I Built

A CLI Caesar Cipher tool that encodes or decodes a message by shifting each letter a specified number of positions through the alphabet. Supports repeated use in a single session and handles non-alphabet characters (spaces, punctuation) gracefully.

## Concepts Used

- `import art` — import a custom/local module for the logo display
- `alphabet.index(letter)` — get the numeric position of a letter in the alphabet list
- Modulo operator (`%`) — wrap around the alphabet so shifts beyond `z` cycle back to `a`
- Negative shift for decoding — multiplying `shift_amount` by `-1` reuses the same encode logic for decode
- `for` loop over a string — iterate character by character through the input message
- `not in` operator — detect non-alphabet characters and pass them through unchanged
- String concatenation (`+=`) — build the output string one character at a time
- Named function arguments — call `caesar(original_text=..., shift_amount=..., encode_or_decode=...)` for clarity
- `while` loop with a boolean flag (`should_continue`) — keep the program running until the user explicitly quits

## Code

```python
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
```

## Sample Output

```
[Caesar Cipher ASCII logo]

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
Here is the encoded result: khoor zruog

Type 'yes' if you want to go again. Otherwise, type 'no'.
yes

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog
Type the shift number:
3
Here is the decoded result: hello world

Type 'yes' if you want to go again. Otherwise, type 'no'.
no
Goodbye
```

## What I Learned

- Flipping the shift to negative for decoding (`shift_amount *= -1`) is a clean trick — encode and decode become the exact same operation, just in opposite directions, so you only need one function
- `% len(alphabet)` is essential — without it, a shift that pushes past `z` would cause an index error; modulo wraps it back around to the start of the alphabet automatically
- Passing non-alphabet characters straight through (`if letter not in alphabet`) means spaces and punctuation survive the cipher intact without any special handling
- Using a `should_continue` boolean flag is a readable way to control a `while` loop — it's clearer than `while True` with a `break` buried inside
- Calling the function with named arguments (`original_text=text, shift_amount=shift`) makes the call site self-documenting — you don't have to remember the parameter order
