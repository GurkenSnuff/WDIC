

class grid_util:


    def find_grid_coords(self, x, y, w, grid_width, grid_scroll, adj_y, adj_x):
        
        found = False
        grid_x = 0
        grid_y = 0
        y_max = round(w / grid_width) + adj_y
        y_min = adj_y
        while not found:
            x_max = round(w / grid_width) + adj_x
            x_min = adj_x
            for space in range(grid_width):
                if x_max >= x >= x_min and y_max >= y >= y_min:
                    return grid_x, grid_y + grid_scroll
                else:
                    x_min += round(w / grid_width)
                    x_max += round(w / grid_width)
                    grid_x += 1
            grid_x = 0
            y_max += round(w / grid_width)
            y_min += round(w / grid_width)
            grid_y += 1

    def grid_to_pixel_coords(self, x, y, w, grid_width, grid_height, grid_scroll, adj_y, adj_x):
        c = round(w / grid_width)

        if(isinstance(y, int)):
            if grid_scroll > y or y - grid_scroll > 11:
                return None
            return (x * c + adj_x, y * c + (c/2) + adj_y - grid_scroll * c)
        else:
            if grid_scroll > y[1] or y[1] - grid_scroll > 11:
                return None
            return (x[0] * c + adj_x, y[1] * c + (c/2) + adj_y - grid_scroll * c)
        