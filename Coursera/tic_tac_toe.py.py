import pygame
import numpy as np
import time

# 🏆 Task 1: Khởi tạo trò chơi, cấu trúc chính
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Màu sắc
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)

# Tạo cửa sổ game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Lưới bàn cờ
def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

draw_lines()

# Khởi tạo ma trận lưu trạng thái bàn cờ
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# 🏆 Task 2: Nhận input từ người chơi, thay phiên lượt
def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    return not (0 in board)

# 🏆 Task 3: Kiểm tra điều kiện thắng
def check_win(player):
    # Kiểm tra hàng ngang
    for row in range(BOARD_ROWS):
        if np.all(board[row] == player):
            return True

    # Kiểm tra cột dọc
    for col in range(BOARD_COLS):
        if np.all(board[:, col] == player):
            return True

    # Kiểm tra đường chéo
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

# 🏆 Task 4: Vẽ X/O trên màn hình
def draw_XO(row, col, player):
    if player == 1:  # Vẽ X
        pygame.draw.line(screen, X_COLOR, (col * SQUARE_SIZE + 50, row * SQUARE_SIZE + 50),
                         (col * SQUARE_SIZE + SQUARE_SIZE - 50, row * SQUARE_SIZE + SQUARE_SIZE - 50), LINE_WIDTH)
        pygame.draw.line(screen, X_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE - 50, row * SQUARE_SIZE + 50),
                         (col * SQUARE_SIZE + 50, row * SQUARE_SIZE + SQUARE_SIZE - 50), LINE_WIDTH)
    elif player == 2:  # Vẽ O
        pygame.draw.circle(screen, O_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3, LINE_WIDTH)

# 🏆 Task 5: Xử lý sự kiện Pygame
player = 1  # Người chơi đầu tiên là X
game_over = False

# 🏆 Task 6: Animation khi đánh dấu X/O
def draw_animated_XO(row, col, player):
    if player == 1:
        for i in range(10):
            pygame.draw.line(screen, X_COLOR, 
                            (col * SQUARE_SIZE + 50, row * SQUARE_SIZE + 50), 
                            (col * SQUARE_SIZE + 50 + i * 10, row * SQUARE_SIZE + 50 + i * 10), 
                            LINE_WIDTH)
            pygame.draw.line(screen, X_COLOR, 
                            (col * SQUARE_SIZE + SQUARE_SIZE - 50, row * SQUARE_SIZE + 50), 
                            (col * SQUARE_SIZE + SQUARE_SIZE - 50 - i * 10, row * SQUARE_SIZE + 50 + i * 10), 
                            LINE_WIDTH)
            pygame.display.update()
            time.sleep(0.02)

    elif player == 2:
        for i in range(10):
            pygame.draw.circle(screen, O_COLOR, 
                            (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                            5 + i * 5, LINE_WIDTH)
            pygame.display.update()
            time.sleep(0.02)

# 🏆 Vòng lặp chính của game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                draw_animated_XO(clicked_row, clicked_col, player)
                
                if check_win(player):
                    print(f"Player {player} wins!")
                    game_over = True

                player = 2 if player == 1 else 1  # Đổi lượt chơi

        pygame.display.update()

pygame.quit()
