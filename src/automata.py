"""Implementação de autômatos finitos."""
from unittest import result


def load_automata(filename):

    try:
        with open(filename, "rt") as file:
            lines = file.read().strip().splitlines()

            Sigma = lines[0]
            Q = lines[1]
            F = lines[2]
            q0 = lines[3]
            transitions = lines[4:]

            delta = {state: {} for state in Q}
            for transition in transitions:
                splitteddelta = transition.split()
                state_a, symbol, state_b = splitteddelta[0], splitteddelta[1], splitteddelta[2]
                if symbol in delta[state_a]:
                    delta[state_a][symbol] = state_b
            return Q, Sigma, delta, q0, set(F)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {filename} não encontrado.")
    except Exception as error:
        raise error


def process(automata, words):

    Q, Sigma, delta, q0, F = automata
    answer = {}
    for word in words:
        current_state = q0
        invalid = False

        for char in word:
            if char not in Sigma:

                answer[word] = "INVÁLIDA"
                invalid = True
                break
            try:
                current_state = delta[current_state][char]
            except KeyError:
                answer[word] = "REJEITA"
                invalid = True
                break
        if not invalid:
            if current_state in F:
                answer[word] = "ACEITA"
            else:
                answer[word] = "REJEITA"
    return answer
