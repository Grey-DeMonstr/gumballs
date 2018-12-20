from enum import Enum
import random
import genetics


population_size = 200
natural_selection_limit = 80
mutated_population_count = 40
mutate_factor = 4
breed_population_count = 40
gene_length = 30
evolution_steps = 200

start_ep = 840
start_hp = 580
start_guard_count = 10
start_king_hp = 1500

king_attack = 24
main_attack = 47
guard_attack = 10
guard_hp = 75
spell_cost = 50
spell_damage = 100

Actions = Enum('Actions', 'attack_guard attack_king spell_guard spell_king spell_all')


class State():
    ep = start_ep
    hp = start_hp
    guard_count = start_guard_count
    has_wounded_guard = False
    king_hp = start_king_hp
    turn = 0

    def apply_action(self, action):
        if self.king_hp <= 0 or self.hp <= 0:
            return

        if action == Actions.attack_guard:
            self.attack_guard()
        elif action == Actions.attack_king:
            self.attack_king()
        elif action == Actions.spell_guard:
            self.spell_guard()
        elif action == Actions.spell_king:
            self.spell_king()
        elif action == Actions.spell_all:
            self.spell_all()

    def process_turn(self):
        if self.king_hp <= 0 or self.hp <= 0:
            return

        self.turn += 1
        if self.turn % 2 == 0:
            self.hp -= guard_attack * self.guard_count

    def attack_guard(self):
        if self.guard_count == 0:
            return
        self.hp -= guard_attack
        if self.has_wounded_guard:
            self.has_wounded_guard = False
            self.guard_count -= 1
        else:
            self.has_wounded_guard = True

    def attack_king(self):
        self.hp -= king_attack
        self.king_hp -= main_attack

    def spell_guard(self):
        if self.guard_count == 0:
            return
        if self.ep < spell_cost:
            return
        self.ep -= spell_cost
        self.guard_count -= 1

    def spell_king(self):
        if self.ep < spell_cost:
            return
        self.ep -= spell_cost
        self.king_hp -= spell_damage

    def spell_all(self):
        if self.ep <= 0:
            return

        enemy_count = 1 + self.guard_count
        damage = (self.ep * 2) / enemy_count
        if damage >= guard_hp:
            self.guard_count = 0
        self.ep = 0
        self.king_hp -= damage

    def score(self):
        base = self.king_hp if self.king_hp > 0 else 0
        return base * 10000 + start_hp - self.hp


def generator(gene):
    return random.choice(list(Actions))


def comparator(gene):
    state = State()
    for action in gene:
        state.apply_action(action)
        state.process_turn()
    return state.score()


def description(gene, verbose=False):
    state = State()
    for action in gene:
        if verbose:
            print action
        state.apply_action(action)
        state.process_turn()
        if verbose:
            print "King hp at turn {0}: {1}, gumball hp: {2}, guards left: {3}".format(
                state.turn, state.king_hp, state.hp, state.guard_count)
    print "King hp: {0}, gumball hp: {1}, score: {2}".format(state.king_hp, state.hp, state.score())


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


for gene in population[:10]:
    print description(gene)

for gene in population[:1]:
    print description(gene, True)
