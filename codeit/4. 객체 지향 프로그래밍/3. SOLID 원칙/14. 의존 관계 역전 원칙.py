from abc import ABC, abstractclassmethod


class IWeapon(ABC):
    """무기 클래스"""

    @abstractclassmethod
    def use_on(self, other_character):
        pass


class Sword(IWeapon):
    """검 클래스"""

    def __init__(self, damage):
        self.damage = damage

    def use_on(self, other_character):
        """검 사용 메소드"""
        other_character.get_damage(self.damage)


class Gun(IWeapon):
    """총 클래스"""

    def __init__(self, damage, num_rounds):
        self.damage = damage
        self.num_rounds = num_rounds  # 총알 갯수

    def use_on(self, other_character):
        """총 사용 메소드"""
        if self.num_rounds > 0:
            other_character.get_damage(self.damage)
            self.num_rounds -= 1
        else:
            print("총알이 없어 공격할 수 없습니다")


class GameCharacter:
    """게임 캐릭터 클래스"""

    def __init__(self, name, hp, weapon: IWeapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.weapon.use_on(other_character)
        else:
            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_weapon(self, new_weapon):
        """검을 바꾸는 메소드"""
        self.weapon = new_weapon

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 사망했습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        """남은 체력을 문자열로 리턴하는 메소드"""
        return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)


bad_sword = Sword(1)
gun = Gun(100, 10)

game_character_1 = GameCharacter("홍길동", 100, bad_sword)
game_character_2 = GameCharacter("아무개", 1000, gun)

game_character_1.attack(game_character_2)
game_character_1.attack(game_character_2)
game_character_1.attack(game_character_2)

game_character_2.attack(game_character_1)

print(game_character_1)
print(game_character_2)