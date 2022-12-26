from rich import box
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.console import Console

from rich.traceback import install
install(show_locals = True)

from datetime import datetime

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
layout["Right"].split(Layout(name="box3", ratio=5), Layout(name = "box4", ratio=3))

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]💼 Pysteward 💼[/]",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="green on black")
    
class Footer:
    """Display footer with info."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "<Company Name>",
            "[b]💼 Pysteward 💼[/]",
            "By Rao (@CodingAssassins)",
        )
        return Panel(grid, style="green on black")

def box1():
    Employee_tbl = Table(title = 'Empolyee Chart')
        
    Employee_tbl.add_column("Name", justify="centre", style="grey62")
    Employee_tbl.add_column("Department", justify="centre", style="grey74")
    Employee_tbl.add_column("Salary", justify="centre", style="grey35")
    Employee_tbl.add_column("Role", justify="centre", style="grey46")
    
    Employee_tbl.add_row("Robert", "CEO", "👍🏼", "CEO")
    Employee_tbl.add_row("Williams", "Accounts", "$144k/month", "Head Accountant")
    Employee_tbl.add_row("James", "Accounts", "$110/month", "Accountant")
    Employee_tbl.add_row("Rao", "Software Engineering", "$100k/month", "Main API Designer")
    Employee_tbl.add_row("Naveed", "Advertising", "$199k/month", "Main UI Designer")
    Employee_tbl.add_row("Bilal", "Advertising", "$170k/month", "Main UX Designer")
    Employee_tbl.add_row("Ahmed", "Production", "$156k/month", "Intern JR")
    Employee_tbl.add_row("Haris", "Production", "$250k/month", "Senior Dev - All in one !")
    Employee_tbl.add_row("Stewie", "Office Manag.", "$10k/month", "Head Events/Organiser")
    Employee_tbl.add_row("Harvy", "Office Manag.", "$5k/month", "Care Taker/Security Head")
    Employee_tbl.add_row("Spector", "Customer Services", "$4.5k/month", "Customer Services")
    Employee_tbl.add_row("Hailey", "Customer Services", "$4k/month", "Customer Services")
    Employee_tbl.add_row("David", "Driver", "$2k/month", "Employee Bus driver")
    
    return Employee_tbl

def box2():
    Tasks = Table(title = 'Task Tracker', show_lines=True)
    
    Tasks.add_column("Employee", justify="centre", style="grey62")
    Tasks.add_column("Task", justify="centre", style="grey74")
    Tasks.add_column("Department", justify="centre", style="grey35")
    Tasks.add_column("Status", justify="centre", style="grey46")
    
    Tasks.add_row("Robert", "Take care of stocks and market value", "CEO/Accounts", "✅")
    Tasks.add_row("Williams", "Meeting with CEO and investors", "Accounts", "✅")
    Tasks.add_row("Haris", "Review API and final production", "Software Engeering", "❌")
    Tasks.add_row("Hailey", "Respond to emails and requests", "Customer Services", "✅")
    Tasks.add_row("Stewie", "Arrange meeting room for Accountant and CEO", "Office Manag.", "✅")
    
    return Tasks
        
def box3():
    Time_tracker = Table(title = "Time Tracker", show_lines=True)
    
    Time_tracker.add_column("Employee", justify="centre", style="grey62")
    Time_tracker.add_column("Department", justify="centre", style="grey35")
    Time_tracker.add_column("Required", justify="centre", style="grey74")
    Time_tracker.add_column("Attendence", justify="centre", style="grey35")
    Time_tracker.add_column("Clocked In", justify="centre", style="grey46")
    
    Time_tracker.add_row("James", "Accounts", "8 hrs", "---", ".--.--")
    Time_tracker.add_row("Williams", "Accounts", "9 hrs", "---", ".--.--")
    Time_tracker.add_row("Ahmed", "Production", "5 hrs", "---", ".--.--")
    Time_tracker.add_row("Hailey", "Customer Services", "8 hrs", "---", ".--.--")
    Time_tracker.add_row("David", "Driver", "3 hrs", "---")
    Time_tracker.add_row("Haris", "Software Engineering", "9 hrs", "---", ".--.--")
    
    return Time_tracker



layout["Header"].size = 3
layout["Footer"].size = 3

layout["box1"].update(box1())
layout["box2"].update(box2())
layout["box3"].update(box3())
layout["Footer"].update(Footer())

from rich.live import Live
import keyboard

with Live(layout, refresh_per_second=10, screen=True):
    while True:
        layout["Header"].update(Header())
        
        if keyboard.is_pressed("q"):
            exit()

print(layout)
