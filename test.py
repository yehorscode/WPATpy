import time
from rich.live import Live
from rich.console import Console

console = Console()

with Live(console=console, refresh_per_second=10) as live:
    live.update("[grey]Processing...[/grey]")
    time.sleep(1)
    live.update("[green]Done![/green]")