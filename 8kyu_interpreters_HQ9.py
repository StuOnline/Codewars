def HQ9(code):
    single_99_bottles_line = "{} bottles of beer on the wall, {} bottles of beer.\n\
    Take one down and pass it around, {} bottles of beer on the wall.\n"
    all_99_bottles_lines = [single_99_bottles_line.format(x, x, x-1) for x in range(99, 2, -1)]
    last_99_bottles_lines = "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around,\
     1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around,\
      no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store\
       and buy some more, 99 bottles of beer on the wall."
    full_99_bottles_lyrics = "".join(all_99_bottles_lines) + last_99_bottles_lines
    
    if code == 'H':
        print("Hello World!")
    elif code == 'Q': 
        print(code)
    elif code == '9': 
        print(full_99_bottles_lyrics)
    else:
        print(None)

HQ9('9')    