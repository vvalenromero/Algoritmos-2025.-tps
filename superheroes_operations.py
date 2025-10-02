from list_ import List
from typing import Optional

class SuperheroList(List):
    
    def remove_by_name(self, name: str) -> Optional[dict]:
        for i, hero in enumerate(self):
            if hero.get('name') == name:
                return self.pop(i)
        return None
    
    def get_first_appearance(self, name: str) -> Optional[int]:
        for hero in self:
            if hero.get('name') == name:
                return hero.get('first_appearance')
        return None
    
    def change_house(self, name: str, new_house: str) -> bool:
        for hero in self:
            if hero.get('name') == name:
                hero['house'] = new_house
                return True
        return False
    
    def find_by_bio_words(self, *words) -> List:
        result = List()
        for hero in self:
            bio = hero.get('short_bio', '').lower()
            if any(word.lower() in bio for word in words):
                result.append(hero['name'])
        return result
    
    def filter_by_year(self, year: int, operator: str = '<') -> List:
        result = List()
        for hero in self:
            first_app = hero.get('first_appearance')
            if operator == '<' and first_app and first_app < year:
                result.append({'name': hero['name'], 'house': hero.get('house'), 'year': first_app})
            elif operator == '>' and first_app and first_app > year:
                result.append({'name': hero['name'], 'house': hero.get('house'), 'year': first_app})
        return result
    
    def get_house(self, name: str) -> Optional[str]:
        for hero in self:
            if hero.get('name') == name:
                return hero.get('house')
        return None
    
    def get_hero_info(self, name: str) -> Optional[dict]:
        for hero in self:
            if hero.get('name') == name:
                return hero
        return None
    
    def filter_by_initial(self, *letters) -> List:
        result = List()
        letters_upper = [letter.upper() for letter in letters]
        for hero in self:
            name = hero.get('name', '')
            if name and name[0].upper() in letters_upper:
                result.append(hero['name'])
        return result
    
    def count_by_house(self) -> dict:
        count = {}
        for hero in self:
            house = hero.get('house', 'Unknown')
            count[house] = count.get(house, 0) + 1
        return count
    
    
    def concatenate(self, other_list) -> 'SuperheroList':
        """a. Concatenar dos listas"""
        result = SuperheroList(self)
        result.extend(other_list)
        return result
    
    def concatenate_unique(self, other_list, key: str = None) -> 'SuperheroList':
        result = SuperheroList(self)
        seen = set()
        
        for item in self:
            identifier = item.get(key) if key and isinstance(item, dict) else item
            seen.add(identifier)
        
        for item in other_list:
            identifier = item.get(key) if key and isinstance(item, dict) else item
            if identifier not in seen:
                result.append(item)
                seen.add(identifier)
        
        return result
    
    def count_intersection(self, other_list, key: str = None) -> int:
        count = 0
        for item1 in self:
            id1 = item1.get(key) if key and isinstance(item1, dict) else item1
            for item2 in other_list:
                id2 = item2.get(key) if key and isinstance(item2, dict) else item2
                if id1 == id2:
                    count += 1
                    break
        return count
    
    def delete_all_showing(self) -> None:
        while len(self) > 0:
            element = self.pop(0)
            print(f"Eliminando: {element}")
