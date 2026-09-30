import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
out = r"D:\Projects\kazantseva\sprintlab-wiki\docs\assets\charts"
plt.rcParams.update({"font.family": "Segoe UI", "font.size": 11})
months = [f"{m:02d}.{y}" for y in (2024, 2025, 2026) for m in range(1, 13)][:32]
# медиана Lead Time, дни
rel = {2: ("v1.0", 9.6), 9: ("v1.5", 5.4), 16: ("v2.0", 3.1), 25: ("v2.5", 2.2)}
anchors = [(0, 11.2), (2, 9.6), (9, 5.4), (16, 3.1), (25, 2.2), (31, 2.05)]
xs, ys = zip(*anchors)
lt = np.interp(range(32), xs, ys)
rng = np.random.default_rng(5)
lt = np.round(lt + rng.normal(0, 0.25, 32) * np.linspace(1, .4, 32), 1)
for i, (_, v) in rel.items(): lt[i] = v
fig, ax = plt.subplots(figsize=(11, 4.6), dpi=150)
ax.plot(range(32), lt, color="#c96f8a", lw=2.5, marker="o", ms=3.5)
ax.axhline(2, color="#8c7aa8", ls="--", lw=1.5); ax.text(31, 2.15, "цель 2026 – 2 дня", color="#6f5a8f", ha="right", fontsize=10)
for i, (name, v) in rel.items():
    ax.axvline(i, color="#90a4ae", ls=":", lw=1)
    ax.annotate(f"{name}\n{str(v).replace('.', ',')} дн.", (i, v), xytext=(6, 18), textcoords="offset points", fontsize=10, fontweight="bold", color="#7a2e47")
ax.set_xticks(range(0, 32, 3)); ax.set_xticklabels([months[i] for i in range(0, 32, 3)])
ax.set_ylabel("дни (медиана)"); ax.set_ylim(0, 12.5); ax.grid(axis="y", alpha=.3)
ax.set_title("Время выполнения изменений (Lead Time for Changes) и релизы продукта", loc="left", fontweight="bold")
for s in ("top", "right"): ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(out + r"\lead_time.png"); plt.close(fig)

years = ["2024", "2025", "2026*"]
data = [("Частота развёртываний, в неделю", [3, 9, 17], "#d98ba2"),
        ("Доля неудачных изменений, %", [21, 14, 9], "#b5557a"),
        ("Время восстановления (MTTR), ч", [6.5, 3.2, 1.4], "#e3aabb"),
        ("Команд-клиентов на платформе", [18, 46, 83], "#9c5b7a")]
fig, axs = plt.subplots(1, 4, figsize=(13, 3.6), dpi=150)
for ax, (t, v, c) in zip(axs, data):
    b = ax.bar(years, v, color=c, width=.6)
    ax.bar_label(b, labels=[str(x).replace(".", ",") for x in v], padding=2, fontsize=10)
    ax.set_title(t, fontsize=10.5, fontweight="bold"); ax.set_yticks([]); ax.set_ylim(0, max(v) * 1.25)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
fig.text(.99, .01, "* 2026 – январь–август", ha="right", fontsize=9, color="#607d8b")
fig.tight_layout(); fig.savefig(out + r"\metrics.png"); plt.close(fig)
print(list(zip(months, lt)))
