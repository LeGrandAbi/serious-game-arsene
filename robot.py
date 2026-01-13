import pygame as pg
import random
import math

from settings import *


class Robot:
    def __init__(self, data):
        self.data = data

        self.position = pg.math.Vector2(random.uniform(350, 450), random.uniform(350, 450))
        self.velocity = pg.math.Vector2()
        self.acceleration = pg.math.Vector2()
        self.body_animation_timer = 0

        self.life = ROBOT_MAX_LIFE

        self.controlled = False
        self.is_next = False

    def get_image(self):
        texture = pg.Surface((64,64), pg.SRCALPHA)

        texture.blit(self.data.texture_robot_body_walk_cycle[int(self.body_animation_timer)], (0,32))
        self.body_animation_timer += (self.velocity.length())/ROBOT_BODY_ANIMATION_SCALAR
        if self.body_animation_timer >= 4:
            self.body_animation_timer = 0

        if self.controlled:
            screen_texture = self.data.texture_robot_screen_signal.copy()
        elif self.is_next:
            screen_texture = self.data.texture_robot_screen_next.copy()
        else:
            screen_texture = self.data.texture_robot_screen_nosignal.copy()
        if self.life != ROBOT_MAX_LIFE:
            neige_texture = self.data.texture_screen_neige[random.randint(0, len(self.data.texture_screen_neige)-1)].copy()
            neige_texture.set_alpha(int(255-255*self.life/ROBOT_MAX_LIFE))
            screen_texture.blit(neige_texture, (0,0))
        texture.blit(screen_texture, (13,3))

        texture.blit(self.data.texture_robot_head_frame, (0,-13))

        if self.velocity.x < 0:
            texture =  pg.transform.flip(texture, True, False)
        return texture

    def update(self, inputs, robots, controlled_robot):
        if self.controlled:
            self.control(inputs)
            if inputs.keys["secondary"].pressed:
                self.life -= random.randint(0, ROBOT_MAX_DAMAGE)
            else:
                self.life += 1
        else:
            self.behave(inputs, robots, controlled_robot)
            self.life += random.randint(0, ROBOT_MAX_REGEN)

        if self.life > ROBOT_MAX_LIFE:
            self.life = ROBOT_MAX_LIFE

        self.velocity += self.acceleration
        if self.velocity.length() > ROBOT_MAX_SPEED: self.velocity.scale_to_length(ROBOT_MAX_SPEED)
        self.position += self.velocity
        self.acceleration *= 0
        self.restrict()

    def restrict(self):
        if self.position.x < 0: 
            self.position.x = 0
            self.velocity.x *= -ROBOT_BOUNCE
        if self.position.x > TILEMAP_WIDTH * TILE_SIZE: 
            self.position.x = TILEMAP_WIDTH * TILE_SIZE
            self.velocity.x *= -ROBOT_BOUNCE
        if self.position.y < 0: 
            self.position.y = 0
            self.velocity.y *= -ROBOT_BOUNCE
        if self.position.y > TILEMAP_HEIGHT * TILE_SIZE: 
            self.position.y = TILEMAP_HEIGHT * TILE_SIZE
            self.velocity.y *= -ROBOT_BOUNCE

    def control(self, inputs):
        if inputs.keys["left"].pressed: self.velocity.x = -CONTROL_SPEED
        if inputs.keys["right"].pressed: self.velocity.x = CONTROL_SPEED
        if inputs.keys["up"].pressed: self.velocity.y = -CONTROL_SPEED
        if inputs.keys["down"].pressed: self.velocity.y = CONTROL_SPEED
        self.velocity *= 0.8

    def behave(self, inputs, robots, controlled_robot):
        separation = self.separate(robots)
        alignment = self.align(robots)
        cohesion = self.cohere(robots)
        follow = self.follow(inputs, controlled_robot)

        self.acceleration += separation
        self.acceleration += alignment
        self.acceleration += cohesion
        self.acceleration += follow

    def separate(self, robots):
        steer = pg.math.Vector2()
        count = 0
        for other in robots:
            distance = self.position.distance_to(other.position)
            if 0 < distance < ROBOT_SEPARATION_DIST:
                diff = self.position - other.position
                diff /= distance
                steer += diff
                count += 1
        if count > 0:
            steer /= count
        if steer.length() > EPS:
            steer.scale_to_length(ROBOT_MAX_SPEED)
            steer -= self.velocity
            if steer.length() > ROBOT_MAX_FORCE:
                steer.scale_to_length(ROBOT_MAX_FORCE)    
        return steer

    def align(self, robots):
        avg_velocity = pg.math.Vector2()
        count = 0
        for other in robots:
            distance = self.position.distance_to(other.position)
            if 0 < distance < ROBOT_NEIGHBOR_DIST:
                avg_velocity += other.velocity
                count += 1
        if count > 0:
            avg_velocity /= count
            if avg_velocity.length() > EPS:
                avg_velocity.scale_to_length(ROBOT_MAX_SPEED)
            steer = avg_velocity - self.velocity
            if steer.length() > ROBOT_MAX_FORCE:
                steer.scale_to_length(ROBOT_MAX_FORCE)
            return steer
        else:
            return pg.math.Vector2()

    def cohere(self, robots):
        center_mass = pg.math.Vector2()
        count = 0
        for other in robots:
            distance = self.position.distance_to(other.position)
            if 0 < distance < ROBOT_NEIGHBOR_DIST:
                center_mass += other.position
                count += 1
        if count > 0:
            center_mass /= count
            desired = center_mass - self.position
            desired.scale_to_length(ROBOT_MAX_SPEED)
            steer = desired - self.velocity
            if steer.length() > ROBOT_MAX_FORCE:
                steer.scale_to_length(ROBOT_MAX_FORCE)
            return steer
        else:
            return pg.math.Vector2()

    def follow(self, inputs, controlled_robot):
        follow = pg.Vector2()
        if inputs.keys["secondary"].pressed:
            diff = controlled_robot.position - self.position
            dist = diff.length()
            if dist > ROBOT_NOFOLLOW_DIST:
                diff.scale_to_length(ROBOT_FOLLOW_STRENGTH * (1/math.sqrt(dist)))
                follow = diff
            elif self.velocity.length() > EPS:
                self.velocity.scale_to_length(0.9)

        return follow

if __name__ == "__main__":
    import main