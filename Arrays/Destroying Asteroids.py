# 2126. Destroying Asteroids

class Solution:
    def asteroidsDestroyed(self, mass, asteroids):

        asteroids.sort()

        planet = mass

        for asteroid in asteroids:

            if planet < asteroid:
                return False

            planet += asteroid

        return True