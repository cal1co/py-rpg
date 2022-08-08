import pygame
from settings import * 

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE) 

        hl = ht = 10
        self.health_bar_rect = pygame.Rect(hl, ht, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        el, et = 10, 34
        self.energy_bar_rect = pygame.Rect(el, et, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha() 
            self.weapon_graphics.append(weapon)
    # init()

    def show_bar(self, current, max, bg_rect, colour):
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, bg_rect)
        
        ratio = current / max
        current_width = bg_rect.width * ratio 
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        pygame.draw.rect(self.display_surface, colour, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, bg_rect, 3)
    # show_bar()

    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOUR)
        x, y = self.display_surface.get_size()[0], self.display_surface.get_size()[1]
        off = 20
        text_rect = text_surf.get_rect(bottomright=(x - off, y - off)) 

        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, text_rect.inflate(20, 20), 3)
    # show_exp()

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOUR, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOUR, bg_rect, 3)
        return bg_rect
    # selection_box()

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 630, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surf, weapon_rect)
    # weapon_overlay()

    def display(self, player): 
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOUR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOUR)

        self.show_exp(player.exp)

        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        # self.selection_box(80, 635)
    # display() 
