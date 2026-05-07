from objects import word, make_whitehead_graph, draw_whitehead_graph, genRandWord, getFreeGroup
fg = getFreeGroup(4)
w = genRandWord(fg, 30, 5)[0]
ug = make_whitehead_graph(w)
draw_whitehead_graph(ug, output="test.png")
