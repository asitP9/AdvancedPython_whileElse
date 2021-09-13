# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def is_comment(item):
    return isinstance(item, str) and item.startswith("#")

def execute(program):
    """
    Execute a stack program
    Args:
    program: Any stack-like containing where each item in the stack
    is a callable operators or non callable operands. The top most items on the stack may be strings
    beginning with the '#' for the purposes of documentation. stack-like means support for:

    item= stack.pop()  # remove and return the top item
    stack.append(item) # push an item to the top
    if stack:          # false in a boolean context when empty
    """

    # Find the start of the 'program' by skipping
    # any item which is a comment
    while program:
        item=program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else: # nobreak
        print("empty program")
        return

    # Evaluate the program
    pending=[]
    while program:
        item=program.pop()
        if callable(item):
            try:
                result=item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:
        print("Program successful")
        print("Result: ", pending)
    print("Finished")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import operator
    program=list(reversed((
        "# A short stack program to add",
        "# and multiply some constants",
        5,
        2,
        operator.add,
        3,
        operator.mul)))
    execute(program)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
