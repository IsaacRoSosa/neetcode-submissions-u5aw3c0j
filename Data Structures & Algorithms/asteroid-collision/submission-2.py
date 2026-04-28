class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        def noColission(orbitAsteroid, incomingAsteroid):
            if orbitAsteroid < 0 and incomingAsteroid < 0 or orbitAsteroid > 0 and incomingAsteroid > 0 or orbitAsteroid < 0 and incomingAsteroid >0  :
                return True
            else:
                return False 
        for asteroid in asteroids:
            if res:
                #Si no van en direcciones opuestas solo agregamos el nuevo 
                if noColission(res[-1], asteroid): 
                    res.append(asteroid)
                else:
                    destroyed = False 
                    while res and not destroyed and not noColission(res[-1],asteroid):
                        orbitAsteroid = res.pop()
                        if abs(orbitAsteroid) == abs(asteroid):
                            destroyed = True
                            #Ambos son destruidos no hacer nada
                        elif abs(orbitAsteroid) > abs(asteroid):
                            #el incoming asteroid es destruido, regresar viejo asteroid al array
                            res.append(orbitAsteroid)
                            destroyed = True 
                    if not destroyed:
                        res.append(asteroid)
            else:
                res.append(asteroid)
        return res
        