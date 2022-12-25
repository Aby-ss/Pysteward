from rich import box
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.console import Console

from rich.traceback import install
install(show_locals = True)

layout = Layout()
console = Console()

layout.split_column(
    Layout(name = "Header"),
    Layout(name = "Body"),
    Layout(name = "Footer")
    )

layout["Body"].split_row(
    Layout(name = "Right"), Layout(name = "Left")
    )
layout["Left"].split(Layout(name = "box1"), Layout(name = "box2"))

layout["Header"].size = 3
layout["Footer"].size = 3

print(layout)
