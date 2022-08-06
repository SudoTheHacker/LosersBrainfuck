# Version 0.1 (pc for proof of concept)


# Losers brainfuck for the one that dont have the time
# What's new
# i to insert char
# v to make variable
# g"NO spaces tho" to go to your variable
# [() kinda self explantory Delayed because its 2:30 am

# Known problem: No comment support

# file = open("script.lbf", 'r')
# code = str(file.readlines())
code = "i'h'.>i'e'."
# num = int(input("num of input: "))
# list_input = {}
# input_pos = 0
# x = 0
# while x != num:
#     list_input[x] = input("input: ")
#     x = x + 1
# x = 0

code_lenght = len(code)

blocks = {}
block_pos = 0
block_set = {}

vinsert = False
vname = ""
variables = {}
variables_name = {}
variable_pos = 0

insert = False
insert_start = False

goto = False
goto_pos = 0

x = 0
def action():
    global block_pos, block_set, insert, insert_start, vinsert, goto, goto_pos, x, list_input
    if block_pos not in block_set:
        blocks[block_pos] = 0
        block_set[block_pos] = block_pos
    # Insert function
    if insert == True:
        if code[x] == "'":
            blocks[block_pos] = ord(code[x+1])
            x = x + 2
            insert = False
        else:
            print("Error: Please use like this i'only one character'")
            exit()
    # insert/create new variable
    if vinsert == True:
        if code[x] == "'" and insert_start == True:
            variables_name[variable_pos] = vname
            variables[variable_pos] = block_pos
            vname = ""
            vinsert = False
            insert_start = False
            variable_pos = variable_pos + 1
        if insert_start and code[x] != "'":
            vname = vname + str(code[x])
        if insert_start == False:
            if code[x] == "'":
                insert_start = True
            else:
                print("Error: Please use like this v'variable name'")
                exit()
    # Move to new block
    if goto == True:
        if code[x] == "'" and insert_start == True:
            y=0
            while vname != variables_name[y]:
                if y > variable_pos:
                    print("Error: Could not find requested variable")
                    y=y+1
            block_pos = y
            vname = ""
            goto = False
            insert_start = False
        if insert_start:
            vname = vname + str(code[x])
        if insert_start == False:
            if code[x] == "'":
                insert_start = True
            else:
                print("Error: Please use like this g'variable name'")
                exit()
    # Code reading
    if insert == False and vinsert == False and goto == False:
        if code[x] == "i":
            insert = True
        if code[x] == '>':
            block_pos = block_pos+1
        if code[x] == '<':
            block_pos = block_pos-1
        if code[x] == '+':
            blocks[block_pos] = blocks[block_pos] + 1
        if code[x] == '-':
            blocks[block_pos] = blocks[block_pos] - 1
        if code[x] == ',':
            blocks[block_pos] = ord(list_input[input_pos])
            input_pos = input_pos + 1
        if code[x] == '.':
            print(chr(blocks[block_pos]), end="")
        if code[x] == 'v':
            vinsert = True
        if code[x] == 'g':
            goto = True
        if code[x] == 'q':
            exit()
        if code[x] == "[":
            pass
    x = x + 1
print()

class while_loop:
  loop_start = 0
  loop_end = 0
  def startLoop():
      action()
while x != code_lenght:
    action()
print()
