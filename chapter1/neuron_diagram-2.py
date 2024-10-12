import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as patches


def draw_perceptron_diagram():
    G = nx.DiGraph()

    # ノード（入力、バイアス、シグマ、出力）
    G.add_node("1", pos=(0.3, 1))
    G.add_node("x1", pos=(0.3, 0.5))
    G.add_node("x2", pos=(0.3, 0))
    G.add_node("a", pos=(1, 0.5))
    G.add_node("y", pos=(1.5, 0.5))

    # エッジ（入力、バイアス、シグマ、出力）
    G.add_edges_from([("1", "a"), ("x1", "a"), ("x2", "a")])
    G.add_edge("a", "y")

    # ノード位置の取得
    pos = nx.get_node_attributes(G, 'pos')

    # 各ノードのサイズ（1, x1, x2は1.5倍のサイズ）
    node_sizes = [4500 if node in ["1", "x1", "x2"] else 3000 for node in G.nodes()]

    # 塗りつぶしの色：1ノードのみグレー、それ以外は透明
    node_colors = ['lightgray' if node == "1" else 'none' for node in G.nodes()]

    # 図の描画
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color=node_colors,
            font_size=10, font_weight="bold", edgecolors='black',  # ノードの境界色を黒に
            arrows=True, arrowstyle='-|>', arrowsize=20)

    # 矢印上にテキスト（b, w1, w2, h()）
    edge_labels = {("1", "a"): 'b', ("x1", "a"): 'w1', ("x2", "a"): 'w2', ("a", "y"): 'h( )'}
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color='black', rotate=False, verticalalignment='bottom',
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'), label_pos=0.5)

    # x軸とy軸に余白を持たせる
    plt.xlim(-0.5, 2.5)  # x軸の範囲（左右の余白を設定）
    plt.ylim(-0.5, 1.5)  # y軸の範囲（上下の余白を設定）

    # aとyのノードを囲む外接円の追加
    circle = patches.Circle(((pos["a"][0] + pos["y"][0]) / 2, pos["a"][1]), 0.4,
                            fill=False, edgecolor='black', linestyle='solid')
    plt.gca().add_patch(circle)

    # グラフ表示
    plt.title("Perceptron Diagram with Margins and Encircled Nodes")
    plt.show()


# 図を表示
draw_perceptron_diagram()
