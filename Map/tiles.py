def load_tiles(self, filename):
    tiles = []
    map_data = self.read_csv(filename)

    tile_dict = {
        '0': 'top_left.png',
        '1': 'top.png',
        '2': 'top_right.png',

        '11': 'left.png',
        '12': 'center.png',
        '13': 'right.png',

        '22': 'bottom_left.png',
        '23': 'bottom.png',
        '24': 'bottom_right.png'
    }

    y = 0

    for row in map_data:
        x = 0

        for tile in row:

            if tile == '-1':
                x += 1
                continue

            if tile in tile_dict:
                tiles.append(
                    Tile(
                        tile_dict[tile],
                        x * self.tile_size,
                        y * self.tile_size,
                        self.spritesheet
                    )
                )

            x += 1

        y += 1

    self.map_w = len(map_data[0]) * self.tile_size
    self.map_h = len(map_data) * self.tile_size

    return tiles