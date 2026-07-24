"""
Generates 04-workflow-diagram.png — the Current-State Workflow for
"Xanh SM: Dieu phoi ho tro tai xe bao pin yeu" (see 02-deep-dive-report.md).

Run:
    python extras/generate_workflow_diagram.py
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

STEPS = [
    {
        "title": "Buoc 1",
        "desc": "Tai xe goi hotline\nbao pin yeu",
        "who": "Ai: Tai xe -> Tong dai",
        "time": "1 phut",
        "bottleneck": False,
        "handoff": True,
    },
    {
        "title": "Buoc 2",
        "desc": "Tong dai xac nhan\nthong tin xe, mo phieu",
        "who": "Ai: Tong dai vien",
        "time": "2 phut",
        "bottleneck": False,
        "handoff": False,
    },
    {
        "title": "Buoc 3",
        "desc": "Tra cuu vi tri GPS\nxe tren ban do",
        "who": "Ai: Dieu phoi vien",
        "time": "3 phut",
        "bottleneck": False,
        "handoff": True,
    },
    {
        "title": "Buoc 4",
        "desc": "Tra cuu tram sac\nVinFast con tru trong",
        "who": "Ai: Dieu phoi vien",
        "time": "6 phut",
        "bottleneck": True,
        "handoff": False,
    },
    {
        "title": "Buoc 5",
        "desc": "Soan & gui tin nhan\nhuong dan tai xe",
        "who": "Ai: Dieu phoi vien",
        "time": "5 phut",
        "bottleneck": True,
        "handoff": False,
    },
]

BOX_W, BOX_H = 2.4, 1.9
GAP = 0.7
N = len(STEPS)

fig_w = N * (BOX_W + GAP) + 1
fig, ax = plt.subplots(figsize=(fig_w, 4.5))
ax.set_xlim(0, fig_w)
ax.set_ylim(0, 5)
ax.axis("off")

fig.suptitle(
    "Current-State Workflow — Xanh SM: Dieu phoi ho tro tai xe bao pin yeu",
    fontsize=13, fontweight="bold", y=0.98,
)

y0 = 2.2
for i, step in enumerate(STEPS):
    x0 = 0.7 + i * (BOX_W + GAP)

    face = "#ffe3e3" if step["bottleneck"] else "#e8f0fe"
    edge = "#d64545" if step["bottleneck"] else "#3b5bdb"

    box = FancyBboxPatch(
        (x0, y0), BOX_W, BOX_H,
        boxstyle="round,pad=0.05,rounding_size=0.08",
        linewidth=2, edgecolor=edge, facecolor=face,
    )
    ax.add_patch(box)

    ax.text(x0 + BOX_W / 2, y0 + BOX_H - 0.28, step["title"],
            ha="center", va="top", fontsize=10, fontweight="bold")
    ax.text(x0 + BOX_W / 2, y0 + BOX_H - 0.62, step["desc"],
            ha="center", va="top", fontsize=8.3)
    ax.text(x0 + BOX_W / 2, y0 + 0.42, step["who"],
            ha="center", va="top", fontsize=7.5, style="italic", color="#333")
    ax.text(x0 + BOX_W / 2, y0 + 0.16, step["time"],
            ha="center", va="top", fontsize=8.5, fontweight="bold",
            color="#d64545" if step["bottleneck"] else "#1a1a1a")

    if step["bottleneck"]:
        ax.text(x0 + BOX_W - 0.18, y0 + BOX_H - 0.16, "BOTTLENECK",
                ha="right", va="top", fontsize=6.5, fontweight="bold",
                color="#d64545")

    if i < N - 1:
        x_arrow0 = x0 + BOX_W
        x_arrow1 = x_arrow0 + GAP
        y_arrow = y0 + BOX_H / 2
        arrow = FancyArrowPatch(
            (x_arrow0 + 0.05, y_arrow), (x_arrow1 - 0.05, y_arrow),
            arrowstyle="-|>", mutation_scale=16, linewidth=1.8, color="#444",
        )
        ax.add_patch(arrow)
        if step["handoff"]:
            ax.text((x_arrow0 + x_arrow1) / 2, y_arrow + 0.28, "Handoff",
                    ha="center", va="bottom", fontsize=7, style="italic", color="#3b5bdb")

total_time = sum(int(s["time"].split()[0]) for s in STEPS)
legend_y = 1.35
red_patch = mpatches.Patch(facecolor="#ffe3e3", edgecolor="#d64545", label="Bottleneck step")
blue_patch = mpatches.Patch(facecolor="#e8f0fe", edgecolor="#3b5bdb", label="Normal step (Handoff marked on arrow)")
ax.legend(handles=[red_patch, blue_patch], loc="lower left",
          bbox_to_anchor=(0.0, -0.02), fontsize=8.5, frameon=False)
ax.text(0.7, legend_y - 0.55,
        f"Tong thoi gian xu ly thu cong: {total_time} phut/luot",
        fontsize=9.5, ha="left", fontweight="bold")

out_path = os.path.join(os.path.dirname(__file__), "..", "04-workflow-diagram.png")
out_path = os.path.abspath(out_path)
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(out_path, dpi=200, bbox_inches="tight")
print(f"Saved diagram to: {out_path}")
