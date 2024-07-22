class Hero:
    def __init__(self, name: str, life: int, rank: float):
        if type(name) == str:
            self.name=name
        else:
            raise ValueError("invalid name")
        if type(life) == int:
            self.life=life
        else:
            raise ValueError("invalid life")
        if type(rank) == float:
            self.rank=rank
        else:
            raise ValueError("invalid rank")

hero1 = Hero("Bobur", 100, 5.3)


print(f"Name: {hero1.name}")
print(f"Life: {hero1.life}")
print(f"Rank: {hero1.rank}")
