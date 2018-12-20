#!/usr/bin/env python

from operator import attrgetter
import random

import genetics
from airship import *

airship_limit = 15
minimum_required_speed = 400

# Necro_knight Fire: 1188, Armor: 1266, Speed: 1227, Luck: 1018


def total(gene, key):
    f = attrgetter(key)
    return sum([f(x) for x in gene])


def totals(gene):
    return (
        total(gene, Airship.ARMOR),
        total(gene, Airship.FIRE),
        total(gene, Airship.LUCK),
        total(gene, Airship.SPEED)
    )


def negative(t):
    return tuple(-x for x in t)


def speed_is_enough(gene):
    return total(gene, Airship.SPEED) >= minimum_required_speed


def other(selected):
    return list(frozenset(airships) - frozenset(selected))


genetics.initialize()

population_size = 1000  # 200
natural_selection_limit = 800  # 80
mutated_population_count = 400  # 40
mutate_factor = 4
breed_population_count = 0
gene_length = airship_limit
evolution_steps = 1000


def generator(gene):
    return random.choice(other(gene))


def comparator(gene):
    speed_flag = -1 if speed_is_enough(gene) else 1
    return (speed_flag, negative(totals(gene)))


population = genetics.run_evolution(
    generator=generator,
    comparator=comparator,
    gene_length=gene_length,
    population_size=population_size,
    natural_selection_limit=natural_selection_limit,
    breed_population_count=breed_population_count,
    mutated_population_count=mutated_population_count,
    mutate_factor=mutate_factor,
    evolution_steps=evolution_steps)

print(population[0])
print(totals(population[0]))
print("--------")
for gene in population[:10]:
    print(totals(gene))
