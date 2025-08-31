import pygame
import random
import sys

# --- 全局设置 ---
CELL_SIZE = 20   # 单元格大小
MAZE_WIDTH = 25  # 迷宫宽度（格子数）
MAZE_HEIGHT = 25 # 迷宫高度（格子数）
SCREEN_WIDTH = MAZE_WIDTH * CELL_SIZE
SCREEN_HEIGHT = MAZE_HEIGHT * CELL_SIZE


# ---------------- 迷宫生成类 ----------------
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]  # 1=墙, 0=路
        self.start = (width // 2, height // 2)  # 起点：中心
        self.exit = None
        self._generate_maze()

    def _generate_maze(self):
        """DFS生成迷宫"""
        stack = []
        x, y = self.start
        self.grid[y][x] = 0
        stack.append((x, y))
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

        while stack:
            cx, cy = stack[-1]
            random.shuffle(directions)
            carved = False
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1:
                    if self.grid[ny][nx] == 1:
                        self.grid[ny][nx] = 0
                        self.grid[cy + dy // 2][cx + dx // 2] = 0
                        stack.append((nx, ny))
                        carved = True
                        break
            if not carved:
                stack.pop()

        # 随机出口：从边缘通路里选
        exits = []
        for i in range(self.width):
            if self.grid[0][i] == 0:
                exits.append((i, 0))
            if self.grid[self.height - 1][i] == 0:
                exits.append((i, self.height - 1))
        for j in range(self.height):
            if self.grid[j][0] == 0:
                exits.append((0, j))
            if self.grid[j][self.width - 1] == 0:
                exits.append((self.width - 1, j))
        self.exit = random.choice(exits)


# ---------------- 玩家类 ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()
        # 加载玩家图片
        self.image = pygame.image.load("hugging_face.png")
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_pos[0] * CELL_SIZE, start_pos[1] * CELL_SIZE)

    def move(self, dx, dy, maze):
        nx = self.rect.x // CELL_SIZE + dx
        ny = self.rect.y // CELL_SIZE + dy
        if 0 <= nx < maze.width and 0 <= ny < maze.height:
            if maze.grid[ny][nx] == 0:  # 路才能走
                self.rect.topleft = (nx * CELL_SIZE, ny * CELL_SIZE)


# ---------------- 出口类 ----------------
class Exit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill((0, 255, 0))  # 绿色
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE)


# ---------------- 游戏类 ----------------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("迷宫游戏 - Hugging Face")
        self.clock = pygame.time.Clock()

        # 初始化迷宫
        self.maze = Maze(MAZE_WIDTH, MAZE_HEIGHT)
        self.player = Player(self.maze.start)
        self.exit = Exit(self.maze.exit)

        # 管理 sprite
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.exit)

    def draw_maze(self):
        self.screen.fill((0, 0, 0))  # 黑色背景
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.maze.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move(0, -1, self.maze)
                    elif event.key == pygame.K_DOWN:
                        self.player.move(0, 1, self.maze)
                    elif event.key == pygame.K_LEFT:
                        self.player.move(-1, 0, self.maze)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(1, 0, self.maze)

            self.draw_maze()
            self.all_sprites.draw(self.screen)

            # 检测是否到达出口
            if pygame.sprite.collide_rect(self.player, self.exit):
                print("恭喜通关！")
                running = False

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
