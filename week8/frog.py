def create_input(number):
    helper = number
    start_input = ""
    while number != 0:
        number -= 1
        start_input += ">"
    start_input += "_"
    while helper != 0:
        helper -= 1
        start_input += "<"
    return start_input


def logic(inp, possible_ans):
    index = inp.find("_")
    if index > 1 and inp[index - 2] == ">":
        way = inp[:index - 2] + "_" + inp[index - 1] + ">" + inp[index + 1:]
        possible_ans.append(way)
    if index > 0 and inp[index - 1] == ">":
        way = inp[:index - 1] + "_" + ">" + inp[index + 1:]
        possible_ans.append(way)
    if index < len(inp) - 1 and inp[index + 1] == "<":
        way = inp[:index] + "<" + "_" + inp[index + 2:]
        possible_ans.append(way)
    if index < len(inp) - 2 and inp[index + 2] == "<":
        way = inp[:index] + "<" + inp[index + 1] + "_" + inp[index + 3:]
        possible_ans.append(way)
    return possible_ans


def game_expected_exit(inp):
    helper = inp.split("_")
    ex = helper[1] + "_" + helper[0]
    return ex


def game(tree, wanted_result, path_to_tree):
    print("wanted result ->", wanted_result)
    if wanted_result in tree:
        path_to_tree.append(wanted_result)
        return path_to_tree
    while tree != []:
        elem = tree.pop(0)
        if elem is wanted_result:
            path_to_tree.append(elem)
            return path_to_tree
        path_to_tree.append(elem)
        pos = logic(elem, [])
        if wanted_result in pos:
            path_to_tree.append(wanted_result)
            return path_to_tree
        for pos_elem in pos:
            tree.insert(0, pos_elem)


def print_path(pth):
    for i in range(len(pth) - 1):
        print(pth[i], "   JUMP   ", end='')
    print(pth[len(pth) - 1])


def create_game():
    all_frogs = int(input("How many frogs do we have?: "))
    frogs = all_frogs / 2
    game_begin = create_input(frogs)
    wanted_result = game_expected_exit(game_begin)
    print("START POSITION: ", game_begin)
    print("WANTED POSITION: ", wanted_result)
    tree = logic(game_begin, [])
    path = game(tree, wanted_result, [])
    return path


correct_alg = create_game()
print_path(correct_alg)