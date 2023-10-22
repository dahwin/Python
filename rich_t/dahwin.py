from rich import print
from rich.table import Table

# Styling text
text = "Dahwin (dahyun+darwin=dahwin)"
colored_text = "[blue][bold]" + text + "[/bold][/blue]"
print(colored_text)

# Creating a table
table = Table(title="Sample Table", show_header=True)
table.add_column("Name")
table.add_column("Age")

table.add_row("Alice", "30")
table.add_row("Bob", "25")

print(table)
