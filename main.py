from search import *


def main():
    puzzler = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0))
    print("Question 5")
    print(puzzler.actions(state=(0, 1, 2, 3, 4, 5, 6, 7, 8)))
    print("Question 6")
    print(puzzler.result(state=(0, 1, 2, 3, 4, 5, 6, 7, 8), action='DOWN'))
    print("Question 7")
    puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0))
    print(breadth_first_graph_search(puzzle).solution())
    print(len((breadth_first_graph_search(puzzle).solution())))
    return


if __name__ == '__main__':
    main()
