import numpy, skfuzzy
from skfuzzy import control

gorjeta = control.Consequent(numpy.arange(0, 30, 1), 'gorjeta')
servico = control.Antecedent(numpy.arange(0, 30, 1), 'servico')
comida = control.Antecedent(numpy.arange(0, 26, 1), 'comida')

comida.automf(names=['horrivel', 'ok', 'otimo'])

gorjeta['pouca'] = skfuzzy.trapmf(gorjeta.universe, [0, 5, 7, 15])
gorjeta['media'] = skfuzzy.trapmf(gorjeta.universe, [0, 14, 16, 30])
gorjeta['muita'] = skfuzzy.trapmf(gorjeta.universe, [15, 25, 27, 30])

servico['horrivel'] = skfuzzy.trapmf(gorjeta.universe, [0, 5, 7, 15])
servico['ok'] = skfuzzy.trapmf(gorjeta.universe, [0, 14, 16, 30])
servico['otimo'] = skfuzzy.trapmf(gorjeta.universe, [15, 25, 27, 30])

gorjeta.view()
servico.view()
comida.view()

regra1 = control.Rule(servico['otimo'] | comida['otimo'], gorjeta['muita'])
regra2 = control.Rule(servico['ok'], gorjeta['media'])
regra3 = control.Rule(servico['horrivel'] & comida['horrivel'], gorjeta['pouca'])

controle = control.ControlSystem([regra1, regra2, regra3])
simulador = control.ControlSystemSimulation(controle)

simulador.input['servico'] = 30.5
simulador.input['comida'] = 15.4

simulador.compute()

gorjeta.view(sim=simulador)
servico.view(sim=simulador)
comida.view(sim=simulador)