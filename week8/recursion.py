def deep_find_BFS(data, key):
    to_be_in = []

    def search(data, key):
        if key in data:
            return data[key]
        for elem in data:
            if type(data[elem]) is dict:
                to_be_in.append(data[elem])
        for elem in to_be_in:
            handle = elem
            to_be_in.remove(elem)
            ans = search(handle, key)
            if ans is not None:
                return ans
    return search(data, key)


def deep_find_DFS(data, key):
    to_be_in = []

    def search(data, key):
        if key in data:
            return data[key]
        for elem in data:
            if type(data[elem]) is dict:
                to_be_in.append(data[elem])
        helper = to_be_in[::-1]
        for elem in helper:
            handle = elem
            to_be_in.remove(elem)
            helper.remove(elem)
            ans = search(handle, key)
            if ans is not None:
                return ans

    return search(data, key)


def deep_find_all_BFS(data, key):
    to_be_in = []
    answers = []

    def search(data, key):
        if key in data:
            answers.append(data[key])
        for elem in data:
            if type(data[elem]) is dict:
                to_be_in.append(data[elem])
        for elem in to_be_in:
            handle = elem
            to_be_in.remove(elem)
            search(handle, key)
        return answers

    return search(data, key)


def deep_find_all_DFS(data, key):
    to_be_in = []
    answers = []

    def search(data, key):
        if key in data:
            answers.append(data[key])
        for elem in data:
            if type(data[elem]) is dict:
                to_be_in.append(data[elem])
        helper = to_be_in[::-1]
        for elem in helper:
            handle = elem
            to_be_in.remove(elem)
            helper.remove(elem)
            search(handle, key)
        return answers

    return search(data, key)


def deep_update(data, key, value):
    to_be_in = []

    def search(data, key):
        if key in data:
            data[key] = value
        for elem in data:
            if type(data[elem]) is dict:
                to_be_in.append(data[elem])
        for elem in to_be_in:
            handle = elem
            to_be_in.remove(elem)
            search(handle, key)

    return search(data, key)
