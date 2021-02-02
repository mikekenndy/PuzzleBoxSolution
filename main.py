

def sumPosition(rows):
    vals = [0, 0, 0, 0]

    for position in range(4):
        for i in range(5):
            if vals[position] == 0 and rows[i][position] != 0:
                vals[position] = rows[i][position]

    return sum(vals)

def is42(layers, config):

    # layers[layer][ring][position]
    # config[l0, l1, l2, l3]

    for i in range(12):
        rows = [[0 for y in range(4)] for x in range(5)]
        for layer in range(5):
            v0 = layers[layer][0][config[layer]]
            v1 = layers[layer][1][config[layer]]
            v2 = layers[layer][2][config[layer]]
            v3 = layers[layer][3][config[layer]]
            rows[layer] = [v0, v1, v2, v3]
        if sumPosition(rows) != 42:
            return False
        for c in range(5):
            if config[c] == 11:
                config[c] = 0
            else:
                config[c] += 1
    return True


def Solve(layers):
    for i in range(12):
        for j in range(12):
            for k in range(12):
                for l in range(12):
                    for m in range(12):
                        order = [i, j, k, l, m]
                        if is42(layers, order):
                            print(order)


if __name__ == '__main__':

    layer0 = [[6, 0, 10, 0, 7, 0, 15, 0, 8, 0, 3, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    layer1 = [[6, 17, 7, 3, 0, 6, 0, 11, 11, 6, 11, 0],
              [12, 0, 4, 0, 7, 15, 0,  0, 14, 0,  9, 0],
              [0,  0, 0, 0, 0,  0, 0,  0,  0, 0,  0, 0],
              [0,  0, 0, 0, 0,  0, 0,  0,  0, 0,  0, 0]]

    layer2 = [[9, 13, 9, 7, 13, 21, 17, 4, 5, 0, 7, 8],
              [21, 6, 15,  4,  9, 18, 11, 26, 14,  1, 12,  0],
              [5,  0, 10,  0,  8,  0, 22,  0, 16,  0,  9,  0],
              [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]

    layer3 = [[7, 0, 9, 0, 7, 14, 11, 0, 8, 0, 16, 2],
              [9, 20, 12,  3,  6,  0, 14, 12,  3,  8,  9,  0],
              [3, 26,  6,  0,  2, 13,  9,  0, 17, 19,  3, 12],
              [1,  0,  9,  0, 12,  0,  6,  0, 10,  0, 10,  0]]

    layer4 = [[14, 11, 14, 11, 14, 14, 11, 14, 11, 14, 11, 11],
              [6,   7,  8,  9, 10, 11, 12, 13, 14, 15,  4,  5],
              [6,   6,  3,  3, 14, 14, 21, 21,  9,  9,  4,  4],
              [4,  12,  2,  5, 10,  7, 16,  8,  7,  8,  8,  3]]

    Solve([layer0, layer1, layer2, layer3, layer4])