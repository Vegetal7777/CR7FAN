PRINCESS_WIDTH = 28
PRINCESS_HEIGHT = 10
LEFT_PRINCESS_X = 75
RIGHT_PRINCESS_X = 267
ENEMY_PRINCESS_Y = 92
ALLY_PRINCESS_Y = 399

KING_LEVEL_X = 148
KING_LEVEL_WIDTH = 14
KING_LEVEL_HEIGHT = 10

KING_HP_X = 188
KING_HP_WIDTH = PRINCESS_WIDTH
KING_HP_HEIGHT = PRINCESS_HEIGHT

CARD_SIZE = 15
CARD_Y = 603
CARD_INIT_X = 106
CARD_DELTA_X = 69

CROWN_SIZE = 20
CROWN_X = 339

OCR_CONFIG = [
    ['left_enemy_princess', (LEFT_PRINCESS_X, ENEMY_PRINCESS_Y, LEFT_PRINCESS_X + PRINCESS_WIDTH, ENEMY_PRINCESS_Y + PRINCESS_HEIGHT), 170],
    ['right_enemy_princess', (RIGHT_PRINCESS_X, ENEMY_PRINCESS_Y, RIGHT_PRINCESS_X + PRINCESS_WIDTH, ENEMY_PRINCESS_Y + PRINCESS_HEIGHT), 170],
    ['left_ally_princess', (LEFT_PRINCESS_X, ALLY_PRINCESS_Y, LEFT_PRINCESS_X + PRINCESS_WIDTH, ALLY_PRINCESS_Y + PRINCESS_HEIGHT), 170],
    ['right_ally_princess', (RIGHT_PRINCESS_X, ALLY_PRINCESS_Y, RIGHT_PRINCESS_X + PRINCESS_WIDTH, ALLY_PRINCESS_Y + PRINCESS_HEIGHT), 170],
    ['enemy_level', (KING_LEVEL_X, 18, KING_LEVEL_X + KING_LEVEL_WIDTH, 18 + KING_LEVEL_HEIGHT), 180],
    ['ally_level', (KING_LEVEL_X, 486, KING_LEVEL_X + KING_LEVEL_WIDTH, 486 + KING_LEVEL_HEIGHT), 180],
    ['first_card', (CARD_INIT_X, CARD_Y, CARD_INIT_X + CARD_SIZE, CARD_Y + CARD_SIZE), 200],
    ['second_card', (CARD_INIT_X + CARD_DELTA_X, CARD_Y, CARD_INIT_X + CARD_DELTA_X + CARD_SIZE, CARD_Y + CARD_SIZE), 200],
    ['third_card', (CARD_INIT_X + 2 * CARD_DELTA_X, CARD_Y, CARD_INIT_X + 2 * CARD_DELTA_X + CARD_SIZE, CARD_Y + CARD_SIZE), 200],
    ['fourth_card', (CARD_INIT_X + 3 * CARD_DELTA_X, CARD_Y, CARD_INIT_X + 3 * CARD_DELTA_X + CARD_SIZE, CARD_Y + CARD_SIZE), 200],
    ['elixir', (96, 621, 123, 638), 190],
    ['timer', (311, 16, 362, 34), 180],
    ['ally_crowns', (CROWN_X, 332, CROWN_X + CROWN_SIZE, 332 + CROWN_SIZE), 100],
    ['enemy_crowns', (CROWN_X, 200, CROWN_X + CROWN_SIZE, 200 + CROWN_SIZE), 100],
    ['ally_hp', (KING_HP_X, 493, KING_HP_X + KING_HP_WIDTH, 493 + KING_HP_HEIGHT), 180],
    ['enemy_hp', (KING_HP_X, 14, KING_HP_X + KING_HP_WIDTH, 14 + KING_HP_HEIGHT), 195],
]

KING_HP = [2400, 2568, 2736, 2904, 3096, 3312, 3528, 3768, 4008, 4392, 4824, 5304, 5832]
PRINCESS_HP = [1400, 1512, 1624, 1750, 1890, 2030, 2184, 2352, 2534, 2786, 3052, 3346, 3668]