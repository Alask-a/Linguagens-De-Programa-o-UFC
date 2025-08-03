% Fatos: relação de filhos
% filho(Filho, Pai).
filho(joao, carlos).
filho(maria, carlos).
filho(carlos, jose).
filho(ana, jose).
filho(pedro, joana).

% Fatos: relação de mães
% filho(Filho, Mae).
filho(joao, ana).
filho(maria, ana).
filho(carlos, maria).
filho(ana, maria).
filho(pedro, maria).

% Definindo pai
pai(Pai, Filho) :- filho(Filho, Pai), homem(Pai).

% Definindo mãe
mae(Mae, Filho) :- filho(Filho, Mae), mulher(Mae).

% Fatos: definição de gênero
homem(carlos).
homem(jose).
homem(joao).
homem(pedro).

mulher(ana).
mulher(maria).
mulher(joana).

% Regra: avô (pai do pai ou pai da mãe)
avo(Avô, Neto) :-
    pai(Avô, Pai),
    pai(Pai, Neto).

avo(Avô, Neto) :-
    pai(Avô, Mae),
    mae(Mae, Neto).

% Regra: avó (mãe do pai ou mãe da mãe)
avo(Avó, Neto) :-
    mae(Avó, Pai),
    pai(Pai, Neto).

avo(Avó, Neto) :-
    mae(Avó, Mae),
    mae(Mae, Neto).

% Regra: irmão (mesmo pai e mesma mãe, e são diferentes)
irmao(X, Y) :-
    pai(P, X), pai(P, Y),
    mae(M, X), mae(M, Y),
    X \= Y.
