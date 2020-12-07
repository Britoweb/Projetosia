import string
import random

LETTERS = string.ascii_letters + ' ' + '!' + '?'

class GeneticHelloWorld(object):
  def __init__(self, 
               target = "Ola Mundo!",
               num_samples = 1000,
               num_selected = 100,  
               mutation_factor = 10):
    self.target = target
    self.num_samples = num_samples  
    self.num_selected = num_selected  
    self.mutation_factor = mutation_factor  


  def generate_random_chromosomes(self,):
    chromos = []
    while len(chromos) < self.num_samples:
      new_chromo = ''
      while len(new_chromo) < len(self.target):
        new_chromo += random.choice(LETTERS)
      chromos.append(new_chromo)
    return chromos


  def fitness(self, chromo):
    total_fitness = 0
    for i, char in enumerate(chromo):
      total_fitness += abs(ord(char) - ord(self.target[i]))
    return total_fitness


  def tourny_select_chromo(self, samples):
    a = random.choice(samples)
    b = random.choice(samples)
    if self.fitness(a) < self.fitness(b):
      return a
    else:
      return b


  def breed(self, a, b):
    splice_pos = random.randrange(len(a))
    new_a = a[:splice_pos] + b[splice_pos:]
    new_b = b[:splice_pos] + a[splice_pos:]
    return new_a, new_b


  def mutate(self, chromo):
    pos = random.randrange(len(chromo))
    return random.choice(LETTERS).join( [chromo[:pos], chromo[pos+1:]] )


  def run(self):
    sample = self.generate_random_chromosomes()
    generation = -1
    while self.fitness(sample[0]) != 0:
      generation += 1
      ten_percent = int(len(sample)*.01)
      selected = sample[:ten_percent]
      while len(selected) < self.num_selected:
        selected.append(self.tourny_select_chromo(sample))

      solution = []
      while len(solution) < self.num_samples:
        solution.extend(self.breed(random.choice(selected),
                                   random.choice(selected)))

      for i, chromo in enumerate(solution[::self.mutation_factor]):
        solution[i] = self.mutate(solution[i])

      sample = sorted(solution, key = self.fitness)
      (min, median, max) = map(self.fitness,
                               [sample[0], sample[len(sample)//2], sample[-1]])
      print("{0} best string: {1}. fitness: best {2}, median {3}, worst {4}" \
              .format(generation, sample[0], min, median, max))

    return generation

  
ghw = GeneticHelloWorld()
print("Took {0} generations".format(ghw.run()))