"""
Variáveis principais do dataset da Premier League (1993/1994 a 2024/2025):

HomeTeam       - Time mandante (que joga em casa)
AwayTeam       - Time visitante
FTHG           - Gols do time da casa no tempo regulamentar (Full Time Home Goals)
FTAG           - Gols do time visitante no tempo regulamentar (Full Time Away Goals)
FTR            - Resultado final (H - Vitória do mandante, A - Vitória do visitante, D - Empate)
HTHG           - Gols do time da casa no primeiro tempo (Half Time Home Goals)
HTAG           - Gols do time visitante no primeiro tempo (Half Time Away Goals)
HTR            - Resultado parcial no intervalo (H - Liderança do mandante, A - Liderança do visitante, D - Empate)
HS             - Finalizações totais do time da casa (Total de chutes a gol)
AS             - Finalizações totais do time visitante
HST            - Finalizações certeiras do time da casa (Chutes no alvo)
AST            - Finalizações certeiras do time visitante
HC             - Escanteios a favor do time da casa (Corner kicks)
AC             - Escanteios a favor do time visitante
HY             - Cartões amarelos acumulados pelo time da casa
AY             - Cartões amarelos acumulados pelo time visitante
HR             - Cartões vermelhos diretos do time da casa
AR             - Cartões vermelhos diretos do time visitante
HF             - Faltas cometidas pelo time da casa (Home Fouls)
AF             - Faltas cometidas pelo time visitante
Attendance     - Público presente no estádio
Referee        - Árbitro da partida

Variáveis adicionais importantes:
Date           - Data da partida (formato DD/MM/YYYY)
Div            - Divisão/liga (E0 = Premier League)
B365H          - Odds Bet365 para vitória do mandante
B365D          - Odds Bet365 para empate
B365A          - Odds Bet365 para vitória do visitante
BbAH           - Número total de apostas no Asian Handicap
BbAv<AH/H/A>   - Média de odds no mercado de handicaps asiáticos

FEATURE ENGINEERING - VARIÁVEIS CRIADAS PARA MODELAGEM

Variáveis de Rating FIFA:
OverHome        - Overall rating FIFA do time da casa (0-100)
OverAway        - Overall rating FIFA do time visitante (0-100)
AttOverHome     - Rating de ataque FIFA do time da casa
MidOverHome     - Rating de meio-campo FIFA do time da casa
DefOverHome     - Rating de defesa FIFA do time da casa
AttOverAway     - Rating de ataque FIFA do time visitante
MidOverAway     - Rating de meio-campo FIFA do time visitante
DefOverAway     - Rating de defesa FIFA do time visitante
DiffOverall     - Diferença entre ratings FIFA totais (Home - Away)
DiffAttack      - Diferença entre ratings de ataque (Home - Away)
DiffMidfield    - Diferença entre ratings de meio-campo (Home - Away)
DiffDefense     - Diferença entre ratings de defesa (Home - Away)

Variáveis de Diferença de Gols:
MHTGD           - Margem de gols do time da casa no jogo (FTHG - FTAG)
MATGD           - Margem de gols do time visitante no jogo (FTAG - FTHG)
GoalsDiffHome   - Saldo acumulado de gols do time da casa na temporada
GoalsDiffAway   - Saldo acumulado de gols do time visitante na temporada
GoalsDiff       - Diferença entre saldos acumulados (Home - Away)

Variáveis KPP (k-Past Performances):
HomeGoalsKPP    - Média de gols do time da casa nos últimos k jogos (k=5)
AwayGoalsKPP    - Média de gols do time visitante nos últimos k jogos
GoalsKPP        - Diferença entre médias de gols (HomeKPP - AwayKPP)
HomeCornersKPP  - Média de escanteios do time da casa nos últimos k jogos
AwayCornersKPP  - Média de escanteios do time visitante nos últimos k jogos
CornersKPP      - Diferença entre médias de escanteios (HomeKPP - AwayKPP)
HomeShotTargetKPP - Média de finalizações certeiras do time da casa (últimos k)
AwayShotTargetKPP - Média de finalizações certeiras do time visitante (últimos k)
ShotsTargetKPP  - Diferença entre médias de finalizações (HomeKPP - AwayKPP)

Variáveis de Sequência de Resultados (Streak):
HomeStreak      - Pontos conquistados pelo time da casa nos últimos k jogos (normalizado)
AwayStreak      - Pontos conquistados pelo time visitante nos últimos k jogos (normalizado)
Streak          - Diferença entre sequências de pontos (HomeStreak - AwayStreak)
HomeWeightedStreak - Sequência ponderada (jogos recentes têm maior peso)
AwayWeightedStreak - Sequência ponderada do visitante
WeightedStreak  - Diferença entre sequências ponderadas (Home - Away)
"""

