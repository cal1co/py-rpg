from turtle import up
import pygame 
from settings import *

class Upgrade:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player 
        self.attribute_nr = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        self.selection_index = 0
        self.selection_time = None
        self.can_move = True
    # __init__()

    def input(self):
        keys = pygame.key.get_pressed()
        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_nr - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks() 
            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks() 

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.item_list[self.selection_index].trigger(self.player)

    # input()

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks() 
            if current_time - self.selection_time >= 300: 
                self.can_move = True
    # selection_cooldown()

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.attribute_nr)):

            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_nr 
            left = (item * increment) + (increment - self.width) // 2
            top = self.display_surface.get_size()[1] * 0.1

            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)
    # create_items()

    def display(self):
        self.input()
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface, self.selection_index, name, value, max_value, cost)
    # display()

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font
    # __init__

    def display_names(self, surface, name, cost, selected):
        colour = TEXT_COLOUR_SELECTED if selected else TEXT_COLOUR

        title_surf = self.font.render(name, False, colour)
        title_rect = title_surf.get_rect(midtop=self.rect.midtop+pygame.math.Vector2(0, 20))

        cost_surf = self.font.render(f'{int(cost)}', False, colour)
        cost_rect = cost_surf.get_rect(midbottom=self.rect.midbottom - pygame.math.Vector2(0, 20))

        surface.blit(title_surf, title_rect)
        surface.blit(cost_surf, cost_rect)
    # display_names()

    def display_bar(self, surface, value, max_value, selected):
        top = self.rect.midtop + pygame.math.Vector2(0, 60)
        bottom = self.rect.midbottom - pygame.math.Vector2(0, 60)
        colour = BAR_COLOUR_SELECTED if selected else BAR_COLOUR

        full_height = bottom[1] - top[1]
        relative_number = (value / max_value) * full_height 
        value_rect = pygame.Rect(top[0] - 15, bottom[1] - relative_number, 30, 10)

        pygame.draw.line(surface, colour, top, bottom, 5)
        pygame.draw.rect(surface, colour, value_rect)
    # display_bar()

    def trigger(self, player):
        upgrade_attribute = list(player.stats.keys())[self.index]
        if player.exp >= player.upgrade_cost[upgrade_attribute] and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:
            player.exp -= player.upgrade_cost[upgrade_attribute]
            player.stats[upgrade_attribute] *= 1.2
            player.upgrade_cost[upgrade_attribute] *= 1.4
        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]
    # trigger()

    def display(self, surface, selection_num, name, value, max_value, cost):
        if self.index == selection_num: 
            pygame.draw.rect(surface, UPGRADE_BG_COLOUR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOUR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOUR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOUR, self.rect, 4)
        self.display_names(surface, name, cost, self.index == selection_num)
        self.display_bar(surface, value, max_value, self.index == selection_num)
    # display()


# Item()