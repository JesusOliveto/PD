/*
    ejemplo codigo prolog
*/

% reglas
padre(juan, maria).
padre(juan, pedro).
padre(ana, maria).
padre(ana, pedro).
padre(jose, ana).
padre(jose, juan).

% hechos
hombre(juan).
hombre(pedro).
hombre(jose).
mujer(maria).
mujer(ana).

% consultas
% ?- padre(juan, maria).
% true.

% ?- padre(juan, X).
% X = maria ;
% X = pedro.

% ?- padre(X, Y).
% X = jose,
% Y = ana ;
% X = jose,
% Y = juan ;
% X = juan,
% Y = maria ;
% X = juan,
% Y = pedro ;
% X = ana,
% Y = maria ;
% X = ana,
% Y = pedro.

% ?- padre(X, Y), mujer(Y).
% X = ana,
% Y = maria ;
% X = ana,
% Y = pedro ;
% X = juan,
% Y = maria ;
% X = juan,
% Y = pedro.

% ?- padre(X, Y), mujer(Y), hombre(X).
% X = ana,
% Y = maria ;
% X = juan,
% Y = maria.

% ?- padre(X, Y), mujer(Y), hombre(X).
% X = ana,
% Y = maria ;
% X = juan,
% Y = maria.

% ?- padre(X, Y), mujer(Y), hombre(X).
% X = ana,
% Y = maria ;
% X = juan,
% Y = maria.

% ?- padre(juan, X), padre(X, Y).
% X = maria,
% Y = ana ;
% X = maria,
% Y = juan ;
% X = pedro,
% Y = ana ;
% X = pedro,
% Y = juan.

% ?- padre(X, Y), padre(Y, Z).
% X = jose,
% Y = ana,
% Z = maria ;
% X = jose,
% Y = ana,
% Z = pedro ;
% X = jose,
% Y = juan,
% Z = maria ;
% X = jose,
% Y = juan,
% Z = pedro ;

