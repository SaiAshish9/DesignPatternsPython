from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, gender, marital_status):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status

class Criteria(ABC):
    @abstractmethod
    def meet_criteria(self, persons):
        pass

class CriteriaMale(Criteria):
    def meet_criteria(self, persons):
        return [person for person in persons if person.gender.lower() == "male"]

class CriteriaFemale(Criteria):
    def meet_criteria(self, persons):
        return [person for person in persons if person.gender.lower() == "female"]

class CriteriaSingle(Criteria):
    def meet_criteria(self, persons):
        return [person for person in persons if person.marital_status.lower() == "single"]

class CriteriaMarried(Criteria):
    def meet_criteria(self, persons):
        return [person for person in persons if person.marital_status.lower() == "married"]

class AndCriteria(Criteria):
    def __init__(self, criteria1, criteria2):
        self.criteria1 = criteria1
        self.criteria2 = criteria2

    def meet_criteria(self, persons):
        first_criteria_persons = self.criteria1.meet_criteria(persons)
        return self.criteria2.meet_criteria(first_criteria_persons)

class OrCriteria(Criteria):
    def __init__(self, criteria1, criteria2):
        self.criteria1 = criteria1
        self.criteria2 = criteria2

    def meet_criteria(self, persons):
        criteria1_persons = self.criteria1.meet_criteria(persons)
        criteria2_persons = self.criteria2.meet_criteria(persons)
        return list(set(criteria1_persons + criteria2_persons))

if __name__ == "__main__":
    persons = [
        Person("John", "Male", "Single"),
        Person("Jane", "Female", "Married"),
        Person("Adam", "Male", "Married"),
        Person("Eve", "Female", "Single"),
        Person("Mike", "Male", "Single"),
    ]

    male_criteria = CriteriaMale()
    female_criteria = CriteriaFemale()
    single_criteria = CriteriaSingle()
    married_criteria = CriteriaMarried()

    print("Males:")
    for person in male_criteria.meet_criteria(persons):
        print(person.name)

    print("\nFemales:")
    for person in female_criteria.meet_criteria(persons):
        print(person.name)

    print("\nSingles:")
    for person in single_criteria.meet_criteria(persons):
        print(person.name)

    print("\nMarried:")
    for person in married_criteria.meet_criteria(persons):
        print(person.name)

    print("\nSingle Males:")
    single_male_criteria = AndCriteria(single_criteria, male_criteria)
    for person in single_male_criteria.meet_criteria(persons):
        print(person.name)

    print("\nSingle Or Females:")
    single_or_female_criteria = OrCriteria(single_criteria, female_criteria)
    for person in single_or_female_criteria.meet_criteria(persons):
        print(person.name)
