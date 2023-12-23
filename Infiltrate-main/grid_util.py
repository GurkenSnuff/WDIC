

class grid_util:

    def __init__(self, grid_width, grid_scroll, adj_y, adj_x, grid_w):
        self.grid_width = grid_width
        self.grid_scroll = grid_scroll
        self.adj_x = adj_x
        self.adj_y = adj_y
        self.grid_w = grid_w

    def find_grid_coords(self, x, y, w):
        print(self.grid_scroll)
        found = False
        grid_x = 0
        grid_y = 0
        y_max = round(w / self.grid_width) + self.adj_y
        y_min = self.adj_y
        while not found:
            x_max = round(w / self.grid_width) + self.adj_x
            x_min = self.adj_x
            for space in range(self.grid_width):
                if x_max >= x >= x_min and y_max >= y >= y_min:
                    return grid_x, grid_y + self.grid_scroll
                else:
                    x_min += round(w / self.grid_width)
                    x_max += round(w / self.grid_width)
                    grid_x += 1
            grid_x = 0
            y_max += round(w / self.grid_width)
            y_min += round(w / self.grid_width)
            grid_y += 1