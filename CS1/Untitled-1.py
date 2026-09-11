
import pygame
import sys
import math
import random

pygame.init()
WIDTH, HEIGHT = 1200, 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fortnite-like prototype (pygame)")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("consolas", 18)

# Colors
WHITE = (245, 245, 245)
BLACK = (18, 18, 20)
GREEN = (50, 205, 50)
RED = (220, 60, 60)
BLUE = (80, 150, 255)
WOOD = (183, 138, 75)
GRAY = (120, 120, 120)

# Game constants
GRAVITY = 0.9
GROUND_Y = HEIGHT - 90
PLAYER_W, PLAYER_H = 36, 54
BULLET_SPEED = 18
MAX_MATERIALS = 100

# Utility
def clamp(v, a, b): return max(a, min(b, v))

# Classes
class Wall:
    def __init__(self, x, y, w=80, h=80):
        # x,y are top-left
        self.rect = pygame.Rect(x, y, w, h)
        self.health = 100

    def draw(self, surf):
        pygame.draw.rect(surf, WOOD, self.rect)
        # health bar
        pygame.draw.rect(surf, BLACK, (self.rect.x, self.rect.y - 8, self.rect.w, 6))
        pygame.draw.rect(surf, GREEN, (self.rect.x, self.rect.y - 8, self.rect.w * (self.health / 100), 6))

class Bullet:
    def __init__(self, x, y, vx, vy, owner):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(vx, vy)
        self.radius = 5
        self.owner = owner
        self.life = 160  # frames

    def update(self):
        self.pos += self.vel
        self.life -= 1

    def draw(self, surf):
        pygame.draw.circle(surf, RED, (int(self.pos.x), int(self.pos.y)), self.radius)

    def get_rect(self):
        return pygame.Rect(int(self.pos.x - self.radius), int(self.pos.y - self.radius), self.radius*2, self.radius*2)

class Player:
    def __init__(self, x, y, color=BLUE, name="Player"):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False
        self.color = color
        self.name = name
        self.rect = pygame.Rect(x, y, PLAYER_W, PLAYER_H)
        self.health = 100
        self.materials = 60
        self.ammo = 30
        self.max_hp = 100
        self.respawn_timer = 0

    def update_rect(self):
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))

    def draw(self, surf, mouse_pos):
        # body
        self.update_rect()
        pygame.draw.rect(surf, self.color, self.rect, border_radius=6)
        # head (simple)
        head_rect = pygame.Rect(self.rect.centerx - 10, self.rect.y - 18, 20, 18)
        pygame.draw.ellipse(surf, (230, 200, 180), head_rect)
        # aim line
        aim_vec = pygame.Vector2(mouse_pos) - pygame.Vector2(self.rect.center)
        if aim_vec.length_squared() > 0:
            aim_vec.scale_to_length(40)
            pygame.draw.line(surf, BLACK, self.rect.center, (self.rect.centerx + aim_vec.x, self.rect.centery + aim_vec.y), 2)
        # health bar
        pygame.draw.rect(surf, BLACK, (self.rect.x, self.rect.y - 14, self.rect.w, 8))
        pygame.draw.rect(surf, GREEN, (self.rect.x, self.rect.y - 14, self.rect.w * (self.health / self.max_hp), 8))

    def apply_gravity(self):
        self.vel.y += GRAVITY

    def move_and_collide(self, walls):
        # Horizontal
        self.pos.x += self.vel.x
        self.update_rect()
        for w in walls:
            if self.rect.colliderect(w.rect):
                if self.vel.x > 0:
                    self.pos.x = w.rect.left - self.rect.w
                elif self.vel.x < 0:
                    self.pos.x = w.rect.right
                self.vel.x = 0
                self.update_rect()

        # Vertical
        self.pos.y += self.vel.y
        self.update_rect()
        self.on_ground = False
        for w in walls:
            if self.rect.colliderect(w.rect):
                if self.vel.y > 0:
                    self.pos.y = w.rect.top - self.rect.h
                    self.vel.y = 0
                    self.on_ground = True
                elif self.vel.y < 0:
                    self.pos.y = w.rect.bottom
                    self.vel.y = 0
                self.update_rect()

        # Ground plane
        if self.pos.y + self.rect.h >= GROUND_Y:
            self.pos.y = GROUND_Y - self.rect.h
            self.vel.y = 0
            self.on_ground = True
            self.update_rect()

    def shoot(self, target_pos):
        if self.ammo <= 0:
            return None
        self.ammo -= 1
        dirv = pygame.Vector2(target_pos) - pygame.Vector2(self.rect.center)
        if dirv.length_squared() == 0:
            dirv = pygame.Vector2(1, 0)
        dirv = dirv.normalize()
        vx, vy = dirv.x * BULLET_SPEED, dirv.y * BULLET_SPEED
        b = Bullet(self.rect.centerx + dirv.x * 22, self.rect.centery + dirv.y * 22, vx, vy, self)
        return b

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.respawn()

    def respawn(self):
        self.health = self.max_hp
        # respawn at a random spawn near top-left or top-right
        spawn_x = random.choice([60, WIDTH - 120])
        self.pos = pygame.Vector2(spawn_x, 60)
        self.vel = pygame.Vector2(0, 0)
        self.ammo = 30
        self.materials = 60

# Game world
class Game:
    def __init__(self):
        self.players = []
        self.bullets = []
        self.walls = []
        # create sample walls / cover
        for i in range(6):
            x = 140 + i * 160
            y = GROUND_Y - 120
            self.walls.append(Wall(x, y, 120, 120))
        # players
        self.local = Player(80, 60, color=BLUE, name="You")
        self.players.append(self.local)
        # simple AI opponent
        self.enemy = Player(WIDTH - 140, 60, color=(200, 80, 80), name="Enemy")
        self.players.append(self.enemy)
        self.shoot_cooldown = 0

    def spawn_wall_at(self, x, y, w=80, h=80):
        # Snap to grid for neatness
        gx = int(x // 40) * 40
        gy = int(y // 40) * 40
        # Check overlapping existing walls somewhat
        new_rect = pygame.Rect(gx, gy, w, h)
        for wll in self.walls:
            if new_rect.colliderect(wll.rect):
                return False
        self.walls.append(Wall(gx, gy, w, h))
        return True

    def update(self, dt, keys, mouse_pos, mouse_pressed):
        # local player input
        p = self.local
        if p.health > 0:
            accel = 0.85
            sprint = 1.5 if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else 1.0
            move_dir = 0
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                move_dir -= 1
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                move_dir += 1
            p.vel.x = move_dir * 6 * sprint

            if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and p.on_ground:
                p.vel.y = -18

            # shooting
            if mouse_pressed[0]:
                if self.shoot_cooldown <= 0:
                    b = p.shoot(mouse_pos)
                    if b:
                        self.bullets.append(b)
                        self.shoot_cooldown = 10  # frames
            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= 1

        # build key
        if keys[pygame.K_b]:
            # place wall at mouse if enough materials
            if p.materials >= 15:
                placed = self.spawn_wall_at(mouse_pos[0] - 40, mouse_pos[1] - 40, 80, 80)
                if placed:
                    p.materials -= 15

        # simple enemy AI: move toward player and shoot occasionally
        e = self.enemy
        if e.health > 0:
            # horizontal follow
            if abs(e.pos.x - p.pos.x) > 120:
                e.vel.x = -3 if e.pos.x > p.pos.x else 3
            else:
                e.vel.x = 0
            # jump sometimes if blocked
            if e.on_ground and random.random() < 0.003:
                e.vel.y = -16
            # aim and shoot
            if random.random() < 0.02:
                dirv = pygame.Vector2(p.rect.center) - pygame.Vector2(e.rect.center)
                if dirv.length_squared() > 0:
                    dirv = dirv.normalize()
                    b = Bullet(e.rect.centerx + dirv.x * 22, e.rect.centery + dirv.y * 22, dirv.x * BULLET_SPEED, dirv.y * BULLET_SPEED, e)
                    self.bullets.append(b)

        # apply physics and movement
        for player in self.players:
            player.apply_gravity()
            player.move_and_collide(self.walls)

        # update bullets
        for b in self.bullets[:]:
            b.update()
            # bullet hits walls
            hit = False
            for wll in self.walls:
                if b.get_rect().colliderect(wll.rect):
                    wll.health -= 22
                    if wll.health <= 0:
                        try:
                            self.walls.remove(wll)
                        except ValueError:
                            pass
                    try:
                        self.bullets.remove(b)
                    except ValueError:
                        pass
                    hit = True
                    break
            if hit: continue
            # bullet hits players
            for pl in self.players:
                if pl is not b.owner and b.get_rect().colliderect(pl.rect):
                    pl.take_damage(18)
                    # give owner some materials for hits
                    b.owner.materials = clamp(b.owner.materials + 3, 0, MAX_MATERIALS)
                    if b in self.bullets:
                        self.bullets.remove(b)
                    break
            # remove if life expired or off-screen
            if b.life <= 0 or not ( -50 < b.pos.x < WIDTH+50 and -50 < b.pos.y < HEIGHT+50):
                if b in self.bullets:
                    self.bullets.remove(b)

        # small world wrap for enemy (optional)
        for pl in self.players:
            pl.pos.x = clamp(pl.pos.x, 0, WIDTH - pl.rect.w)

    def draw(self, surf, mouse_pos):
        surf.fill((135, 206, 235))  # sky
        # ground
        pygame.draw.rect(surf, (50, 150, 60), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
        pygame.draw.rect(surf, (100, 100, 100), (0, GROUND_Y + 40, WIDTH, HEIGHT - (GROUND_Y + 40)))  # road/dirt stripe

        # draw walls
        for w in self.walls:
            w.draw(surf)

        # draw bullets
        for b in self.bullets:
            b.draw(surf)

        # draw players
        for pl in self.players:
            pl.draw(surf, mouse_pos)

        # HUD for local player
        p = self.local
        # health, ammo, materials
        hud_x, hud_y = 12, 12
        draw_text(surf, f"HP: {p.health}/{p.max_hp}", hud_x, hud_y)
        draw_text(surf, f"Ammo: {p.ammo}", hud_x, hud_y + 22)
        draw_text(surf, f"Materials: {p.materials}", hud_x, hud_y + 44)
        draw_text(surf, "Controls: WASD/Arrow keys move, Space jump, LShift sprint", hud_x, HEIGHT - 28)
        draw_text(surf, "Left click shoot | B build wall (15 materials) | R reload (auto) ", hud_x, HEIGHT - 46)

def draw_text(surf, txt, x, y, color=BLACK):
    surf.blit(FONT.render(txt, True, color), (x, y))

def main():
    game = Game()
    running = True
    mouse_held = False
    reload_ticks = 0

    while running:
        dt = clock.tick(FPS) / 1000.0
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_r:
                    # reload (simple instant-ish)
                    game.local.ammo = 30
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_held = True
            if ev.type == pygame.MOUSEBUTTONUP:
                mouse_held = False

        # update world
        game.update(dt, keys, mouse_pos, mouse_pressed)

        # simple regen materials over time
        if random.random() < 0.02:
            game.local.materials = clamp(game.local.materials + 1, 0, MAX_MATERIALS)

        # draw
        game.draw(screen, mouse_pos)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()