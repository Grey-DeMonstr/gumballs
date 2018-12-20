from builtins import range
import random


def initialize():
    random.seed()


def generate(generator, length):
    gene = []
    for i in range(length):
        gene += [generator(gene)]
    return gene
    # return [generator() for i in range(length)]


def mutated(generator, sequence, count=1):
    gene = sequence[:]
    for i in range(count):
        index = random.randrange(len(gene))
        gene[index] = generator(gene)
    return gene


def merged(seq1, seq2, point=-1):
    assert(len(seq1) == len(seq2))
    index = point if point >= 0 else random.randrange(len(seq1))
    assert(index < len(seq1))
    return seq1[:index] + seq2[index:]


def create_population(generator, gene_length, population_size):
    return [generate(generator, gene_length) for i in range(population_size)]


def repopulate(population, generator, gene_length, population_size):
    return population + create_population(
        generator, gene_length, population_size - len(population))


def natural_selection(population, comparator, limit):
    return sorted(population, key=comparator)[:limit]


def mutate_population(population, generator, mutated_population_count, mutate_factor):
    return population + [mutated(
        generator, random.choice(population), mutate_factor) for n in range(
            mutated_population_count)]


def breed_population(population, breed_population_count):
    return population + [merged(
        random.choice(population), random.choice(population)) for n in range(
            breed_population_count)]


def run_evolution(
    generator,
    comparator,
    gene_length,
    population_size,
    natural_selection_limit,
    breed_population_count,
    mutated_population_count,
    mutate_factor,
    evolution_steps
):
    population = create_population(generator, gene_length, population_size)
    for i in range(evolution_steps):
        population = natural_selection(population, comparator, natural_selection_limit)
        population = breed_population(population, breed_population_count)
        population = mutate_population(
            population, generator, mutated_population_count, mutate_factor)
        population = repopulate(population, generator, gene_length, population_size)
        if i > 0 and i % 100 == 0:
            print("{} steps done".format(i))
    return sorted(population, key=comparator)
