class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dates = []
        population = max_population = max_year = 0
        
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))
        dates.sort()
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = year
        return max_year