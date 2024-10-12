import matplotlib.pyplot as plt
import networkx as nx


# パーセプトロンの図を描く
def draw_perceptron_diagram():
    G = nx.DiGraph()

    # ノード（入力、バイアス、重み、シグマ、活性化関数、出力）
    G.add_node("1", pos=(0, 1))
    G.add_node("x1", pos=(0, 0.5))
    G.add_node("x2", pos=(0, 0))
    G.add_node("a", pos=(2, 0.5))
    G.add_node("y", pos=(4, 0.5))

    # エッジ（入力、バイアス、重み、シグマ、活性化関数、出力）
    G.add_edges_from([("1", "a"), ("x1", "a"), ("x2", "a")])
    # G.add_edges_from([("b", "a"), ("w1", "a"), ("w2", "a")])
    G.add_edge("a", "y")
    # G.add_edge("h(a)", "y")

    # ノード位置の取得
    pos = nx.get_node_attributes(G, 'pos')

    # 図の描画
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgray", font_size=10, font_weight="bold",
            arrows=True, arrowstyle='-|>', arrowsize=20)

    # 矢印上にテキスト（b, w1, w2）
    edge_labels = {("1", "a"): 'b', ("x1", "a"): 'w1', ("x2", "a"): 'w2'}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    # グラフ表示
    plt.title("Perceptron Diagram with Bias and Activation Function")
    plt.show()


# 図を表示
draw_perceptron_diagram()
