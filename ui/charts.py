class Charts:
    def __init__(self):
        # Store history for trend charts
        self.cpu_history = []
        self.memory_history = []
        self.disk_history = []

        self.max_points = 20  # width of chart

    # UPDATE HISTORY
  
    def update(self, stats):
        self.cpu_history.append(stats["cpu"])
        self.memory_history.append(stats["memory"])
        self.disk_history.append(stats["disk"])

        # Keep fixed length
        if len(self.cpu_history) > self.max_points:
            self.cpu_history.pop(0)
            self.memory_history.pop(0)
            self.disk_history.pop(0)

    # BAR CHART
  
    def bar(self, value, length=20):
        filled = int((value / 100) * length)
        return "█" * filled + "░" * (length - filled)

    # MINI LINE CHART
  
    def line_chart(self, data):
        chart = ""

        for value in data:
            if value > 80:
                chart += "█"
            elif value > 50:
                chart += "▓"
            elif value > 20:
                chart += "▒"
            else:
                chart += "░"

        return chart

    # DISPLAY ALL CHARTS
  
    def display(self, stats):
        self.update(stats)

        print("\n📊 SYSTEM CHARTS\n")

        # Bar charts
        print(f"CPU:    {self.bar(stats['cpu'])} {stats['cpu']}%")
        print(f"Memory: {self.bar(stats['memory'])} {stats['memory']}%")
        print(f"Disk:   {self.bar(stats['disk'])} {stats['disk']}%")

        # Trend charts
        print("\n📈 TRENDS\n")
        print(f"CPU:    {self.line_chart(self.cpu_history)}")
        print(f"Memory: {self.line_chart(self.memory_history)}")
        print(f"Disk:   {self.line_chart(self.disk_history)}")
