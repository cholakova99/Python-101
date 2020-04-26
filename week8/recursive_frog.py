def create_input(number):
    start_input = number * ">" + "_" + number * "<"
    return start_input


def game_expected_exit(inp):
    helper = inp.split("_")
    ex = helper[1] + "_" + helper[0]
    return ex


def next_possible_jumps(inp, possible_ans):
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


# we use wrong_way for nodes we have visited and nodes that are deadlock
def game(tree, wanted_result, path_to_tree, wrong_way):
    helper = tree[0]
    if helper in wrong_way:
        tree.pop(0)
        if helper in path_to_tree:
            path_to_tree.remove(helper)
        return game(tree, wanted_result, path_to_tree, wrong_way)

    possible_pos = next_possible_jumps(helper, [])
    if wanted_result in possible_pos:
        path_to_tree.append(helper)
        path_to_tree.append(wanted_result)
        return path_to_tree

    if len(possible_pos) == 0 or (len(possible_pos) == 1 and len(next_possible_jumps(possible_pos[0], [])) == 0):
        wrong_way.append(helper)
        tree.pop(0)
        return game(tree, wanted_result, path_to_tree, wrong_way)

    path_to_tree.append(helper)
    wrong_way.append(helper)

    for pos_elm in possible_pos:
        if len(next_possible_jumps(pos_elm, [])) == 0:
            wrong_way.append(pos_elm)
        if pos_elm not in wrong_way:
            tree.insert(0, pos_elm)
    return game(tree, wanted_result, path_to_tree, wrong_way)


def print_path(pth):
    for i in range(len(pth) - 1):
        print(pth[i], "  ~JUMP~  ", end='')
    print(pth[len(pth) - 1])


def create_game():
    all_frogs = int(input("How many frogs do we have?: "))
    frogs = int(all_frogs / 2)
    print(frogs)
    game_begin = create_input(frogs)
    wanted_result = game_expected_exit(game_begin)
    print("START POSITION: ", game_begin)
    print("WANTED POSITION: ", wanted_result)
    tree = next_possible_jumps(game_begin, [])
    path = game(tree, wanted_result, [], [])
    return path


correct_alg = create_game()
print_path(correct_alg)
print("JUMPS MADE : ", len(correct_alg))
