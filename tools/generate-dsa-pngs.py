#!/usr/bin/env python3
"""Generate high-quality Data Structures diagrams as PNG using matplotlib.

This script redraws all diagrams used in `content/en/data-structures/*.md`
without relying on SVG conversion.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

# Keep matplotlib/font caches in a writable location in restricted environments.
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


OUT_DIR = Path("assets/img/data-structures")

COLORS = {
    "bg": "#f8fafc",
    "panel": "#ffffff",
    "line": "#475569",
    "muted": "#64748b",
    "subtle": "#94a3b8",
    "accent": "#2563eb",
    "accent_light": "#dbeafe",
    "success": "#16a34a",
    "success_light": "#dcfce7",
    "danger": "#dc2626",
    "danger_light": "#fee2e2",
    "warn": "#d97706",
    "warn_light": "#fef3c7",
    "gray_light": "#e2e8f0",
    "gray_mid": "#cbd5e1",
    "text": "#0f172a",
}


def make_canvas(title: str, subtitle: str = ""):
    fig, ax = plt.subplots(figsize=(12, 6), dpi=220)
    fig.patch.set_facecolor(COLORS["bg"])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis("off")

    panel = FancyBboxPatch(
        (1, 1),
        98,
        58,
        boxstyle="round,pad=0.8,rounding_size=2",
        linewidth=1.2,
        edgecolor=COLORS["gray_mid"],
        facecolor=COLORS["panel"],
    )
    ax.add_patch(panel)
    ax.text(4, 56, title, fontsize=16, color=COLORS["text"], fontweight="bold")
    if subtitle:
        ax.text(4, 52.4, subtitle, fontsize=10.8, color=COLORS["muted"])

    return fig, ax


def save(fig, filename: str):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / filename
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(out, dpi=220, facecolor=COLORS["bg"])
    plt.close(fig)


def arrow(
    ax,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str = COLORS["line"],
    lw: float = 1.8,
    rad: float = 0.0,
    style: str = "-|>",
    mscale: int = 14,
):
    patch = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle=style,
        mutation_scale=mscale,
        linewidth=lw,
        color=color,
        connectionstyle=f"arc3,rad={rad}",
    )
    ax.add_patch(patch)


def draw_cell(
    ax,
    x: float,
    y: float,
    value: str,
    index: int | None = None,
    w: float = 10,
    h: float = 8,
    fill: str = COLORS["panel"],
    edge: str = COLORS["gray_mid"],
    txt: str = COLORS["text"],
    lw: float = 1.6,
):
    rect = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.3,rounding_size=1.2",
        linewidth=lw,
        edgecolor=edge,
        facecolor=fill,
    )
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h / 2 + 0.1, str(value), ha="center", va="center", fontsize=12, color=txt)
    if index is not None:
        ax.text(
            x + w / 2,
            y - 2.0,
            str(index),
            ha="center",
            va="center",
            fontsize=9,
            color=COLORS["subtle"],
        )


def draw_array(
    ax,
    values: Iterable,
    *,
    x: float,
    y: float,
    w: float = 10,
    h: float = 8,
    highlight_idx: int | None = None,
    deleted_idx: int | None = None,
    shifted: tuple[int, ...] = (),
):
    for i, value in enumerate(values):
        fill = COLORS["panel"]
        edge = COLORS["gray_mid"]
        text = COLORS["text"]
        lw = 1.6
        if i == highlight_idx:
            fill = COLORS["accent_light"]
            edge = COLORS["accent"]
            text = "#1d4ed8"
            lw = 2.1
        if i == deleted_idx:
            fill = COLORS["danger_light"]
            edge = COLORS["danger"]
            text = COLORS["danger"]
            lw = 2.1
        draw_cell(ax, x + i * w, y, value, i, w=w, h=h, fill=fill, edge=edge, txt=text, lw=lw)

    for idx in shifted:
        sx = x + idx * w + w / 2
        arrow(ax, sx, y + h + 1.2, sx + w, y + h + 1.2, color=COLORS["warn"], lw=1.4, style="->", mscale=12)


def draw_ll_node(
    ax,
    x: float,
    y: float,
    value: str,
    *,
    w: float = 12,
    h: float = 8,
    fill: str = COLORS["panel"],
    edge: str = COLORS["gray_mid"],
    txt: str = COLORS["text"],
    lw: float = 1.6,
):
    rect = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.3,rounding_size=1.1",
        linewidth=lw,
        edgecolor=edge,
        facecolor=fill,
    )
    ax.add_patch(rect)
    split_x = x + w * 0.7
    ax.plot([split_x, split_x], [y, y + h], color=edge, linewidth=1.4)
    ax.text(x + w * 0.35, y + h / 2, str(value), ha="center", va="center", fontsize=11.5, color=txt)
    ax.text(x + w * 0.85, y + h / 2, "next", ha="center", va="center", fontsize=8.8, color=COLORS["subtle"])


def draw_linked_list(
    ax,
    values: list[int],
    *,
    x: float,
    y: float,
    highlight_idx: int | None = None,
    deleted_idx: int | None = None,
):
    w = 12
    h = 8
    gap = 4
    for i, value in enumerate(values):
        fill = COLORS["panel"]
        edge = COLORS["gray_mid"]
        txt = COLORS["text"]
        lw = 1.6
        if i == highlight_idx:
            fill = COLORS["accent_light"]
            edge = COLORS["accent"]
            txt = "#1d4ed8"
            lw = 2.0
        if i == deleted_idx:
            fill = COLORS["danger_light"]
            edge = COLORS["danger"]
            txt = COLORS["danger"]
            lw = 2.0
        node_x = x + i * (w + gap)
        draw_ll_node(ax, node_x, y, str(value), w=w, h=h, fill=fill, edge=edge, txt=txt, lw=lw)

    for i in range(len(values) - 1):
        x1 = x + i * (w + gap) + w
        y1 = y + h / 2
        x2 = x + (i + 1) * (w + gap)
        arrow(ax, x1 + 0.5, y1, x2 - 0.6, y1, color=COLORS["line"], lw=1.8)

    if values:
        head_x = x + w * 0.35
        arrow(ax, head_x, y + h + 5, head_x, y + h + 0.9, color=COLORS["success"], lw=1.8)
        ax.text(head_x, y + h + 6.5, "head", ha="center", va="bottom", fontsize=9.5, color=COLORS["success"], fontweight="bold")
        tail_x = x + (len(values) - 1) * (w + gap) + w * 0.35
        arrow(ax, tail_x, y - 5, tail_x, y - 0.9, color=COLORS["warn"], lw=1.8)
        ax.text(tail_x, y - 6.5, "tail", ha="center", va="top", fontsize=9.5, color=COLORS["warn"], fontweight="bold")


def draw_stack(ax, values: list[int], *, x: float, y: float, w: float = 16, h: float = 6, highlight_top: bool = False):
    for i, value in enumerate(values):
        fill = COLORS["panel"]
        edge = COLORS["gray_mid"]
        text = COLORS["text"]
        lw = 1.6
        if highlight_top and i == len(values) - 1:
            fill = COLORS["accent_light"]
            edge = COLORS["accent"]
            text = "#1d4ed8"
            lw = 2.0
        draw_cell(ax, x, y + i * h, str(value), None, w=w, h=h, fill=fill, edge=edge, txt=text, lw=lw)
    arrow(ax, x + w + 5, y + len(values) * h - h / 2, x + w + 0.8, y + len(values) * h - h / 2, color=COLORS["success"])
    ax.text(x + w + 6.2, y + len(values) * h - h / 2, "top", va="center", fontsize=10, color=COLORS["success"], fontweight="bold")


def draw_queue(ax, values: list[int], *, x: float, y: float, w: float = 10, h: float = 8):
    for i, value in enumerate(values):
        draw_cell(ax, x + i * w, y, str(value), None, w=w, h=h)
    arrow(ax, x - 5.2, y + h / 2, x - 0.8, y + h / 2, color=COLORS["success"])
    ax.text(x - 6.1, y + h / 2, "front", ha="right", va="center", fontsize=9.8, color=COLORS["success"], fontweight="bold")
    arrow(ax, x + len(values) * w + 0.8, y + h / 2, x + len(values) * w + 5.2, y + h / 2, color=COLORS["warn"])
    ax.text(x + len(values) * w + 6.2, y + h / 2, "rear", ha="left", va="center", fontsize=9.8, color=COLORS["warn"], fontweight="bold")


def draw_tree(ax, pos: dict[str, tuple[float, float]], edges: list[tuple[str, str]], labels: dict[str, str],
              highlight_nodes: set[str] | None = None, new_nodes: set[str] | None = None,
              delete_nodes: set[str] | None = None, highlight_edges: set[tuple[str, str]] | None = None):
    highlight_nodes = highlight_nodes or set()
    new_nodes = new_nodes or set()
    delete_nodes = delete_nodes or set()
    highlight_edges = highlight_edges or set()

    for a, b in edges:
        x1, y1 = pos[a]
        x2, y2 = pos[b]
        color = COLORS["gray_mid"]
        lw = 1.6
        if (a, b) in highlight_edges or (b, a) in highlight_edges:
            color = COLORS["accent"]
            lw = 2.0
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, zorder=1)

    for node, (x, y) in pos.items():
        fill = COLORS["panel"]
        edge = COLORS["gray_mid"]
        txt = COLORS["text"]
        lw = 1.8
        if node in highlight_nodes:
            fill = COLORS["accent_light"]
            edge = COLORS["accent"]
            txt = "#1d4ed8"
            lw = 2.2
        if node in new_nodes:
            fill = COLORS["success_light"]
            edge = COLORS["success"]
            txt = COLORS["success"]
            lw = 2.2
        if node in delete_nodes:
            fill = COLORS["danger_light"]
            edge = COLORS["danger"]
            txt = COLORS["danger"]
            lw = 2.2

        circ = Circle((x, y), radius=3.2, facecolor=fill, edgecolor=edge, linewidth=lw, zorder=3)
        ax.add_patch(circ)
        ax.text(x, y, labels[node], ha="center", va="center", fontsize=11, color=txt, zorder=4, fontweight="bold")


# ---- Array diagrams -------------------------------------------------------

def array_get():
    fig, ax = make_canvas("Array get(index)", "Direct address calculation gives O(1) access")
    draw_array(ax, [10, 20, 30, 40, 50], x=8, y=24, highlight_idx=2)
    arrow(ax, 33, 50, 33, 33.0, color=COLORS["accent"], lw=2.0)
    ax.text(33, 50.8, "get(2)", ha="center", va="bottom", fontsize=11, color=COLORS["accent"], fontweight="bold")
    ax.text(63, 29, "returns 30", fontsize=13, color=COLORS["text"], fontweight="bold")
    ax.text(63, 24.8, "No traversal needed", fontsize=10.2, color=COLORS["muted"])
    save(fig, "array-get.png")


def array_append():
    fig, ax = make_canvas("Array append(value)", "Add at the end; resize only occasionally")
    ax.text(8, 45.5, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_array(ax, [10, 20, 30, 40], x=8, y=35)

    ax.text(8, 26.5, "After append(50)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_array(ax, [10, 20, 30, 40, 50], x=8, y=16, highlight_idx=4)

    arrow(ax, 54, 40, 54, 24, color=COLORS["success"], lw=2.0)
    ax.text(58, 31.6, "new element", fontsize=10.2, color=COLORS["success"], va="center")
    ax.text(68, 18, "Amortized O(1)", fontsize=11.5, color=COLORS["text"], fontweight="bold")
    save(fig, "array-append.png")


def array_insert():
    fig, ax = make_canvas("Array insert(index, value)", "Elements shift right from insertion point")
    ax.text(8, 45.5, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_array(ax, [10, 20, 40, 50], x=8, y=35)

    ax.text(8, 26.5, "Insert 30 at index 2", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_array(ax, [10, 20, 30, 40, 50], x=8, y=16, highlight_idx=2, shifted=(2, 3))

    arrow(ax, 33, 34.5, 33, 24.5, color=COLORS["accent"], lw=2.0)
    ax.text(36.5, 29.5, "insert here", fontsize=10, color=COLORS["accent"])
    ax.text(68, 17.8, "O(n) shift", fontsize=11.5, color=COLORS["text"], fontweight="bold")
    save(fig, "array-insert.png")


def array_delete():
    fig, ax = make_canvas("Array delete(index)", "Delete item and shift remaining elements left")
    ax.text(8, 45.5, "Before delete(index=2)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_array(ax, [10, 20, 30, 40, 50], x=8, y=35, deleted_idx=2)
    arrow(ax, 33, 35, 33, 31, color=COLORS["danger"], lw=2.0)

    ax.text(8, 25.0, "After", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_array(ax, [10, 20, 40, 50], x=8, y=16)
    arrow(ax, 48, 20, 38, 20, color=COLORS["warn"], lw=1.7, style="->")
    arrow(ax, 58, 20, 48, 20, color=COLORS["warn"], lw=1.7, style="->")

    ax.text(67, 19.2, "O(n) shift", fontsize=11.5, color=COLORS["text"], fontweight="bold")
    save(fig, "array-delete.png")


# ---- Linked list diagrams -------------------------------------------------

def linked_list_prepend():
    fig, ax = make_canvas("Linked list prepend(value)", "New node becomes head in O(1)")
    ax.text(8, 45.5, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_linked_list(ax, [10, 20, 30], x=8, y=35)

    ax.text(8, 25.5, "After prepend(5)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_linked_list(ax, [5, 10, 20, 30], x=8, y=15, highlight_idx=0)
    ax.text(70, 19, "Head pointer moves", fontsize=10.6, color=COLORS["muted"])
    ax.text(70, 15.3, "No shifting", fontsize=10.6, color=COLORS["muted"])
    save(fig, "linked-list-prepend.png")


def linked_list_append():
    fig, ax = make_canvas("Linked list append(value)", "Tail pointer keeps append O(1)")
    ax.text(8, 45.5, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_linked_list(ax, [10, 20, 30], x=8, y=35)

    ax.text(8, 25.5, "After append(40)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_linked_list(ax, [10, 20, 30, 40], x=8, y=15, highlight_idx=3)
    ax.text(70, 18.7, "Tail.next -> new", fontsize=10.6, color=COLORS["muted"])
    ax.text(70, 15.0, "Tail updates", fontsize=10.6, color=COLORS["muted"])
    save(fig, "linked-list-append.png")


def linked_list_find():
    fig, ax = make_canvas("Linked list find(value)", "Traverse node by node until match")
    draw_linked_list(ax, [10, 20, 30, 40], x=8, y=24, highlight_idx=2)

    ax.text(8, 44, "find(30)", fontsize=11.4, color=COLORS["accent"], fontweight="bold")
    arrow(ax, 14, 41, 14, 33, color=COLORS["accent"], lw=1.8)
    arrow(ax, 30, 41, 30, 33, color=COLORS["accent"], lw=1.8)
    arrow(ax, 46, 41, 46, 33, color=COLORS["accent"], lw=1.8)
    ax.text(11.2, 42, "step 1", fontsize=8.8, color=COLORS["accent"])
    ax.text(27.2, 42, "step 2", fontsize=8.8, color=COLORS["accent"])
    ax.text(43.2, 42, "found", fontsize=8.8, color=COLORS["success"])

    ax.text(67, 28.5, "result index = 2", fontsize=11.8, color=COLORS["text"], fontweight="bold")
    ax.text(67, 24.8, "Worst case O(n)", fontsize=10.2, color=COLORS["muted"])
    save(fig, "linked-list-find.png")


def linked_list_delete():
    fig, ax = make_canvas("Linked list delete(value)", "Relink pointers to skip deleted node")
    ax.text(8, 45.5, "Before delete(30)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_linked_list(ax, [10, 20, 30, 40], x=8, y=35, deleted_idx=2)

    bypass_start_x = 8 + 1 * (12 + 4) + 12
    bypass_end_x = 8 + 3 * (12 + 4)
    arrow(ax, bypass_start_x + 0.2, 39, bypass_end_x - 0.5, 39, color=COLORS["accent"], lw=2.2, rad=-0.25)
    ax.text(39, 42.3, "bypass", fontsize=9.2, color=COLORS["accent"])

    ax.text(8, 24.8, "After", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_linked_list(ax, [10, 20, 40], x=8, y=15)

    ax.text(70, 19.0, "Pointer relink", fontsize=10.4, color=COLORS["muted"])
    ax.text(70, 15.4, "No element shifting", fontsize=10.4, color=COLORS["muted"])
    save(fig, "linked-list-delete.png")


def linked_list_reverse():
    fig, ax = make_canvas("Linked list reverse()", "Flip next pointers in one pass")
    ax.text(8, 45.5, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_linked_list(ax, [10, 20, 30, 40], x=8, y=35)

    ax.text(8, 24.8, "After", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_linked_list(ax, [40, 30, 20, 10], x=8, y=15)

    arrow(ax, 46, 32, 46, 26, color=COLORS["accent"], lw=1.8)
    ax.text(49, 29, "all links reverse direction", fontsize=9.8, color=COLORS["accent"])
    ax.text(70, 18.8, "Time O(n)", fontsize=11.2, color=COLORS["text"], fontweight="bold")
    ax.text(70, 15.2, "Space O(1)", fontsize=10.2, color=COLORS["muted"])
    save(fig, "linked-list-reverse.png")


# ---- Stack/queue diagrams -------------------------------------------------

def stack_push():
    fig, ax = make_canvas("Stack push(value)", "LIFO: add to the top")
    ax.text(11, 44, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_stack(ax, [10, 20, 30], x=10, y=18)

    ax.text(45, 44, "After push(40)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_stack(ax, [10, 20, 30, 40], x=45, y=14, highlight_top=True)

    arrow(ax, 34, 33, 45, 39, color=COLORS["accent"], lw=2.0)
    ax.text(34.5, 35.2, "push", fontsize=10, color=COLORS["accent"])
    save(fig, "stack-push.png")


def stack_pop():
    fig, ax = make_canvas("Stack pop()", "LIFO: remove from the top")
    ax.text(11, 44, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_stack(ax, [10, 20, 30, 40], x=10, y=14, highlight_top=True)

    ax.text(45, 44, "After", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_stack(ax, [10, 20, 30], x=45, y=18)

    arrow(ax, 28, 38, 41, 49, color=COLORS["danger"], lw=2.1)
    ax.text(33, 50, "returns 40", fontsize=9.8, color=COLORS["danger"], fontweight="bold")
    save(fig, "stack-pop.png")


def queue_enqueue():
    fig, ax = make_canvas("Queue enqueue(value)", "FIFO: insert at rear")
    ax.text(8, 44, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_queue(ax, [10, 20, 30], x=10, y=28)

    ax.text(8, 24, "After enqueue(40)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_queue(ax, [10, 20, 30, 40], x=10, y=10)
    draw_cell(
        ax,
        40,
        10,
        "40",
        None,
        w=10,
        h=8,
        fill=COLORS["accent_light"],
        edge=COLORS["accent"],
        txt="#1d4ed8",
        lw=2.1,
    )

    arrow(ax, 52, 32, 52, 18, color=COLORS["accent"], lw=2.0)
    ax.text(54.5, 25, "new rear", fontsize=9.6, color=COLORS["accent"])
    save(fig, "queue-enqueue.png")


def queue_dequeue():
    fig, ax = make_canvas("Queue dequeue()", "FIFO: remove from front")
    ax.text(8, 44, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_queue(ax, [10, 20, 30], x=10, y=28)
    draw_cell(
        ax,
        10,
        28,
        "10",
        None,
        w=10,
        h=8,
        fill=COLORS["danger_light"],
        edge=COLORS["danger"],
        txt=COLORS["danger"],
        lw=2.1,
    )

    ax.text(8, 24, "After", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_queue(ax, [20, 30], x=20, y=10)

    arrow(ax, 15, 32, 4.5, 45, color=COLORS["danger"], lw=2.0)
    ax.text(4.7, 46.0, "returns 10", fontsize=9.8, color=COLORS["danger"], fontweight="bold")
    save(fig, "queue-dequeue.png")


# ---- Hash table diagrams --------------------------------------------------

def draw_bucket_chain(ax, x: float, y: float, key_values: list[tuple[str, str]],
                      highlight_key: str | None = None, delete_key: str | None = None):
    ax.add_patch(FancyBboxPatch((x, y), 8, 6, boxstyle="round,pad=0.2,rounding_size=0.8",
                                linewidth=1.5, edgecolor=COLORS["gray_mid"], facecolor=COLORS["panel"]))
    ax.text(x + 4, y + 3, "bucket", ha="center", va="center", fontsize=8.5, color=COLORS["subtle"])

    cx = x + 12
    for i, (k, v) in enumerate(key_values):
        fill = COLORS["panel"]
        edge = COLORS["gray_mid"]
        txt = COLORS["text"]
        lw = 1.4
        if k == highlight_key:
            fill = COLORS["accent_light"]
            edge = COLORS["accent"]
            txt = "#1d4ed8"
            lw = 2.0
        if k == delete_key:
            fill = COLORS["danger_light"]
            edge = COLORS["danger"]
            txt = COLORS["danger"]
            lw = 2.0
        node = FancyBboxPatch((cx + i * 14, y), 12, 6, boxstyle="round,pad=0.2,rounding_size=0.8",
                              linewidth=lw, edgecolor=edge, facecolor=fill)
        ax.add_patch(node)
        ax.text(cx + i * 14 + 6, y + 3, f"{k}:{v}", ha="center", va="center", fontsize=8.8, color=txt)
        if i == 0:
            arrow(ax, x + 8.3, y + 3, cx - 0.4, y + 3, color=COLORS["line"], lw=1.5)
        if i > 0:
            arrow(ax, cx + (i - 1) * 14 + 12.2, y + 3, cx + i * 14 - 0.4, y + 3, color=COLORS["line"], lw=1.5)


def draw_bucket_row(ax, x: float, y: float, n: int = 6, active_idx: int | None = None):
    w = 6.4
    h = 5.6
    gap = 1.2
    centers = []
    for i in range(n):
        fill = COLORS["panel"]
        edge = COLORS["gray_mid"]
        txt = COLORS["text"]
        lw = 1.4
        if i == active_idx:
            fill = COLORS["accent_light"]
            edge = COLORS["accent"]
            txt = "#1d4ed8"
            lw = 2.0
        draw_cell(
            ax,
            x + i * (w + gap),
            y,
            str(i),
            None,
            w=w,
            h=h,
            fill=fill,
            edge=edge,
            txt=txt,
            lw=lw,
        )
        centers.append((x + i * (w + gap) + w / 2, y + h / 2))
    return centers


def hash_table_set():
    fig, ax = make_canvas("Hash table set(key, value)", "Hash to bucket, then update or append in chain")

    ax.text(6, 46.5, "set('kiwi', 9)", fontsize=11.5, color=COLORS["accent"], fontweight="bold")
    ax.text(6, 42.6, "hash('kiwi') % 6 = 2", fontsize=10.0, color=COLORS["muted"])

    ax.text(6, 35.7, "Buckets", fontsize=10.2, color=COLORS["muted"], fontweight="bold")
    centers = draw_bucket_row(ax, x=6, y=29.2, n=6, active_idx=2)

    bx, by = centers[2]
    arrow(ax, bx, 41.6, bx, by + 3.2, color=COLORS["accent"], lw=2.0)
    ax.text(bx + 1.4, 37.7, "index 2", fontsize=9.2, color=COLORS["accent"])

    ax.text(25, 22.6, "Chain at bucket 2", fontsize=10.2, color=COLORS["muted"], fontweight="bold")
    draw_bucket_chain(ax, 23, 15.5, [("pear", "4"), ("kiwi", "9")], highlight_key="kiwi")
    ax.text(23, 11.0, "Collision: multiple keys share same bucket", fontsize=9.6, color=COLORS["muted"])

    ax.text(66, 22.0, "set inserts or updates", fontsize=10.2, color=COLORS["muted"])
    ax.text(66, 17.4, "Average O(1)", fontsize=12, color=COLORS["text"], fontweight="bold")
    save(fig, "hash-table-set.png")


def hash_table_get():
    fig, ax = make_canvas("Hash table get(key)", "Jump directly to one bucket, scan short chain")

    ax.text(6, 46.5, "get('banana')", fontsize=11.5, color=COLORS["accent"], fontweight="bold")
    ax.text(6, 42.6, "hash('banana') % 6 = 1", fontsize=10.0, color=COLORS["muted"])

    ax.text(6, 35.7, "Buckets", fontsize=10.2, color=COLORS["muted"], fontweight="bold")
    centers = draw_bucket_row(ax, x=6, y=29.2, n=6, active_idx=1)
    bx, by = centers[1]
    arrow(ax, bx, 41.6, bx, by + 3.2, color=COLORS["accent"], lw=2.0)
    ax.text(bx + 1.4, 37.7, "index 1", fontsize=9.2, color=COLORS["accent"])

    ax.text(25, 22.6, "Scan chain at bucket 1", fontsize=10.2, color=COLORS["muted"], fontweight="bold")
    draw_bucket_chain(ax, 23, 15.5, [("grape", "2"), ("banana", "8")], highlight_key="banana")
    arrow(ax, 45.2, 18.5, 48.2, 18.5, color=COLORS["accent"], lw=1.7, style="->", mscale=11)
    ax.text(43.8, 22.3, "scan -> match", fontsize=9.2, color=COLORS["accent"])

    ax.text(66, 22.0, "found value = 8", fontsize=12, color=COLORS["text"], fontweight="bold")
    ax.text(66, 17.8, "Only one bucket is inspected", fontsize=10.0, color=COLORS["muted"])
    save(fig, "hash-table-get.png")


def hash_table_delete():
    fig, ax = make_canvas("Hash table delete(key)", "Remove key from its bucket chain")

    ax.text(6, 46.5, "delete('banana')", fontsize=11.5, color=COLORS["danger"], fontweight="bold")
    ax.text(6, 42.6, "hash('banana') % 6 = 1", fontsize=10.0, color=COLORS["muted"])

    ax.text(8, 33.5, "Before (bucket 1 chain)", fontsize=10.2, color=COLORS["muted"], fontweight="bold")
    draw_bucket_chain(ax, 8, 26, [("grape", "2"), ("banana", "8"), ("melon", "6")], delete_key="banana")
    arrow(ax, 42, 25.3, 42, 20.2, color=COLORS["danger"], lw=2.0)

    ax.text(8, 16.8, "After deletion", fontsize=10.2, color=COLORS["muted"], fontweight="bold")
    draw_bucket_chain(ax, 8, 9.2, [("grape", "2"), ("melon", "6")])

    ax.text(66, 22.3, "Key removed from chain", fontsize=10.2, color=COLORS["muted"])
    ax.text(66, 18.2, "Size decremented", fontsize=10.2, color=COLORS["muted"])
    ax.text(66, 13.8, "Average O(1)", fontsize=12, color=COLORS["text"], fontweight="bold")
    save(fig, "hash-table-delete.png")


# ---- BST diagrams ---------------------------------------------------------

def bst_insert():
    fig, ax = make_canvas("BST insert(key)", "Compare and descend left/right until empty child")
    pos = {
        "50": (30, 42),
        "30": (20, 30),
        "70": (40, 30),
        "60": (35, 18),
        "80": (45, 18),
        "65": (38, 8),
    }
    edges = [("50", "30"), ("50", "70"), ("70", "60"), ("70", "80"), ("60", "65")]
    labels = {k: k for k in pos}

    draw_tree(
        ax,
        pos,
        edges,
        labels,
        highlight_nodes={"50", "70", "60"},
        new_nodes={"65"},
        highlight_edges={("50", "70"), ("70", "60"), ("60", "65")},
    )

    ax.text(57, 39, "insert(65)", fontsize=12, color=COLORS["accent"], fontweight="bold")
    ax.text(57, 33.8, "50 -> right", fontsize=10, color=COLORS["muted"])
    ax.text(57, 30.2, "70 -> left", fontsize=10, color=COLORS["muted"])
    ax.text(57, 26.6, "60 -> right", fontsize=10, color=COLORS["muted"])
    ax.text(57, 22.0, "Insert new node", fontsize=10, color=COLORS["success"])
    save(fig, "bst-insert.png")


def bst_search():
    fig, ax = make_canvas("BST contains(key)", "At each node follow one branch only")
    pos = {
        "50": (30, 42),
        "30": (20, 30),
        "70": (40, 30),
        "60": (35, 18),
        "80": (45, 18),
    }
    edges = [("50", "30"), ("50", "70"), ("70", "60"), ("70", "80")]
    labels = {k: k for k in pos}

    draw_tree(
        ax,
        pos,
        edges,
        labels,
        highlight_nodes={"50", "70", "60"},
        highlight_edges={("50", "70"), ("70", "60")},
    )

    ax.text(57, 39, "contains(60)", fontsize=12, color=COLORS["accent"], fontweight="bold")
    ax.text(57, 33.8, "60 > 50: go right", fontsize=10, color=COLORS["muted"])
    ax.text(57, 30.2, "60 < 70: go left", fontsize=10, color=COLORS["muted"])
    ax.text(57, 26.6, "60 == 60: found", fontsize=10, color=COLORS["success"], fontweight="bold")
    ax.text(57, 20.5, "Average O(log n)", fontsize=11.5, color=COLORS["text"], fontweight="bold")
    save(fig, "bst-search.png")


def bst_delete():
    fig, ax = make_canvas("BST delete(key)", "Two-child delete: replace with inorder successor")

    ax.text(7, 44, "Before delete(70)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    left_pos = {
        "50": (24, 36),
        "30": (16, 26),
        "70": (32, 26),
        "60": (28, 16),
        "80": (36, 16),
    }
    left_edges = [("50", "30"), ("50", "70"), ("70", "60"), ("70", "80")]
    draw_tree(ax, left_pos, left_edges, {k: k for k in left_pos}, delete_nodes={"70"}, highlight_nodes={"80"})

    ax.text(52, 44, "After", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    right_pos = {
        "50": (70, 36),
        "30": (62, 26),
        "80": (78, 26),
        "60": (74, 16),
    }
    right_edges = [("50", "30"), ("50", "80"), ("80", "60")]
    draw_tree(ax, right_pos, right_edges, {k: k for k in right_pos}, new_nodes={"80"})

    arrow(ax, 43, 30, 57, 30, color=COLORS["accent"], lw=2.1)
    ax.text(44, 33.2, "successor", fontsize=9.4, color=COLORS["accent"])
    save(fig, "bst-delete.png")


# ---- Heap diagrams --------------------------------------------------------

def heap_push():
    fig, ax = make_canvas("Heap push(value)", "Insert at end, then sift up")

    ax.text(8, 45.5, "Before: [4, 7, 5, 12, 15]", fontsize=10.2, color=COLORS["muted"])
    draw_array(ax, [4, 7, 5, 12, 15], x=8, y=36)

    ax.text(8, 30.0, "After append 3", fontsize=10.2, color=COLORS["muted"])
    draw_array(ax, [4, 7, 5, 12, 15, 3], x=8, y=20, highlight_idx=5)

    ax.text(8, 14.2, "After sift up", fontsize=10.2, color=COLORS["muted"])
    draw_array(ax, [3, 7, 4, 12, 15, 5], x=8, y=6, highlight_idx=0)

    arrow(ax, 63, 24, 63, 15, color=COLORS["accent"], lw=2.0)
    ax.text(66.2, 17.2, "sift up", fontsize=9.6, color=COLORS["accent"])
    ax.text(70, 8.4, "O(log n)", fontsize=11.5, color=COLORS["text"], fontweight="bold")
    save(fig, "heap-push.png")


def heap_pop():
    fig, ax = make_canvas("Heap pop()", "Remove root, move last, then sift down")

    ax.text(8, 45.5, "Before: [4, 7, 5, 12, 15, 9]", fontsize=10.2, color=COLORS["muted"])
    draw_array(ax, [4, 7, 5, 12, 15, 9], x=8, y=36, deleted_idx=0)

    ax.text(8, 30.0, "Move last to root", fontsize=10.2, color=COLORS["muted"])
    draw_array(ax, [9, 7, 5, 12, 15], x=8, y=20, highlight_idx=0)

    ax.text(8, 14.2, "After sift down", fontsize=10.2, color=COLORS["muted"])
    draw_array(ax, [5, 7, 9, 12, 15], x=8, y=6, highlight_idx=0)

    arrow(ax, 13, 39, 4.5, 50, color=COLORS["danger"], lw=2.1)
    ax.text(4.7, 51.0, "returns 4", fontsize=9.8, color=COLORS["danger"], fontweight="bold")
    arrow(ax, 13, 24, 13, 16, color=COLORS["accent"], lw=2.0)
    ax.text(15.3, 20, "sift down", fontsize=9.6, color=COLORS["accent"])
    ax.text(70, 8.3, "O(log n)", fontsize=11.5, color=COLORS["text"], fontweight="bold")
    save(fig, "heap-pop.png")


# ---- Graph diagrams -------------------------------------------------------

def draw_graph_nodes(ax, pos: dict[str, tuple[float, float]], highlights: set[str] | None = None):
    highlights = highlights or set()
    for name, (x, y) in pos.items():
        fill = COLORS["panel"]
        edge = COLORS["gray_mid"]
        txt = COLORS["text"]
        lw = 1.8
        if name in highlights:
            fill = COLORS["accent_light"]
            edge = COLORS["accent"]
            txt = "#1d4ed8"
            lw = 2.2
        circ = Circle((x, y), radius=3.0, facecolor=fill, edgecolor=edge, linewidth=lw, zorder=3)
        ax.add_patch(circ)
        ax.text(x, y, name, ha="center", va="center", fontsize=11, color=txt, fontweight="bold", zorder=4)


def draw_graph_edges(ax, pos: dict[str, tuple[float, float]], edges: list[tuple[str, str]],
                     highlight_edges: set[tuple[str, str]] | None = None,
                     dashed_edges: set[tuple[str, str]] | None = None):
    highlight_edges = highlight_edges or set()
    dashed_edges = dashed_edges or set()
    for a, b in edges:
        x1, y1 = pos[a]
        x2, y2 = pos[b]
        color = COLORS["line"]
        lw = 1.7
        ls = "-"
        if (a, b) in dashed_edges or (b, a) in dashed_edges:
            color = COLORS["subtle"]
            ls = "--"
        if (a, b) in highlight_edges or (b, a) in highlight_edges:
            color = COLORS["accent"]
            lw = 2.2
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, linestyle=ls, zorder=1)


def graph_add_edge():
    fig, ax = make_canvas("Graph add_edge(u, v)", "Insert a new connection in adjacency list")
    pos = {
        "A": (20, 35),
        "B": (35, 44),
        "C": (35, 26),
        "D": (52, 35),
    }

    ax.text(8, 49, "Before", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_graph_edges(ax, pos, [("A", "B"), ("A", "C"), ("B", "D")], dashed_edges={("C", "D")})
    draw_graph_nodes(ax, pos)

    arrow(ax, 60.5, 35, 69.2, 35, color=COLORS["accent"], lw=2.1)

    shifted = {k: (v[0] + 40, v[1]) for k, v in pos.items()}
    ax.text(70, 49, "After add_edge(C, D)", fontsize=10.5, color=COLORS["muted"], fontweight="bold")
    draw_graph_edges(ax, shifted, [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")], highlight_edges={("C", "D")})
    draw_graph_nodes(ax, shifted, highlights={"C", "D"})

    ax.text(65, 10, "Adjacency list update:", fontsize=10, color=COLORS["muted"])
    ax.text(65, 6.8, "C: [..., D]", fontsize=10, color=COLORS["text"], fontweight="bold")
    save(fig, "graph-add-edge.png")


def graph_bfs_dfs():
    fig, ax = make_canvas("Graph BFS vs DFS", "Same graph, different traversal order")
    pos = {
        "A": (25, 36),
        "B": (40, 46),
        "C": (40, 26),
        "D": (56, 40),
        "E": (56, 22),
    }
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]

    draw_graph_edges(ax, pos, edges)
    draw_graph_nodes(ax, pos, highlights={"A", "B", "C", "D", "E"})

    ax.text(6, 18.8, "BFS from A", fontsize=11.5, color=COLORS["accent"], fontweight="bold")
    ax.text(6, 15.2, "A, B, C, D, E", fontsize=11.0, color=COLORS["text"])

    ax.text(6, 10.0, "DFS from A", fontsize=11.5, color=COLORS["success"], fontweight="bold")
    ax.text(6, 6.4, "A, B, D, E, C", fontsize=11.0, color=COLORS["text"])

    arrow(ax, 25, 33, 40, 43, color=COLORS["accent"], lw=1.8)
    arrow(ax, 40, 43, 56, 37, color=COLORS["accent"], lw=1.8)
    arrow(ax, 56, 37, 56, 24, color=COLORS["accent"], lw=1.8)

    arrow(ax, 26, 31.8, 40, 28.2, color=COLORS["success"], lw=1.8)
    arrow(ax, 40, 28.2, 56, 23.5, color=COLORS["success"], lw=1.8)

    save(fig, "graph-bfs-dfs.png")


def generate_all():
    array_get()
    array_append()
    array_insert()
    array_delete()

    linked_list_prepend()
    linked_list_append()
    linked_list_find()
    linked_list_delete()
    linked_list_reverse()

    stack_push()
    stack_pop()
    queue_enqueue()
    queue_dequeue()

    hash_table_set()
    hash_table_get()
    hash_table_delete()

    bst_insert()
    bst_search()
    bst_delete()

    heap_push()
    heap_pop()

    graph_add_edge()
    graph_bfs_dfs()


def main():
    generate_all()
    print("Generated 23 data-structure PNG diagrams in", OUT_DIR)


if __name__ == "__main__":
    main()
